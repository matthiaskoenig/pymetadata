"""Lookup of ontology information from the ontology lookup service (OLS)."""
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

from pymetadata import CACHE_PATH, CACHE_USE, log
from pymetadata.cache import read_json_cache, write_json_cache
from pymetadata.identifiers.registry import Registry


registry = Registry()
logger = log.get_logger(__name__)


@dataclass
class OLSOntology:
    """OLSOntology."""

    name: str
    iri_pattern: Optional[str] = field(default=None)

    def __post_init__(self) -> None:
        """Fix IRI patterns."""
        if self.iri_pattern is None:
            self.iri_pattern = (
                f"http://purl.obolibrary.org/obo/{self.name.upper()}" + "_{$Id}"
            )


ONTOLOGIES = [
    # ontologies which are used in the project
    OLSOntology(name="sbo", iri_pattern="http://biomodels.net/SBO/SBO_{$Id}"),
    OLSOntology(
        name="ncbitaxon", iri_pattern="http://purl.obolibrary.org/obo/NCBITaxon_{$Id}"
    ),
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

    def get_iri(self, ontology: str, term: str) -> str:
        """Get IRI information."""
        ols_ontology: Optional[OLSOntology] = self.ontologies.get(ontology, None)
        # remove prefix if existing
        if term.startswith(ontology.upper()):
            term = term.replace(f"{ontology.upper()}:", "")

        if ols_ontology is None:
            logger.warning(
                f"Ontology '{ontology}' is not registered, using default iri."
            )
            iri = f"http://purl.obolibrary.org/obo/{ontology.upper()}_{term}"
        else:
            if not ols_ontology.iri_pattern:
                raise ValueError(f"No iri pattern for `{ols_ontology}")
            iri = ols_ontology.iri_pattern.replace("{$Id}", term)

        return iri

    def query_ols(self, ontology: Optional[str], term: Optional[str]) -> Dict:
        """Query the ontology lookup service."""
        if not ontology:
            return {"errors": [], "warnings": ["No collection."]}
        if not term:
            return {"errors": [], "warnings": [f"No term: '{ontology}'"]}

        namespace = registry.ns_dict.get(ontology)
        ols_pattern = None
        if namespace and namespace.resources:
            for ns_resource in namespace.resources:
                if ns_resource.providerCode == "ols":
                    ols_pattern = ns_resource.urlPattern
                    break

        if not ols_pattern:
            return {
                "errors": [],
                "warnings": [f"'{ontology}' is not on OLS."],
            }

        if ontology == "taxonomy":
            ontology = "ncbitaxon"

        iri = self.get_iri(ontology=ontology, term=term)

        # double urlencode iri for OLS
        urliri = urllib.parse.quote(iri, safe="")
        urliri = urllib.parse.quote(urliri, safe="")
        # urliri = iri.replace(":", "%253A")
        # urliri = urliri.replace("/", "%252F")

        # term_id = term.split(":")[-1]
        # url = ols_pattern.replace('{$id}', term_id)
        cache_path = self.cache_path / f"{urliri}.json"
        if self.cache:
            data = read_json_cache(cache_path=cache_path)
        else:
            data = {}

        if not data:
            url = self.url_term_query.format(ontology, urliri)
            logger.warning(f"Query: {url}")
            response = requests.get(url)

            if response.status_code != 200:
                data = {
                    "errors": [f"{response.status_code} response for: '{url}'"],
                    "warnings": [],
                }
            else:
                # print(response.text)
                data = response.json()
                if not data or "error" in data:
                    error_msg = (
                        f"Error in OLS query <{ontology}|{term}> at {url}: {data}"
                    )
                    logger.error(error_msg)
                    data = {
                        "errors": [error_msg],
                        "warnings": [],
                    }
                    return data
                else:
                    data["errors"] = []
                    data["warnings"] = []
                    write_json_cache(data=data, cache_path=cache_path)  # type: ignore

        return data

    def process_response(self, term: Dict) -> Dict[str, Any]:
        """Process the response dictionary."""
        data = {
            "errors": term["errors"],
            "warnings": term["warnings"],
        }

        label = term.get("label", None)
        description = term.get("description", None)
        # fallback description
        if description is None:
            annotation = term.get("annotation")
            if annotation:
                definition = annotation.get("definition")
                if definition:
                    description = definition[0]

        if description and isinstance(description, list):
            description = description[0]
        synonyms = term.get("obo_synonym", [])
        xrefs = term.get("obo_xref", [])

        return {
            **data,
            "label": label,
            "description": description,
            "synonyms": synonyms,
            "xrefs": xrefs,
        }
