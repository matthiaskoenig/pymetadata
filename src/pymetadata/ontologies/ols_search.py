"""This module searches annotation terms from the ontology lookup service.

See https://www.ebi.ac.uk/ols/docs/api -> Search for documentation.

**Milestone 2.2 Develop backend functionality for the annotation search**
The frontend annotation query will be send to the python backend which will query the
various existing web services (Ontology Lookup Service, Bio Ontologies, AnnotateDB)
to fetch the ontology terms. Results will be processed/cached/ranked and returned to
the frontend as ranked results via the JSON annotation format.

TODO: Create a class which allows to search OLS via the REST API.
see for instance
https://www.ebi.ac.uk/ols/api/search?q=glucose


Do something similar for
https://data.bioontology.org/documentation -> Term search

-> (term_id, ontology, label, descriptions);

object.id, object.name, object.meta_id


TODO: Code review
- create test case & test code
- add type annotatations
- check that test are passing, i.e. run `./fcode.sh` for code formating and `tox -e flake8` and `tox -e mypy`
- process_response should be probably a class method, not member
- better naming of your data structure. This is not an OLSOntology, but a OLSSearchEntry
- create a data structure for a set of results, i.e. something which manages multiple results
"""

from typing import Dict, List, Optional

import requests

from pymetadata.log import get_logger


logger = get_logger(__file__)


class OLSSearchResult:
    """Class for storing OLS search results."""

    def __init__(
        self,
        key: str,
        iri: str,
        short_form: str,
        obo_id: str,
        label: str,
        descriptions: List[str],
        ontology_name: str,
        onotology_prefix: str,
    ):
        """Initialize OLSSearchResult."""
        self.key = key
        self.iri = iri
        self.short_form = short_form
        self.obo_id = obo_id
        self.label = label
        self.descriptions: List[str] = descriptions
        self.ontology_name = ontology_name
        self.ontology_prefix = onotology_prefix


class OLSSearch:
    """Class to search the ontology lookup service (OLS)."""

    @classmethod
    def ols_search(cls, term: str, ontology: str = "") -> List[OLSSearchResult]:
        """Perform OLS search with given term and ontology.

        Raises requests.HTTPError.
        """
        query = (
            "https://www.ebi.ac.uk/ols/api/search?q=" + term + "&ontology=" + ontology
        )
        try:
            response: requests.Response = requests.get(query)
        except requests.HTTPError as err:
            logger.error(err)
            raise err
        return cls.process_response(response)

    @staticmethod
    def process_response(response: requests.Response) -> List[OLSSearchResult]:
        """Parse response."""
        json: Dict = response.json()
        results: List = []

        item: Dict
        for item in json["response"]["docs"]:
            logger.debug(item)
            result = OLSSearchResult(
                key=item["id"],
                iri=item["iri"],
                short_form=item["short_form"],
                obo_id=item["obo_id"],
                label=item.get("label", ""),
                descriptions=item.get("descriptions", []),
                ontology_name=item["ontology_name"],
                onotology_prefix=item["ontology_prefix"],
            )
            results.append(result)

        return results


if __name__ == "__main__":
    OLSSearch().ols_search(term="liver")
