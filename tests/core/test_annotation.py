"""Test annotations."""

import dataclasses
from typing import Any

import pytest

from pymetadata.core.annotation import ProviderType, RDFAnnotation, RDFAnnotationData
from pymetadata.core.miriam import BQB, BQM
from pymetadata.core.xref import is_url
from pymetadata.webservices.registry import Registry, Resource

rdf_annotation_data = [
    (
        BQB.IS,
        "https://identifiers.org/DOI:10.1016/j.jtbi.2004.04.039",
        "RDFAnnotation(BQB.IS|doi|10.1016/j.jtbi.2004.04.039|identifiers.org)",
    ),
    (
        BQB.IS,
        "NCIT:C75913",
        "RDFAnnotation(BQB.IS|ncit|C75913|identifiers.org)",
    ),
    (
        BQB.IS,
        "ncit:C75913",
        "RDFAnnotation(BQB.IS|ncit|C75913|identifiers.org)",
    ),
    (
        BQB.IS,
        "ncit/C75913",
        "RDFAnnotation(BQB.IS|ncit|C75913|identifiers.org)",
    ),
    (
        BQB.IS,
        "taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606|identifiers.org)",
    ),
    (
        BQB.IS,
        "taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/biomodels.sbo/SBO:0000247",
        "RDFAnnotation(BQB.IS|sbo|SBO:0000247|identifiers.org)",
    ),
    (
        BQB.IS,
        "urn:miriam:obo.go:GO%3A0005623",
        "RDFAnnotation(BQB.IS|go|GO:0005623|identifiers.org)",
    ),
    (
        BQB.IS,
        "urn:miriam:chebi:CHEBI%3A33699",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:33699|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "bto/BTO:0000089",
        "RDFAnnotation(BQB.IS|bto|BTO:0000089|identifiers.org)",
    ),
    (
        BQB.IS,
        "BTO:0000089",
        "RDFAnnotation(BQB.IS|bto|BTO:0000089|identifiers.org)",
    ),
    (
        BQB.IS,
        "CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012|identifiers.org)",
    ),
    (
        BQB.IS,
        "chebi/CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://en.wikipedia.org/wiki/Cytosol",
        "RDFAnnotation(BQB.IS|None|https://en.wikipedia.org/wiki/Cytosol|none)",
    ),
    (
        BQB.IS_VERSION_OF,
        "urn:miriam:uniprot:P03023",
        "RDFAnnotation(BQB.IS_VERSION_OF|uniprot|P03023|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012|identifiers.org)",
    ),
    (
        BQB.IS,
        "doi/10.3389/fphar.2025.1686415",
        "RDFAnnotation(BQB.IS|doi|10.3389/fphar.2025.1686415|identifiers.org)",
    ),
    (
        BQB.IS,
        "doi/10.5281/zenodo.17091694",
        "RDFAnnotation(BQB.IS|doi|10.5281/zenodo.17091694|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://bioregistry.io/chebi:15996",
        "RDFAnnotation(BQB.IS|chebi|chebi:15996|bioregistry.io)",
    ),
    (
        BQB.IS,
        "hmdb/HMDB0000122",
        "RDFAnnotation(BQB.IS|hmdb|HMDB0000122|identifiers.org)",
    ),
    (
        BQB.IS,
        "hmdb:HMDB0000122",
        "RDFAnnotation(BQB.IS|hmdb|HMDB0000122|identifiers.org)",
    ),
]


@pytest.mark.parametrize("qualifier,resource,expected", rdf_annotation_data)
def test_rdf_annotation(qualifier: BQB | BQM, resource: str, expected: str) -> None:
    """Test various RDF annotation patterns."""
    a = RDFAnnotation(qualifier=qualifier, resource=resource)
    assert a
    assert str(a) == expected


def test_check_term_pass() -> None:
    """Test that check term passes."""
    rdf_annotation = RDFAnnotation(qualifier=BQB.IS, resource="CHEBI:000012")
    assert rdf_annotation.check_miriam_term()


def test_check_bioregistry() -> None:
    """Test that check collection fails."""
    rdf_annotation = RDFAnnotation(
        qualifier=BQB.IS, resource="https://bioregistry.io/CHEBI:000012"
    )
    assert not rdf_annotation.check_miriam_term()


