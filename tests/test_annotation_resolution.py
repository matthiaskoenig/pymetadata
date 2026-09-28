"""Regression tests for resolver URLs and ontology identifiers."""

import urllib.parse
from pathlib import Path
from types import SimpleNamespace

import pytest

from pymetadata.core.annotation import (
    BQB,
    ProviderType,
    RDFAnnotation,
    RDFAnnotationData,
)
from pymetadata.webservices.ols import ONTOLOGIES, OLSQuery


@pytest.mark.parametrize("prefix", ["CMO", "cmo", "DRON", "MMO", "SCDO"])
def test_bioregistry_resolves_without_identifiers_namespace(
    prefix: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Bioregistry terms resolve through configured OLS ontologies."""

    def unexpected_registry() -> None:
        raise AssertionError(
            "Configured Bioregistry terms need no identifiers registry"
        )

    monkeypatch.setattr("pymetadata.core.annotation.get_registry", unexpected_registry)
    monkeypatch.setattr("pymetadata.webservices.ols.get_registry", unexpected_registry)
    query = OLSQuery(ONTOLOGIES, cache_path=tmp_path)
    monkeypatch.setattr("pymetadata.core.annotation.get_ols_query", lambda: query)
    urls: list[str] = []

    def respond(url: str) -> dict:
        urls.append(urllib.parse.unquote(urllib.parse.unquote(url)))
        return {"label": "body height", "description": ["Height of a body."]}

    monkeypatch.setattr("pymetadata.webservices.ols.get_json", respond)
    resource = f"https://bioregistry.io/{prefix}:0000003"
    annotation = RDFAnnotation(BQB.IS, resource)
    data = RDFAnnotationData(annotation)

    assert annotation.collection == prefix.lower()
    assert annotation.provider == ProviderType.BIOREGISTRY_IO
    assert annotation.resource_normalized == resource
    assert data.label == "body height"
    assert data.errors == []
    assert data.warnings == []
    assert annotation.validate()
    # Repeated resolution uses the successful OLS response already on disk.
    assert RDFAnnotationData(annotation).label == "body height"
    assert urls == [
        f"https://www.ebi.ac.uk/ols4/api/ontologies/{prefix.lower()}/terms/"
        f"http://purl.obolibrary.org/obo/{prefix.upper()}_0000003"
    ]


@pytest.mark.parametrize(
    "ontology,term,iri",
    [
        ("sio", "SIO_001013", "http://semanticscience.org/resource/SIO_001013"),
        ("obi", "OBI_0000070", "http://purl.obolibrary.org/obo/OBI_0000070"),
        ("chebi", "chebi:37924", "http://purl.obolibrary.org/obo/CHEBI_37924"),
        ("chebi", "CHEBI:37924", "http://purl.obolibrary.org/obo/CHEBI_37924"),
        ("sio", "001013", "http://semanticscience.org/resource/SIO_001013"),
        ("fma", "10951", "http://purl.org/sig/ont/fma/fma10951"),
        ("fma", "FMA:10951", "http://purl.org/sig/ont/fma/fma10951"),
        ("fma", "FMA_10951", "http://purl.org/sig/ont/fma/fma10951"),
    ],
)
def test_ols_iri_prefix(ontology: str, term: str, iri: str, tmp_path: Path) -> None:
    """A local identifier or CURIE contributes its ontology prefix only once."""
    assert OLSQuery(ONTOLOGIES, cache_path=tmp_path).get_iri(ontology, term) == iri


def test_unknown_bioregistry_ontology_is_not_guessed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """An unconfigured ontology without an OLS provider stays unresolved."""
    registry = SimpleNamespace(ns_dict={})
    monkeypatch.setattr("pymetadata.webservices.ols.get_registry", lambda: registry)
    query = OLSQuery(ONTOLOGIES, cache_path=tmp_path)
    monkeypatch.setattr("pymetadata.core.annotation.get_ols_query", lambda: query)

    def unexpected_request(url: str) -> dict:
        raise AssertionError(f"Unsupported ontology must not be queried: {url}")

    monkeypatch.setattr("pymetadata.webservices.ols.get_json", unexpected_request)
    data = RDFAnnotationData(
        RDFAnnotation(BQB.IS, "https://bioregistry.io/unknown:123")
    )
    assert data.label is None
    assert data.errors == []
    assert data.warnings == ["'unknown' is not on OLS."]


@pytest.mark.parametrize(
    "resource",
    [
        "https://bioregistryXio/CMO:0000003",
        "https://bioregistry.io/CMO:",
        "https://bioregistry.io/CMO",
    ],
)
def test_non_bioregistry_identifier_url_is_preserved(resource: str) -> None:
    """Lookalike hosts and URLs without an accession are arbitrary resources."""
    annotation = RDFAnnotation(BQB.IS, resource)
    assert annotation.provider == ProviderType.NONE
    assert annotation.collection is None
    assert annotation.resource_normalized == resource
