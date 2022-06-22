from typing import List

from pymetadata.ontologies.ols_search import OLSSearch, OLSSearchResult


def test_liver_query():
    results: List[OLSSearchResult] = OLSSearch().ols_search(term="liver")
    assert results
    assert len(results) > 2
    assert "liver" in results[0].label.lower()
