from pymetadata.unichem import UnichemQuery


def test_unichem() -> None:
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    results = UnichemQuery.query_xrefs(inchikey=inchikey, cache=False)
    results = UnichemQuery.query_xrefs(inchikey=inchikey, cache=True)
