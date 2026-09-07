"""Testing that the web service queries survive an outage.

If a service cannot be reached and content is cached, the cached content is
used however old it is: the library logs a warning instead of failing, so that
working offline keeps working with whatever was cached before.
"""

import logging
import os
import time
import urllib.parse
from pathlib import Path
from typing import Any

import pytest

import pymetadata
from pymetadata.cache import write_json_cache
from pymetadata.webservices.chebi import ChebiQuery
from pymetadata.webservices.ols import ONTOLOGIES, OLSQuery
from pymetadata.webservices.registry import Namespace, Registry
from pymetadata.webservices.unichem import UnichemQuery
from pymetadata.webservices.webservice import WebserviceError


@pytest.fixture
def offline(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make every web service query fail as if there were no network."""

    def fail(url: str) -> Any:
        raise WebserviceError(f"Service is not reachable for '{url}': offline")

    for module in ["chebi", "ols", "registry", "unichem"]:
        monkeypatch.setattr(f"pymetadata.webservices.{module}.get_json", fail)


def age_cache(cache_path: Path, hours: float) -> None:
    """Backdate a cache file by the given number of hours."""
    old = time.time() - hours * 3600
    os.utime(cache_path, (old, old))


def test_chebi_falls_back_to_outdated_cache(
    tmp_path: Path, offline: None, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that ChEBI information survives an outage."""
    chebi = "CHEBI:2668"
    cached = {"chebi": chebi, "name": "amiloride", "inchikey": "XSDQTOBWRPYKKA"}
    cache_path = tmp_path / "chebi" / "CHEBI%3A2668.json"
    write_json_cache(data=cached, cache_path=cache_path)
    # far beyond the cache duration, so the query is attempted and fails
    age_cache(cache_path, hours=100 * 24)

    with caplog.at_level(logging.WARNING):
        data = ChebiQuery.query(chebi=chebi, cache=True, cache_path=tmp_path)

    assert data == cached
    assert "could not be refreshed" in caplog.text


def test_chebi_without_cache_returns_empty(tmp_path: Path, offline: None) -> None:
    """Test that ChEBI answers with nothing if it is neither cached nor reachable."""
    assert ChebiQuery.query(chebi="CHEBI:2668", cache=True, cache_path=tmp_path) == {}


def ols_registry() -> Registry:
    """Build a registry with a single collection resolved by OLS."""
    # `Namespace.__post_init__` builds the resources from dictionaries
    resource = {
        "id": 1,
        "providerCode": "ols",
        "name": "Ontology Lookup Service",
        "urlPattern": "https://www.ebi.ac.uk/ols4/ontologies/chebi/terms/{$id}",
        "mirId": None,
        "description": "",
        "official": True,
        "sampleId": None,
        "resourceHomeUrl": None,
        "institution": {},
        "location": {},
        "deprecated": False,
        "deprecationDate": "",
    }
    namespace = Namespace(
        id="2",
        prefix="chebi",
        name="ChEBI",
        pattern=r"^CHEBI:\d+$",
        namespaceEmbeddedInLui=True,
        description="",
        resources=[resource],
    )
    registry = Registry.__new__(Registry)
    registry.ns_dict = {"chebi": namespace}
    return registry


def test_ols_falls_back_to_outdated_cache(
    tmp_path: Path,
    offline: None,
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Test that an OLS term survives an outage."""
    # the registry is not the subject here, it must not query identifiers.org
    monkeypatch.setattr(
        "pymetadata.webservices.ols.get_registry", lambda: ols_registry()
    )

    query = OLSQuery(ontologies=ONTOLOGIES, cache_path=tmp_path, cache=True)
    cached = {"label": "polysaccharide", "errors": [], "warnings": []}
    urliri = urllib.parse.quote(
        urllib.parse.quote(
            query.get_iri(ontology="chebi", term="CHEBI:37924"), safe=""
        ),
        safe="",
    )
    cache_path = query.cache_path / f"{urliri}.json"
    write_json_cache(data=cached, cache_path=cache_path)
    age_cache(cache_path, hours=100 * 24)

    with caplog.at_level(logging.WARNING):
        data = query.query_ols(ontology="chebi", term="CHEBI:37924")

    assert data == cached
    assert "could not be refreshed" in caplog.text


def test_ols_without_cache_reports_the_error(
    tmp_path: Path, offline: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that OLS reports the outage if the term is not cached."""
    monkeypatch.setattr(
        "pymetadata.webservices.ols.get_registry", lambda: ols_registry()
    )
    query = OLSQuery(ontologies=ONTOLOGIES, cache_path=tmp_path, cache=True)

    data = query.query_ols(ontology="chebi", term="CHEBI:37924")

    assert data["errors"]
    assert "not reachable" in data["errors"][0]


def test_unichem_sources_fall_back_to_outdated_cache(
    tmp_path: Path, offline: None, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the UniChem sources survive an outage."""
    source = {
        "sourceID": 1,
        "srcUrl": "https://www.ebi.ac.uk/chembl/",
        "name": "chembl",
        "nameLabel": "ChEMBL",
        "nameLong": "ChEMBL",
        "UCICount": 0,
        "baseIdUrl": "https://www.ebi.ac.uk/chembl/compound_report_card/",
        "description": "",
        "created": "",
        "lastUpdated": "",
        "srcDetails": "",
        "srcReleaseDate": "",
        "srcReleaseNumber": 1,
        "updateComments": "",
        "private": False,
    }
    cache_path = tmp_path / "unichem_sources.json"
    write_json_cache(data={"1": source}, cache_path=cache_path)
    age_cache(cache_path, hours=100 * 24)

    with caplog.at_level(logging.WARNING):
        sources = UnichemQuery(cache=True, cache_path=tmp_path).get_sources()

    assert sources[1].name == "chembl"
    assert "could not be refreshed" in caplog.text


def test_unichem_sources_without_cache_raise(tmp_path: Path, offline: None) -> None:
    """Test that UniChem raises if the sources are neither cached nor reachable."""
    UnichemQuery.sources = {}
    with pytest.raises(WebserviceError, match="not reachable"):
        UnichemQuery(cache=True, cache_path=tmp_path)


def test_unichem_xrefs_fall_back_to_outdated_cache(
    tmp_path: Path, offline: None, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that the UniChem cross references survive an outage."""
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    write_json_cache(
        data={"1": {"sourceID": 1}}, cache_path=tmp_path / "unichem_sources.json"
    )
    xref_path = tmp_path / "unichem" / f"{inchikey}.json"
    write_json_cache(data={"error": "none"}, cache_path=xref_path)
    age_cache(xref_path, hours=100 * 24)

    query = UnichemQuery.__new__(UnichemQuery)
    query.cache_path = tmp_path
    query.cache = True

    with caplog.at_level(logging.WARNING):
        xrefs = query.query_xrefs_for_inchikey(inchikey=inchikey)

    assert xrefs == []
    assert "could not be refreshed" in caplog.text


def test_registry_falls_back_to_outdated_cache(
    tmp_path: Path, offline: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that the registry survives an outage."""
    monkeypatch.setattr(pymetadata, "CACHE_PATH", tmp_path)
    namespace = {
        "prefix": "chebi",
        "name": "ChEBI",
        "pattern": r"^CHEBI:\d+$",
        "description": "",
        "mirId": "MIR:00000002",
        "created": "",
        "modified": "",
        "sampleId": "CHEBI:36927",
        "namespaceEmbeddedInLui": True,
        "deprecated": False,
        "deprecationDate": None,
        "id": 2,
        "resources": [],
    }
    registry_path = tmp_path / "identifiers_registry.json"
    write_json_cache(data={"chebi": namespace}, cache_path=registry_path)
    age_cache(registry_path, hours=100 * 24)

    registry = Registry()

    assert registry.ns_dict["chebi"].pattern == r"^CHEBI:\d+$"


def test_registry_without_cache_raises(
    tmp_path: Path, offline: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that the registry raises if it is neither cached nor reachable."""
    monkeypatch.setattr(pymetadata, "CACHE_PATH", tmp_path)
    with pytest.raises(WebserviceError, match="not reachable"):
        Registry()


def test_registry_without_cache_does_not_fall_back(
    tmp_path: Path, offline: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that `cache=False` does not read the cache, not even on a failure."""
    monkeypatch.setattr(pymetadata, "CACHE_PATH", tmp_path)
    write_json_cache(
        data={"chebi": {}}, cache_path=tmp_path / "identifiers_registry.json"
    )

    with pytest.raises(WebserviceError, match="not reachable"):
        Registry(cache=False)
