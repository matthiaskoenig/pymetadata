"""Lookup of ontology information from the ontology lookup service (OLS)."""
import logging
from dataclasses import dataclass, field
from pathlib import Path
from pprint import pprint
from typing import Dict, List

import requests

from pymetadata import CACHE_PATH, CACHE_USE
from pymetadata.pkdb_data.cache import read_json_cache, write_json_cache


logger = logging.getLogger(__name__)


@dataclass
class OLSOntology:
    """OLSOntology."""

    name: str
    iri_pattern: str = field(default=None)

    def __post_init__(self):
        """Fix IRI patterns."""
        if self.iri_pattern is None:
            self.iri_pattern = (
                f"http://purl.obolibrary.org/obo/{self.name.upper()}" + "_{$Id}"
            )


ONTOLOGIES = [
    # ontologies which are used in the project
    OLSOntology(name="bto"),
    OLSOntology(name="chebi"),
    OLSOntology(name="cmo"),
    OLSOntology(name="chmo"),
    OLSOntology(name="doid"),
    OLSOntology(name="efo", iri_pattern="http://www.ebi.ac.uk/efo/EFO_{$Id}"),
    OLSOntology(name="fix"),
    OLSOntology(name="fma"),
    OLSOntology(name="foodon"),
    OLSOntology(name="go"),
    OLSOntology(name="hp"),
    OLSOntology(name="nbo"),
    OLSOntology(name="obi"),
    OLSOntology(name="mondo"),
    OLSOntology(name="ncit"),
    OLSOntology(name="mp"),
    OLSOntology(name="oba"),
    OLSOntology(name="opmi"),
    OLSOntology(name="omit"),
    OLSOntology(
        name="sio", iri_pattern="http://semanticscience.org/resource/SIO_{$Id}"
    ),
    OLSOntology(name="vto"),
]


class OLSQuery:
    """Handling OLS queries."""

    url_term_query = "https://www.ebi.ac.uk/ols/api/ontologies/{}/terms/{}"

    def __init__(
        self,
        ontologies: List[OLSOntology],
        cache_path: Path = CACHE_PATH,
        cache: bool = CACHE_USE,
    ):
        self.ontologies = {
            ontology.name: ontology for ontology in ontologies
        }  # type: Dict[str, OLSOntology]
        self.cache_path = cache_path / "ols"
        self.cache = cache

        if not self.cache_path.exists():
            self.cache_path.mkdir(parents=True)

    def get_iri(self, ontology: str, term: str):
        """Get IRI information."""
        ols_ontology = self.ontologies.get(ontology, None)  # type: OLSOntology
        # remove prefix if existing
        if term.startswith(ontology.upper()):
            term = term.replace(f"{ontology.upper()}:", "")

        if ols_ontology is None:
            logger.warning(
                f"Ontology '{ontology}' is not registered, using default iri."
            )
            iri = f"http://purl.obolibrary.org/obo/{ontology.upper()}_{term}"
        else:
            iri = ols_ontology.iri_pattern.replace("{$Id}", term)

        return iri

    def query_ols(self, ontology: str, term: str) -> Dict:
        """Query the ontology lookup service."""
        if ontology in {
            "inchikey",
            "taxonomy",
            "pubchem.substance",
            "pubchem.compound",
            "wikidata",
            "uniprot",
        }:
            # exclude some annotation from query
            return None

        iri = self.get_iri(ontology=ontology, term=term)

        # urlencode iri for OLS
        urliri = iri.replace(":", "%253A")
        urliri = urliri.replace("/", "%252F")

        cache_path = self.cache_path / f"{urliri}.json"
        if self.cache:
            data = read_json_cache(cache_path=cache_path)

        if not data:
            url = self.url_term_query.format(ontology, urliri)
            logger.info(f"Query: {iri}")
            response = requests.get(url)
            data = response.json()
            if "error" in data:
                logger.warning(
                    f"Error in OLS query <{ontology}|{term}> at {iri}: {data}"
                )
                return None

            write_json_cache(data=data, cache_path=cache_path)

        return data

    def process_response(self, term: Dict):
        """Process the response dictionary."""
        if term is None:
            return None

        label = term.get("label", None)
        description = term.get("description", None)
        if description and isinstance(description, list):
            description = description[0]
        synonyms = term.get("obo_synonym", [])
        _ = term.get("obo_xref", [])

        return {
            "label": label,
            "description": description,
            "synonyms": synonyms,
            "xrefs": [],  # xrefs, FIXME: not using ols xrefs for now
        }