resource_normalized_data = [
    # namespace not embedded in the LUI: compact identifier `prefix:accession`
    # with the prefix from the identifiers.org registry (see #71)
    ("NCIT:C180619", "https://identifiers.org/ncit:C180619"),
    ("ncit:C180619", "https://identifiers.org/ncit:C180619"),
    ("ncit/C180619", "https://identifiers.org/ncit:C180619"),
    ("https://identifiers.org/NCIT:C180619", "https://identifiers.org/ncit:C180619"),
    ("https://identifiers.org/ncit/C180619", "https://identifiers.org/ncit:C180619"),
    ("http://identifiers.org/ncit/C180619", "https://identifiers.org/ncit:C180619"),
    ("taxonomy/9606", "https://identifiers.org/taxonomy:9606"),
    ("http://identifiers.org/taxonomy/9606", "https://identifiers.org/taxonomy:9606"),
    ("urn:miriam:uniprot:P03023", "https://identifiers.org/uniprot:P03023"),
    ("hmdb/HMDB0000122", "https://identifiers.org/hmdb:HMDB0000122"),
    (
        "doi/10.5281/zenodo.17091694",
        "https://identifiers.org/doi:10.5281/zenodo.17091694",
    ),
    (
        "https://identifiers.org/DOI:10.1016/j.jtbi.2004.04.039",
        "https://identifiers.org/doi:10.1016/j.jtbi.2004.04.039",
    ),
    # namespace embedded in the LUI: prefix is part of the term, unchanged
    ("GO:0005829", "https://identifiers.org/GO:0005829"),
    ("https://identifiers.org/go/GO:0005829", "https://identifiers.org/GO:0005829"),
    ("urn:miriam:chebi:CHEBI%3A33699", "https://identifiers.org/CHEBI:33699"),
    (
        "http://identifiers.org/biomodels.sbo/SBO:0000247",
        "https://identifiers.org/SBO:0000247",
    ),
    ("bto/BTO:0000089", "https://identifiers.org/BTO:0000089"),
    # no identifiers.org collection: resource is returned unchanged
    ("https://en.wikipedia.org/wiki/Cytosol", "https://en.wikipedia.org/wiki/Cytosol"),
    ("https://bioregistry.io/chebi:15996", "https://bioregistry.io/chebi:15996"),
]


@pytest.mark.parametrize("resource,expected", resource_normalized_data)
def test_resource_normalized(resource: str, expected: str) -> None:
    """Test normalization to identifiers.org compact identifiers."""
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource)
    assert a.resource_normalized == expected


resource_kept_data = [
    # collection which is not in the registry (see #81)
    ("http://identifiers.org/sabiork/1406", "https://identifiers.org/sabiork/1406"),
    ("urn:miriam:foo:bar", "https://identifiers.org/foo/bar"),
    ("foo/bar", "https://identifiers.org/foo/bar"),
    # collection which is not in the registry, term with a prefix of its own
    (
        "http://identifiers.org/unit/UO:0000040",
        "https://identifiers.org/unit/UO:0000040",
    ),
    # compact identifier of a prefix which is not in the registry
    ("https://identifiers.org/CMO:0000012", "https://identifiers.org/CMO:0000012"),
    ("CMO:0000012", "https://identifiers.org/CMO:0000012"),
    # term which does not match the pattern of its collection
    (
        "http://identifiers.org/chebi/000000035",
        "https://identifiers.org/chebi/000000035",
    ),
    ("taxonomy/abc", "https://identifiers.org/taxonomy:abc"),
    # prefix with a hyphen or an underscore
    ("urn:miriam:ec-code:1.1.1.1", "https://identifiers.org/ec-code:1.1.1.1"),
    (
        "https://identifiers.org/ec-code/1.1.1.1",
        "https://identifiers.org/ec-code:1.1.1.1",
    ),
    ("go_ref/GO_REF:0000041", "https://identifiers.org/GO_REF:0000041"),
    (
        "https://identifiers.org/GO_REF:0000041",
        "https://identifiers.org/GO_REF:0000041",
    ),
    # prefixes are case insensitive
    ("urn:miriam:CHEBI:CHEBI%3A33699", "https://identifiers.org/CHEBI:33699"),
    ("TAXONOMY/9606", "https://identifiers.org/taxonomy:9606"),
]


def assert_resource_kept(resource: str) -> None:
    """Assert that the normalized resource is a url with the same meaning."""
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource, validate=False)
    normalized = a.resource_normalized
    assert normalized
    assert normalized.startswith("https://")

    b = RDFAnnotation(qualifier=BQB.IS, resource=normalized, validate=False)
    assert (b.collection, b.term) == (a.collection, a.term)
    assert b.resource_normalized == normalized


