"""Lookup of ontology terms in the Ontology Lookup Service (OLS).

OLS resolves an ontology term to its label, description, synonyms and cross
references. `RDFAnnotationData` uses it to fill in what an annotation actually
refers to.

```python
from pymetadata.ontologies.ols import ONTOLOGIES, OLSQuery

query = OLSQuery(ontologies=ONTOLOGIES)
info = query.query_ols(ontology="chebi", term="CHEBI:33699")
print(query.process_response(info)["label"])
```

`ONTOLOGIES` lists the ontologies used in most projects together with the IRI
pattern needed to build the term IRI OLS expects.

See <https://www.ebi.ac.uk/ols4>.
"""

import contextlib
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pymetadata
from pymetadata import log
from pymetadata.cache import read_json_cache, write_json_cache
from pymetadata.identifiers.registry import get_registry
from pymetadata.webservice import get_session

logger = log.get_logger(__name__)


@dataclass
class OLSOntology:
    """An ontology available in OLS.

    Attributes:
        name: lowercase ontology id, e.g., `chebi`
        iri_pattern: pattern of the term IRI with the placeholder `{$Id}`,
            defaults to the OBO purl of the ontology
    """

    name: str
    iri_pattern: str | None = field(default=None)

    def __post_init__(self) -> None:
        """Set the default OBO purl pattern if no pattern was given."""
        if self.iri_pattern is None:
            self.iri_pattern = (
                f"http://purl.obolibrary.org/obo/{self.name.upper()}" + "_{$Id}"
            )


ONTOLOGIES = [
    # ontologies which are used in most projects
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
    """Queries against the Ontology Lookup Service.

    Responses can be cached on disk, see `pymetadata.CACHE_USE`.

    Attributes:
        ontologies: the queryable ontologies by name
        cache_path: directory of the cached responses
        cache: whether responses are cached
    """

    url_term_query = "https://www.ebi.ac.uk/ols4/api/ontologies/{}/terms/{}"

    def __init__(
        self,
        ontologies: list[OLSOntology],
        cache_path: Path | None = None,
        cache: bool | None = None,
    ):
        """Initialize the query.

        Args:
            ontologies: ontologies which can be queried, e.g., `ONTOLOGIES`
            cache_path: directory for cached responses, defaults to
                `pymetadata.CACHE_PATH`
            cache: cache responses, defaults to `pymetadata.CACHE_USE`
        """
        self.ontologies: dict[str, OLSOntology] = {
            ontology.name: ontology for ontology in ontologies
        }
        if not cache_path:
            cache_path = pymetadata.CACHE_PATH
        if not cache:
            cache = pymetadata.CACHE_USE

        self.cache_path = cache_path / "ols"
        self.cache = cache

        if cache and not self.cache_path.exists():
            self.cache_path.mkdir(parents=True)

    def get_iri(self, ontology: str, term: str) -> str:
        """Build the term IRI which OLS expects.

        Args:
            ontology: ontology id, e.g., `chebi`
            term: term of the ontology, e.g., `CHEBI:33699`

        Returns:
            The IRI of the term, or an empty string for an unknown ontology.
        """
        ols_ontology: OLSOntology | None = self.ontologies.get(ontology, None)
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

    def query_ols(self, ontology: str | None, term: str | None) -> dict:
        """Query OLS for a single term.

        Args:
            ontology: ontology id, e.g., `chebi`
            term: term of the ontology, e.g., `CHEBI:33699`

        Returns:
            The OLS response, with `errors` and `warnings` describing problems
            with the query.
        """
        if not ontology:
            return {"errors": [], "warnings": ["No collection."]}
        if not term:
            return {"errors": [], "warnings": [f"No term: '{ontology}'"]}

        namespace = get_registry().ns_dict.get(ontology)
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
        cache_path = self.cache_path / f"{urliri}.json"
        data: dict[str, Any] = {}
        if self.cache:
            with contextlib.suppress(OSError):
                # cache does not exist
                data = read_json_cache(cache_path=cache_path)

        if not data:
            url = self.url_term_query.format(ontology, urliri)
            logger.info(f"Query: {url}")
            response = get_session().get(url)

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
                    return {
                        "errors": [error_msg],
                        "warnings": [],
                    }
                data["errors"] = []
                data["warnings"] = []
                if self.cache:
                    write_json_cache(data=data, cache_path=cache_path)

        return data

    def process_response(self, term: dict) -> dict[str, Any]:
        """Reduce an OLS response to the information used for annotations.

        Args:
            term: OLS response from `query_ols`

        Returns:
            Dictionary with `label`, `description`, `synonyms` and `xrefs`.
        """
        data = {
            "errors": term["errors"],
            "warnings": term["warnings"],
        }

        label = term.get("label")
        description = term.get("description")
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
