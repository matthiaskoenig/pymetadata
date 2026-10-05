"""Test ChEBI."""

from pathlib import Path
from typing import Any

import pytest

from pymetadata.webservices.chebi import ChebiQuery

WATER = {
    "ascii_name": "water",
    "definition": "An oxygen hydride.",
    "chemical_data": {"formula": "H2O", "charge": 0, "mass": "18.015"},
    "default_structure": {"standard_inchi_key": "XLYOFNOQVPJJNP-UHFFFAOYSA-N"},
}


class FakeChebi:
    """Stand-in for `get_json` which answers like the ChEBI web service."""

    def __init__(self) -> None:
        """Start without recorded queries."""
        self.queries: list[tuple[str, dict[str, str] | None]] = []

    def __call__(self, url: str, params: dict[str, str] | None = None) -> Any:
        """Record the query and answer with water, every other id is unknown."""
        self.queries.append((url, params))
        assert params is not None
        chebi = params["chebi_ids"]
        if chebi == "CHEBI:15377":
            return {chebi: {"exists": True, "data": WATER}}
        return {chebi: {"exists": False, "data": None}}


@pytest.fixture
def fake_chebi(monkeypatch: pytest.MonkeyPatch) -> FakeChebi:
    """Answer the ChEBI queries without network."""
    fake = FakeChebi()
    monkeypatch.setattr("pymetadata.webservices.chebi.get_json", fake)
    return fake


@pytest.mark.parametrize("chebi", ["CHEBI:15377", "chebi:15377", "15377"])
def test_chebi_normalizes_the_id(
    tmp_path: Path, fake_chebi: FakeChebi, chebi: str
) -> None:
    """Test that the id spellings are queried and cached as `CHEBI:<number>`."""
    data = ChebiQuery.query(chebi=chebi, cache=True, cache_path=tmp_path)

    assert data["chebi"] == "CHEBI:15377"
    assert data["name"] == "water"
    url, params = fake_chebi.queries[0]
    assert "?" not in url
    assert params == {"chebi_ids": "CHEBI:15377"}
    assert (tmp_path / "chebi" / "CHEBI%3A15377.json").exists()


@pytest.mark.parametrize("chebi", ["../../evil", "CHEBI:abc", "CHEBI:1&x=2"])
def test_chebi_rejects_invalid_id(
    tmp_path: Path, fake_chebi: FakeChebi, chebi: str
) -> None:
    """Test that an invalid id is neither queried nor cached."""
    cache_path = tmp_path / "cache"

    assert ChebiQuery.query(chebi=chebi, cache=True, cache_path=cache_path) == {}
    assert fake_chebi.queries == []
    assert list(tmp_path.rglob("*.json")) == []


def test_chebi_unknown_id_is_empty(tmp_path: Path, fake_chebi: FakeChebi) -> None:
    """Test that an id unknown to ChEBI gives empty information."""
    assert ChebiQuery.query("CHEBI:999999999", cache=True, cache_path=tmp_path) == {}
    assert not (tmp_path / "chebi" / "CHEBI%3A999999999.json").exists()


def test_chebi_without_cache_writes_nothing(
    tmp_path: Path, fake_chebi: FakeChebi
) -> None:
    """Test that `cache=False` neither creates the cache nor writes to it."""
    cache_path = tmp_path / "cache"

    assert ChebiQuery.query("CHEBI:15377", cache=False, cache_path=cache_path)
    assert not cache_path.exists()


def test_chebi_corrupt_cache_is_refreshed(
    tmp_path: Path, fake_chebi: FakeChebi
) -> None:
    """Test that a corrupt cache file is queried again instead of failing."""
    chebi_path = tmp_path / "chebi" / "CHEBI%3A15377.json"
    chebi_path.parent.mkdir(parents=True)
    chebi_path.write_text("{not json")

    data = ChebiQuery.query("CHEBI:15377", cache=True, cache_path=tmp_path)

    assert data["name"] == "water"
    assert len(fake_chebi.queries) == 1


@pytest.mark.parametrize(
    "chebi", ["CHEBI:2668", "CHEBI:138366", "CHEBI:9637", "CHEBI:155897"]
)
def test_chebi(tmp_path: Path, chebi: str) -> None:
    """Test that chebi information can be accessed."""
    cache_path = tmp_path / "cache"
    keys = ["chebi", "formula", "charge", "mass", "inchikey"]

    d = ChebiQuery.query(chebi=chebi, cache=False, cache_path=cache_path)
    assert d
    for key in keys:
        assert key in d

    d = ChebiQuery.query(chebi=chebi, cache=True, cache_path=cache_path)
    for key in keys:
        assert key in d
    for key in keys:
        assert key in d


SVG = b"<?xml version='1.0'?><svg xmlns='http://www.w3.org/2000/svg'></svg>"


def test_structure_is_cached(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The structure is fetched once and cached as an svg file."""
    urls: list[str] = []

    def get_bytes(url: str, params: Any = None) -> bytes:
        urls.append(url)
        return SVG

    monkeypatch.setattr("pymetadata.webservices.chebi.get_bytes", get_bytes)
    assert ChebiQuery.structure("CHEBI:15377", cache=True, cache_path=tmp_path) == SVG
    assert ChebiQuery.structure("chebi:15377", cache=True, cache_path=tmp_path) == SVG
    assert urls == [
        "https://www.ebi.ac.uk/chebi/backend/api/public/compound/15377/structure/"
    ]
    assert (tmp_path / "chebi" / "CHEBI%3A15377.svg").read_bytes() == SVG


@pytest.mark.parametrize("chebi", ["../../evil", "CHEBI:abc", ""])
def test_structure_rejects_invalid_id(tmp_path: Path, chebi: str) -> None:
    """An invalid id has no structure and queries nothing."""
    assert ChebiQuery.structure(chebi, cache=True, cache_path=tmp_path) is None


def test_structure_unknown(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A compound without a structure answers None."""
    from pymetadata.webservices.webservice import WebserviceNotFoundError

    def missing(url: str, params: Any = None) -> bytes:
        raise WebserviceNotFoundError("404")

    monkeypatch.setattr("pymetadata.webservices.chebi.get_bytes", missing)
    assert ChebiQuery.structure("CHEBI:1", cache=True, cache_path=tmp_path) is None
