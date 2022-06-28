"""Testing OLS Search."""
from typing import List

from pymetadata.ontologies.ols_search import OLSSearch, OLSSearchResult


def test_ols_search_query() -> None:
    """Test OLS Search."""
    searchParam = {
        "query": "liver",
        "ontology": "bto",
        "obsoletes": "false",
        "exact": "false",
    }
    results: List[OLSSearchResult] = OLSSearch().ols_search(searchParam)
    assert results
    assert len(results) > 2
    assert "liver" in results[0].label.lower()
