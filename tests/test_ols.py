"""Testing OLS."""

from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

import pymetadata
from pymetadata.core.annotation import BQB, RDFAnnotation, RDFAnnotationData
from pymetadata.webservices.ols import ONTOLOGIES, OLSQuery


def test_ols_query() -> None:
    """Test OLS query."""
    data = [
        (BQB.IS, "chebi/CHEBI:37924"),
        (BQB.IS, "ncit/C66872"),
    ]
    annotations = [RDFAnnotation(qualifier=d[0], resource=d[1]) for d in data]

    for a in annotations:
        info = RDFAnnotationData(a).query_ols()
        assert info
        for key in ["description", "label", "synonyms", "xrefs"]:
            assert key in info


def test_annotation_data_to_dict() -> None:
    """Test that the resolved annotation converts to a dictionary.

    Regression test for 0.6.0, where `RDFAnnotationData` had no `provider`
    and `to_dict` failed on the normalized resource.
    """
    annotation = RDFAnnotation(qualifier=BQB.IS, resource="chebi/CHEBI:37924")
    data = RDFAnnotationData(annotation)

    assert data.provider == annotation.provider
    info = data.to_dict()
    assert info["resource"] == "chebi/CHEBI:37924"
    assert info["resource_normalized"] == "https://identifiers.org/CHEBI:37924"
    assert info["collection"] == "chebi"
    assert info["term"] == "CHEBI:37924"


def test_ols_explicit_cache_false(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that `cache=False` is not overridden by `pymetadata.CACHE_USE`."""
    monkeypatch.setattr(pymetadata, "CACHE_USE", True)

    query = OLSQuery(ontologies=ONTOLOGIES, cache_path=tmp_path, cache=False)

    assert query.cache is False
    assert not (tmp_path / "ols").exists()


def test_ols_caches_long_iri(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that a term whose IRI is too long for a file name is cached."""

    def respond(url: str) -> Any:
        return {"label": "long"}

    monkeypatch.setattr("pymetadata.webservices.ols.get_json", respond)
    query = OLSQuery(ontologies=ONTOLOGIES, cache_path=tmp_path, cache=True)

    data = query.query_ols(ontology="chebi", term="CHEBI:" + "1" * 300)

    assert data["label"] == "long"
    cached = list((tmp_path / "ols").iterdir())
    assert len(cached) == 1
    assert len(cached[0].name.encode()) <= 255


def test_unknown_term_is_a_warning(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A term OLS does not know is a warning and no error, nothing is cached."""
    from pymetadata.webservices.webservice import WebserviceNotFoundError

    def missing(url: str, params: object = None) -> dict:
        raise WebserviceNotFoundError(f"'404' response for: '{url}'")

    monkeypatch.setattr("pymetadata.webservices.ols.get_json", missing)
    query = OLSQuery(ontologies=ONTOLOGIES, cache_path=tmp_path, cache=True)
    data = query.query_ols(ontology="go", term="GO:9999999")
    assert data == {"errors": [], "warnings": ["Term 'GO:9999999' is not on OLS."]}
    assert not any(tmp_path.rglob("*.json"))


def test_collection_not_on_ols_warns_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    """A collection without an ontology on OLS is no problem of the annotation."""
    registry = SimpleNamespace(ns_dict={})
    monkeypatch.setattr("pymetadata.webservices.ols.get_registry", lambda: registry)
    query = OLSQuery(ontologies=ONTOLOGIES, cache=False)
    assert query.query_ols(ontology="pubmed", term="10659856") == {
        "errors": [],
        "warnings": [],
    }


def test_process_response_reports_the_term_page() -> None:
    """The ontology, the IRI and the OLS page of the term are part of the response."""
    from pymetadata.webservices.ols import ONTOLOGIES, OLSQuery

    info = OLSQuery(ontologies=ONTOLOGIES, cache=False).process_response(
        {
            "errors": [],
            "warnings": [],
            "label": "glycolytic process",
            "ontology_name": "go",
            "iri": "http://purl.obolibrary.org/obo/GO_0006096",
        }
    )
    assert info["ontology"] == "go"
    assert info["iri"] == "http://purl.obolibrary.org/obo/GO_0006096"
    assert info["ols_url"] == (
        "https://www.ebi.ac.uk/ols4/ontologies/go/classes?iri="
        "http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0006096"
    )


def test_term_page_needs_ontology_and_iri() -> None:
    """Without an ontology or an IRI there is no term page."""
    from pymetadata.webservices.ols import ols_term_url

    assert ols_term_url(None, "http://purl.obolibrary.org/obo/GO_0006096") is None
    assert ols_term_url("go", None) is None