@pytest.mark.parametrize("resource,expected", resource_kept_data)
def test_resource_normalized_keeps_resource(resource: str, expected: str) -> None:
    """Test that collection and term survive the normalization, see #81."""
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource, validate=False)
    assert a.resource_normalized == expected
    assert_resource_kept(resource)


@pytest.mark.parametrize(
    "resource", [resource for resource, _ in resource_normalized_data]
)
def test_resource_normalized_roundtrip(resource: str) -> None:
    """Test that the normalized resource parses to the same annotation."""
    assert_resource_kept(resource)


def test_resource_normalized_registry() -> None:
    """Test the normalization with the sample of every registry namespace."""
    from pymetadata.webservices.registry import get_registry

    for prefix, namespace in get_registry().ns_dict.items():
        sample_id = namespace.sampleId
        if not sample_id:
            continue
        for resource in [
            f"https://identifiers.org/{prefix}/{sample_id}",
            f"urn:miriam:{prefix}:{sample_id.replace(':', '%3A')}",
        ]:
            assert_resource_kept(resource)


xref_url_data = [
    # term without the embedded prefix of its collection
    ("chebi/33699", "chebiId=CHEBI:33699"),
    ("go/0005829", "id=GO:0005829"),
    # term with the embedded prefix
    ("CHEBI:33699", "chebiId=CHEBI:33699"),
    ("GO:0005829", "id=GO:0005829"),
]


@pytest.mark.parametrize("resource,expected", xref_url_data)
def test_rdf_annotation_data_url(
    resource: str, expected: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that the provider url contains the full term."""
    monkeypatch.setattr(RDFAnnotationData, "query_ols", lambda self: {})
    data = RDFAnnotationData(RDFAnnotation(qualifier=BQB.IS, resource=resource))
    assert data.url
    assert data.url.endswith(expected)


def test_rdf_annotation_data_xrefs_validate_each_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test that every cross reference is checked by its own url."""
    from pymetadata.webservices.registry import get_registry

    namespace = dataclasses.replace(get_registry().ns_dict["taxonomy"])
    valid, invalid = (
        dataclasses.replace(resource) for resource in (namespace.resources or [])[:2]
    )
    invalid.urlPattern = "no url {$id}"
    namespace.resources = [valid, invalid]
    monkeypatch.setitem(get_registry().ns_dict, "taxonomy", namespace)
    monkeypatch.setattr(RDFAnnotationData, "query_ols", lambda self: {})

    data = RDFAnnotationData(RDFAnnotation(qualifier=BQB.IS, resource="taxonomy/9606"))
    assert [xref.url for xref in data.xrefs] == [data.url]
    assert all(is_url(xref.url) for xref in data.xrefs)


parse_data = [
    # compact identifier with a `/` in the accession
    ("doi:10.1016/j.jtbi.2004.04.039", "doi", "10.1016/j.jtbi.2004.04.039"),
    ("DOI:10.1016/j.jtbi.2004.04.039", "doi", "10.1016/j.jtbi.2004.04.039"),
    # lowercase percent encoding in urns
    ("urn:miriam:chebi:CHEBI%3a33699", "chebi", "CHEBI:33699"),
    (
        "urn:miriam:doi:10.1016%2Fj.jtbi.2004.04.039",
        "doi",
        "10.1016/j.jtbi.2004.04.039",
    ),
    # scheme and host are case insensitive
    ("HTTPS://identifiers.org/taxonomy/9606", "taxonomy", "9606"),
    ("https://IDENTIFIERS.ORG/taxonomy/9606", "taxonomy", "9606"),
    ("HTTPS://bioregistry.io/chebi:15996", "chebi", "chebi:15996"),
    # query string, fragment and trailing slash are not part of the term
    ("https://identifiers.org/taxonomy/9606/", "taxonomy", "9606"),
    ("https://identifiers.org/taxonomy/9606?format=json", "taxonomy", "9606"),
    ("https://identifiers.org/taxonomy/9606#top", "taxonomy", "9606"),
    ("https://identifiers.org/CHEBI:33699/", "chebi", "CHEBI:33699"),
    ("https://identifiers.org/CHEBI:33699?x=1", "chebi", "CHEBI:33699"),
    ("https://bioregistry.io/chebi:15996/", "chebi", "chebi:15996"),
    ("https://bioregistry.io/chebi:15996?x=1", "chebi", "chebi:15996"),
    # percent-encoded `#` and `?` are part of the term
    ("https://identifiers.org/dev.ga4ghdos:abc%23def", "dev.ga4ghdos", "abc#def"),
]


@pytest.mark.parametrize("resource,collection,term", parse_data)
def test_rdf_annotation_parse(resource: str, collection: str, term: str) -> None:
    """Test parsing of resources into collection and term."""
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource, validate=False)
    assert (a.collection, a.term) == (collection, term)
    assert a.provider != ProviderType.NONE


