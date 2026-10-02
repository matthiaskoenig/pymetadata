"""Testing unichem."""

from pathlib import Path
from typing import Any

import pytest
import requests

from pymetadata.webservices.unichem import UnichemQuery, UnichemSource


def test_source_from_dict_current_fields() -> None:
    """Test creating a source from the fields UniChem answers with."""
    source = UnichemSource.from_dict(
        {
            "UCICount": 29916004,
            "baseIdUrl": "https://www.surechembl.org/chemical/",
            "created": None,
            "description": "SureChEMBL extracts chemistry from patents.",
            "lastChecked": "2026-09-15",
            "name": "surechembl",
            "nameLabel": "SureChEMBL",
            "nameLong": "SureChEMBL",
            "private": False,
            "sourceID": 15,
            "srcDetails": None,
            "srcLastUpdated": "2026-09-12 00:49:52",
            "srcUrl": "https://www.surechembl.org/",
            "updateComments": None,
        }
    )
    assert source.sourceID == 15
    assert source.name == "surechembl"
    assert source.baseIdUrl == "https://www.surechembl.org/chemical/"
    assert source.lastChecked == "2026-09-15"
    assert source.srcLastUpdated == "2026-09-12 00:49:52"


def test_source_from_dict_schema_changes() -> None:
    """Test that added and removed fields of UniChem do not break a source.

    UniChem changed the fields of a source without notice, e.g., `lastChecked`
    appeared and `srcReleaseNumber` disappeared.
    """
    source = UnichemSource.from_dict(
        {"sourceID": 1, "name": "chembl", "srcReleaseNumber": 1, "newField": "x"}
    )
    assert source.sourceID == 1
    assert source.name == "chembl"
    assert source.baseIdUrl is None
    assert not hasattr(source, "newField")


def test_get_sources(tmp_path: Path) -> None:
    """Test retrieving sources."""
    cache_path: Path = tmp_path
    sources = UnichemQuery(cache=True, cache_path=cache_path).get_sources()
    assert sources
    assert (cache_path / "unichem_sources.json").exists()

    sources = UnichemQuery(cache=True, cache_path=cache_path).get_sources()
    assert sources


def test_get_source_exists() -> None:
    """Test existing source."""
    query = UnichemQuery(cache=False)
    source: UnichemSource | None = query.sources.get(1, None)
    assert source
    assert isinstance(source, UnichemSource)


def test_get_source_missing() -> None:
    """Test missing source."""
    query = UnichemQuery(cache=False)
    source: UnichemSource | None = query.sources.get(-1, None)
    assert source is None


def test_query_xref_for_inchikey_no_cache(tmp_path: Path) -> None:
    """Test retrieving xrefs without cache."""
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    xrefs = UnichemQuery(cache=False, cache_path=tmp_path).query_xrefs_for_inchikey(
        inchikey=inchikey
    )
    assert xrefs


def test_query_xref_for_inchikey_cache(tmp_path: Path) -> None:
    """Test retrieving xrefs with cache."""
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    xrefs1 = UnichemQuery(cache=False, cache_path=tmp_path).query_xrefs_for_inchikey(
        inchikey=inchikey
    )
    xrefs2 = UnichemQuery(
        cache=True,
        cache_path=tmp_path,
    ).query_xrefs_for_inchikey(inchikey=inchikey)
    assert xrefs1
    assert xrefs2
    assert len(xrefs1) == len(xrefs2)


def test_query_xrefs_server_error(tmp_path: Path, monkeypatch: Any) -> None:
    """Test that a server error does not surface as a JSONDecodeError.

    The UniChem service intermittently answers with a HTML error page, see #73.
    """
    html_error = "<!doctype html><html lang='en'>500 Internal Server Error</html>"

    class FakeResponse:
        status_code = 500
        text = html_error
        content = html_error.encode()

        def json(self) -> Any:
            raise requests.exceptions.JSONDecodeError("Expecting value", html_error, 0)

    # the sources are not the subject here, they must not be queried
    monkeypatch.setattr(
        UnichemQuery,
        "sources",
        {1: UnichemSource(sourceID=1, name="chembl", baseIdUrl="https://x.org/")},
    )
    # the queries go through `get_json`, which uses the session of `webservice`
    monkeypatch.setattr(
        "pymetadata.webservices.webservice.get_session",
        lambda: type("S", (), {"get": lambda self, url, **kw: FakeResponse()})(),
    )

    xrefs = UnichemQuery(cache=False, cache_path=tmp_path).query_xrefs_for_inchikey(
        inchikey="NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    )
    assert xrefs == []


class FakeUnichem:
    """Stand-in for `get_json` which answers like the UniChem web service."""

    def __init__(self) -> None:
        """Start without recorded queries."""
        self.urls: list[str] = []

    def __call__(self, url: str) -> Any:
        """Record the query and answer with a single ChEMBL entry."""
        self.urls.append(url)
        return [{"src_id": "1", "src_compound_id": "CHEMBL1"}]


def offline_query(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, cache: bool
) -> tuple[UnichemQuery, FakeUnichem]:
    """Create a query which answers without network."""
    fake = FakeUnichem()
    monkeypatch.setattr("pymetadata.webservices.unichem.get_json", fake)
    monkeypatch.setattr(
        UnichemQuery,
        "sources",
        {1: UnichemSource(sourceID=1, name="chembl", baseIdUrl="https://x.org/")},
    )
    query = UnichemQuery(cache=cache, cache_path=tmp_path / "cache")
    return query, fake


def test_query_xrefs_normalizes_inchikey(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that a lower case InChIKey is queried and cached upper case."""
    query, fake = offline_query(tmp_path, monkeypatch, cache=True)

    xrefs = query.query_xrefs_for_inchikey("ngbfqhcmquljnz-uhfffaoysa-n")

    assert [xref.accession for xref in xrefs] == ["CHEMBL1"]
    assert fake.urls == [
        "https://www.ebi.ac.uk/unichem/rest/inchikey/NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    ]
    assert (
        tmp_path / "cache" / "unichem" / "NGBFQHCMQULJNZ-UHFFFAOYSA-N.json"
    ).exists()


@pytest.mark.parametrize("inchikey", ["../../evil", "yxsdfasdfs", ""])
def test_query_xrefs_rejects_invalid_inchikey(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, inchikey: str
) -> None:
    """Test that an invalid InChIKey is neither queried nor cached."""
    query, fake = offline_query(tmp_path, monkeypatch, cache=True)

    assert query.query_xrefs_for_inchikey(inchikey) == []
    assert fake.urls == []
    assert list(tmp_path.rglob("*.json")) == []


def test_query_xrefs_without_cache_writes_nothing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that `cache=False` neither creates the cache nor writes to it."""
    query, _ = offline_query(tmp_path, monkeypatch, cache=False)

    assert query.query_xrefs_for_inchikey("NGBFQHCMQULJNZ-UHFFFAOYSA-N")
    assert not (tmp_path / "cache").exists()
