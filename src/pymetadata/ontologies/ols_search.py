"""This module searches annotation terms from the Ontology Lookup Service (OLS).

See https://www.ebi.ac.uk/ols/docs/api -> Search for documentation.
https://www.ebi.ac.uk/ols/api/search?q=glucose

**Milestone 2.2 Develop backend functionality for the annotation search**
The frontend annotation query will be send to the python backend which will query the
various existing web services (Ontology Lookup Service, Bio Ontologies, AnnotateDB)
to fetch the ontology terms. Results will be processed/cached/ranked and returned to
the frontend as ranked results via the JSON annotation format.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List


import requests

from pymetadata.log import get_logger


logger = get_logger(__file__)


@dataclass
class SearchResult:
    """Class for storing OLS search results."""

    key: str
    iri: str
    short_form: str
    obo_id: str
    label: str
    descriptions: List[str]
    ontology_name: str
    ontology_prefix: str

    @staticmethod
    def rank(query: str, results: List[SearchResult]) -> List[float]:
        """Rank given list of results.

        TODO: rank results based on query; perfect match is 1.0, worst case 0.0.
        Use label, descriptions. ....

        TODO: do research on scoring functions/libraries
        """
        raise NotImplementedError



@dataclass
class SearchParameters:
    """Class for search parameters.

    TODO:
    """

    query: str
    ontology: str
    obsoletes: bool = False
    exact: bool = False


class OLSSearch:
    """Class to search the ontology lookup service (OLS)."""

    @classmethod
    def search(cls, parameters: SearchParameters) -> List[SearchResult]:
        """Perform OLS search with given term and ontology.

        Raises requests.HTTPError.
        """
        # create query
        query_parts = [
            f"https://www.ebi.ac.uk/ols/api/search?q={parameters.query}",
            f"ontology={parameters.ontology}",
            f"obsoletes={'true' if parameters.obsoletes else 'false'}",
            f"exact={'true' if parameters.exact else 'false'}",
        ]
        query: str = "&".join(query_parts)
        print(query)

        # perform query
        try:
            response: requests.Response = requests.get(query)
        except requests.HTTPError as err:
            logger.error(err)
            raise err
        return cls._process_response(response)

    @staticmethod
    def _process_response(response: requests.Response) -> List[SearchResult]:
        """Parse response."""
        json: Dict = response.json()
        results: List = []

        item: Dict
        for item in json["response"]["docs"]:
            logger.debug(item)
            result = SearchResult(
                key=item["id"],
                iri=item["iri"],
                short_form=item["short_form"],
                obo_id=item["obo_id"],
                label=item.get("label", ""),
                descriptions=item.get("descriptions", []),
                ontology_name=item["ontology_name"],
                ontology_prefix=item["ontology_prefix"],
            )
            results.append(result)

        return results


if __name__ == "__main__":
    parameters = SearchParameters(
        query="liver",
        ontology="bto",
    )
    print(parameters)
    annotation = OLSSearch().search(parameters)
    for item in annotation:
        print(item)