none_provider_data = [
    # the dot of identifiers.org is not a wildcard
    "https://identifiersXorg/taxonomy/9606",
    # not an http(s) url
    "httpfoo",
    "ftp://identifiers.org/taxonomy/9606",
]


@pytest.mark.parametrize("resource", none_provider_data)
def test_rdf_annotation_not_identifiers_org(resource: str) -> None:
    """Test that only identifiers.org urls are parsed as identifiers.org."""
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource, validate=False)
    assert a.provider == ProviderType.NONE
    assert a.collection is None


invalid_term_data = [
    # unanchored registry patterns must match the whole term
    "gtr/123abc",
    "m4i/foo-bar",
    "taxonomy/9606abc",
]


@pytest.mark.parametrize("resource", invalid_term_data)
def test_check_miriam_term_full_match(resource: str) -> None:
    """Test that a term must match the registry pattern completely."""
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource, validate=False)
    assert a.provider == ProviderType.IDENTIFIERS_ORG
    assert not a.check_miriam_term()
    assert not a.validate()


def test_validate_unparseable_resource() -> None:
    """Test that a resource which is neither an identifier nor a url is invalid."""
    a = RDFAnnotation(qualifier=BQB.IS, resource="foo", validate=False)
    assert a.provider == ProviderType.NONE
    assert not a.validate()


def test_validate_url() -> None:
    """Test that an arbitrary url is valid."""
    a = RDFAnnotation(
        qualifier=BQB.IS, resource="https://en.wikipedia.org/wiki/Cytosol"
    )
    assert a.validate()


def test_replaced_collection_before_shortening(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test that legacy collections are replaced before the term is shortened."""
    monkeypatch.setitem(RDFAnnotation.replaced_collections, "obo.ncit", "ncit")
    a = RDFAnnotation(
        qualifier=BQB.IS, resource="urn:miriam:obo.ncit:ncit%3AC75913", validate=False
    )
    assert (a.collection, a.term) == ("ncit", "C75913")


def test_namespaces_from_dict_ignores_unknown_keys() -> None:
    """Test that a cached registry with additional keys can be loaded."""
    data = {
        "taxonomy": {
            "id": "1",
            "prefix": "taxonomy",
            "name": "Taxonomy",
            "pattern": r"^\d+$",
            "namespaceEmbeddedInLui": False,
            "description": "",
            "unknownKey": "value",
            "resources": [
                {
                    "id": 1,
                    "providerCode": "ncbi",
                    "name": "NCBI",
                    "urlPattern": "https://example.org/{$id}",
                    "mirId": None,
                    "description": "",
                    "official": True,
                    "sampleId": None,
                    "resourceHomeUrl": None,
                    "institution": {},
                    "location": {},
                    "deprecated": False,
                    "deprecationDate": "",
                    "unknownKey": "value",
                }
            ],
        }
    }
    ns_dict = Registry.namespaces_from_dict(data)
    namespace = ns_dict["taxonomy"]
    assert namespace.resources
    assert isinstance(namespace.resources[0], Resource)


def test_annotation_data_carries_the_ols_term(monkeypatch: pytest.MonkeyPatch) -> None:
    """The ontology, the IRI and the OLS page of the term end up in `to_dict`."""

    class Query:
        def query_ols(self, ontology: Any, term: Any) -> dict:
            return {"errors": [], "warnings": []}

        def process_response(self, term: dict) -> dict:
            return {
                "errors": [],
                "warnings": [],
                "label": "glycolytic process",
                "description": None,
                "synonyms": [],
                "xrefs": [],
                "ontology": "go",
                "iri": "http://purl.obolibrary.org/obo/GO_0006096",
                "ols_url": "https://www.ebi.ac.uk/ols4/ontologies/go/classes?iri=x",
            }

    monkeypatch.setattr("pymetadata.core.annotation.get_ols_query", lambda: Query())
    data = RDFAnnotationData(
        RDFAnnotation(qualifier=BQB.IS, resource="GO:0006096")
    ).to_dict()
    assert data["ontology"] == "go"
    assert data["iri"] == "http://purl.obolibrary.org/obo/GO_0006096"
    assert data["ols_url"] == "https://www.ebi.ac.uk/ols4/ontologies/go/classes?iri=x"
