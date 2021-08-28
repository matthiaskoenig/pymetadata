from pymetadata.pkdb_data.annotation import BQB, Annotation
from pymetadata.pkdb_data.ols import ONTOLOGIES, OLSQuery


def test_ols_query():
    data = [
        (BQB.IS, "chebi/CHEBI:37924"),
        (BQB.IS, "ncit/C66872"),
    ]
    annotations = [Annotation(relation=d[0], resource=d[1]) for d in data]

    for a in annotations:
        info = a.query_ols()
        assert info
        for key in ["description", "label", "synonyms", "xrefs"]:
            assert key in info
