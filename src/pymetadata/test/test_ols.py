from pymetadata.core.annotation import BQB, RDFAnnotation, RDFAnnotationData


def test_ols_query() -> None:
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
