# @pytest.mark.parametrize("chebi", ["CHEBI:2668", "CHEBI:138366", "CHEBI:9637", "CHEBI:155897"])
# def test_chebi(tmp_path, chebi):
#     cache_path = tmp_path / "cache"
#     keys = ["chebi", "formula", "charge", "mass", "inchikey"]
#
#     d = ChebiQuery.query(chebi=chebi, cache=False, cache_path=cache_path)
#     assert (cache_path / "chebi" / f"{chebi}.json").exists()
#     assert d
#     for key in keys:
#         assert key in d
#
#     d = ChebiQuery.query(chebi=chebi, cache=True, cache_path=cache_path)
#     for key in keys:
#         assert key in d
#     for key in keys:
#         assert key in d
