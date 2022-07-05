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
from typing import Dict, List, Optional

import requests

from pymetadata.log import get_logger
import re
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
import numpy as np
# FIXME: add dependency

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

    @classmethod
    def rank(cls, query: str, results: List[SearchResult]) -> List[float]:
        """Rank given list of results.

        The default search is across all textual fields in the ontology, but results
        are ranked towards hits in labels, then synonyms, then definitions,
        then annotations.

        label^5 synonym^3 description short_form^2 obo_id^2 annotations
        logical_description iri

        see also https://solr.apache.org/guide/6_6/the-dismax-query-parser.html#TheDisMaxQueryParser-Theqf_QueryFields_Parameter

        - label
        - description
        - short_form
        - obo_id
        - iri

        missing (probably secondary query needed)
        - synonym
        - annotations
        - logical descriptions

        Rank results based on query; perfect match is 1.0, worst case 0.0.
        """
        scores = []
        for result in search_results:
            score = cls.match_fraction(query, result.label) * 5 \
                    + cls.match_fraction(query, " ".join(result.descriptions)) \
                    + cls.match_fraction(query, result.short_form) * 2 \
                    + cls.match_fraction(query, result.obo_id) * 2 \
                    + cls.match_fraction(query, result.iri)
            # normalization with maximum score
            score = score/11.0
            scores.append(score)

        return scores

    @staticmethod
    def match_fraction(query, text) -> float:
        """Maximal contribution of query string to text."""
        if not query:
            return 0.0
        if not text:
            return 0.0

        query_items = SearchResult.word_list(query)
        text_items = SearchResult.word_list(text)

        # perform the matching
        n_query = len(query_items)
        n_text = len(text_items)
        scores = []
        for q in query_items:
            count = 0
            for word in text_items:
                if q in word:
                    count += 1
            scores.append(count/n_text)

        score = np.sum(np.array(scores))
        print("---")
        print(query_items)
        print(text_items)
        print(scores)
        print(score)

        return score


    @staticmethod
    def word_list(text: str) -> List[str]:
        """Create clean word list from text."""
        # normalization/toxenization
        # see https://stackabuse.com/text-classification-with-python-and-scikit-learn/

        # https://www.nltk.org/
        # FIXME: add nltk dependency
        from nltk.stem import WordNetLemmatizer
        stemmer = WordNetLemmatizer()

        # Remove all the special characters
        text = re.sub(r'\W', ' ', str(text))

        # remove all single characters
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)

        # Remove single characters from the start
        text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)

        # Substituting multiple spaces with single space
        text = re.sub(r'\s+', ' ', text, flags=re.I)

        # Removing prefixed 'b'
        text = re.sub(r'^b\s+', '', text)

        # Converting to Lowercase
        text = text.lower()

        # Lemmatization
        text = text.split()

        return [stemmer.lemmatize(word) for word in text]




@dataclass
class SearchParameters:
    """Class for search parameters.

    TODO:
    """

    query: str
    ontology: Optional[str] = None
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
            f"ontology={parameters.ontology if parameters.ontology else ''}",
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
                descriptions=item.get("description", []),
                ontology_name=item["ontology_name"],
                ontology_prefix=item["ontology_prefix"],
            )
            results.append(result)

        return results


if __name__ == "__main__":
    query = "liver organ"
    parameters = SearchParameters(
        query=query,
    )
    print(parameters)
    search_results: List[SearchResult] = OLSSearch().search(parameters)
    for item in search_results:
        print(item)

    # rank the results
    ranking = SearchResult.rank(query=query, results=search_results)
    print(ranking)
