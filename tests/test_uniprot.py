"""Test UniProt."""

import os
from pathlib import Path
from typing import Any

import pytest

from pymetadata.webservices.uniprot import UniprotQuery
from pymetadata.webservices.webservice import WebserviceError, WebserviceNotFoundError

HBA = {
    "entryType": "UniProtKB reviewed (Swiss-Prot)",
    "primaryAccession": "P69905",
    "uniProtkbId": "HBA_HUMAN",
    "proteinDescription": {
        "recommendedName": {"fullName": {"value": "Hemoglobin subunit alpha"}}
    },
    "organism": {"scientificName": "Homo sapiens"},
    "genes": [{"geneName": {"value": "HBA1"}}, {"geneName": {"value": "HBA2"}}],
    "comments": [
        {
            "commentType": "FUNCTION",
            "texts": [{"value": "Involved in oxygen transport."}],
        }
    ],
    "sequence": {"length": 142},
}


@pytest.fixture
def fake_uniprot(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """Answer P69905, every other accession is unknown."""
    queries: list[str] = []

    def get_json(url: str, params: Any = None) -> dict:
        queries.append(url)
        if url.endswith("/P69905.json"):
            return HBA
        raise WebserviceNotFoundError(f"'404' response for: '{url}'")

    monkeypatch.setattr("pymetadata.webservices.uniprot.get_json", get_json)
    return queries


def test_query(tmp_path: Path, fake_uniprot: list[str]) -> None:
    """The entry is reduced to name, organism, genes, length and function, and cached."""
    data = UniprotQuery.query("P69905", cache=True, cache_path=tmp_path)
    assert data == {
        "accession": "P69905",
        "entry": "HBA_HUMAN",
        "name": "Hemoglobin subunit alpha",
        "organism": "Homo sapiens",
        "genes": ["HBA1", "HBA2"],
        "length": 142,
        "function": "Involved in oxygen transport.",
    }
    assert (tmp_path / "uniprot" / "P69905.json").exists()
    assert UniprotQuery.query("P69905", cache=True, cache_path=tmp_path) == data
    assert len(fake_uniprot) == 1


@pytest.mark.parametrize("accession", ["Q00000", "../../x", "P69905&x=1", ""])
def test_unknown_or_invalid(
    tmp_path: Path, fake_uniprot: list[str], accession: str
) -> None:
    """An unknown or invalid accession answers no information."""
    assert UniprotQuery.query(accession, cache=True, cache_path=tmp_path) == {}


def test_outdated_cache_when_offline(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """An outdated cache is used when UniProt cannot be reached."""
    monkeypatch.setattr(
        "pymetadata.webservices.uniprot.get_json", lambda url, params=None: HBA
    )
    UniprotQuery.query("P69905", cache=True, cache_path=tmp_path)
    path = tmp_path / "uniprot" / "P69905.json"
    os.utime(path, (0, 0))

    def offline(url: str, params: Any = None) -> dict:
        raise WebserviceError("Service is not reachable")

    monkeypatch.setattr("pymetadata.webservices.uniprot.get_json", offline)
    assert UniprotQuery.query("P69905", cache=True, cache_path=tmp_path)["entry"] == (
        "HBA_HUMAN"
    )


def test_inactive_entry(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A merged or deleted entry answers no information."""
    monkeypatch.setattr(
        "pymetadata.webservices.uniprot.get_json",
        lambda url, params=None: {
            "entryType": "Inactive",
            "primaryAccession": "P00000",
        },
    )
    assert UniprotQuery.query("P00000", cache=False, cache_path=tmp_path) == {}
