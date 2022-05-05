"""Testing unichem."""
from pymetadata.unichem import UnichemQuery


def test_unichem() -> None:
    """Test unichem queries."""
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    _ = UnichemQuery.query_xrefs(inchikey=inchikey, cache=False)
    _ = UnichemQuery.query_xrefs(inchikey=inchikey, cache=True)
