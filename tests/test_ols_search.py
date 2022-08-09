"""Testing OLS Search."""
from typing import List

import pytest

from pymetadata.ontologies.ols_search import OLSSearch, SearchParameters, SearchResult


query_parameters: List[SearchParameters] = [
    SearchParameters(query="liver", ontology="bto"),
    SearchParameters(query="liver", ontology="bto", exact=True),
    SearchParameters(query="liver", ontology="bto", obsoletes=True),
]


@pytest.mark.parametrize("parameters", query_parameters)
def test_ols_search(parameters: SearchParameters) -> None:
    """Test OLS Search."""
    results: List[SearchResult] = OLSSearch().search(parameters)
    assert results
    assert len(results) >= 1


def test_ols_search_core() -> None:
    """Test OLS Search."""
    parameters = SearchParameters(
        query="liver",
        ontology="bto",
    )
    results: List[SearchResult] = OLSSearch().search(parameters)
    assert results
    assert len(results) > 2
    assert "liver" in results[0].label.lower()
