"""Testing OLS."""

from pymetadata.core.annotation import BQB, RDFAnnotation, RDFAnnotationData


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
