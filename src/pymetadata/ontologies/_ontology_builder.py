"""Downloading ontologies and generating the term enums.

This module builds the enums of `pymetadata.ontologies`, it is internal tooling
for maintainers and not part of the public API: everything here can change
without notice, use the generated enums instead.

The enums are generated from the ontology releases: `update_ontology_files`
downloads the OWL files listed in `ontology_files`, `Ontology` reads them with
pronto and `create_ontology_enum` writes one python module per ontology, with
the terms as members and their label, definition, synonyms and deprecation as
data.

Running the module does all three steps for the packaged ontologies, i.e., SBO,
KISAO and PBPKO:

```bash
python -m pymetadata.ontologies._ontology_builder
```

`pronto` is an optional dependency, install it with
`pip install pymetadata[ontology]`. It is only needed to read the ontologies and
generate the modules, not to use the generated enums.

Adding an ontology means adding an `OntologyFile` to `ontology_files` and a
`create_ontology_enum` call with the id pattern of the ontology. The downloaded
OWL files are not part of the repository, and the generated modules should never
be edited by hand.
"""

import gzip
import importlib
import re
import shutil
import tempfile
import warnings
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING

import requests

from pymetadata import ENUM_DIR, RESOURCES_DIR, log
from pymetadata.ontologies.term import TermData

if TYPE_CHECKING:
    from pronto.ontology import Ontology as ProntoOntology
    from pronto.relationship import Relationship as ProntoRelationship
    from pronto.term import Term as ProntoTerm

logger = log.get_logger(__name__)

_ONTOLOGY_EXTRA_MSG = (
    "Reading ontologies requires the optional `ontology` dependencies. Install "
    "them with `pip install pymetadata[ontology]` or `uv sync --extra ontology`."
)


class OntologyFormat(str, Enum):
    """Serialization format of an ontology file."""

    OBO = "obo"
    OWL = "owl"


@dataclass
class OntologyFile:
    """An ontology which can be downloaded and turned into an enum.

    Attributes:
        id: uppercase ontology id, e.g., `SBO`
        name: name of the ontology
        format: format of the source file
        source: url the ontology is downloaded from
        bioportal: ontology is available on BioPortal
        ols: ontology is available on OLS
    """

    id: str
    name: str
    format: OntologyFormat
    source: str
    bioportal: bool
    ols: bool

    @property
    def path(self) -> Path:
        """Path of the local, gzipped copy of the ontology."""
        return (
            RESOURCES_DIR / "ontologies" / f"{self.id.lower()}.{self.format.value}.gz"
        )

    @property
    def filename(self) -> str:
        """Get the path of the local ontology copy as a string.

        Returns:
            Path of the gzipped ontology file.
        """
        return str(self.path)


_ontology_files: list[OntologyFile] = [
    OntologyFile(
        "BTO",
        name="The BRENDA Tissue Ontology (BTO)",
        format=OntologyFormat.OWL,
        source="http://purl.obolibrary.org/obo/bto.owl",
        bioportal=False,
        ols=True,
    ),
    OntologyFile(
        "CHEBI",
        name="Chemical Entities of Biological Interest Ontology",
        format=OntologyFormat.OWL,
        source="http://purl.obolibrary.org/obo/chebi.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "FMA",
        name="Foundational Model of Anatomy",
        format=OntologyFormat.OWL,
        source="http://purl.obolibrary.org/obo/fma.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "ECO",
        name="Evidence & Conclusion Ontology (ECO)",
        format=OntologyFormat.OWL,
        source="http://purl.obolibrary.org/obo/eco.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "GO",
        name="Gene Ontology",
        format=OntologyFormat.OWL,
        source="http://purl.obolibrary.org/obo/go/extensions/go-plus.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "KISAO",
        name="Kinetic Simulation Algorithm Ontology",
        format=OntologyFormat.OWL,
        # source="https://raw.githubusercontent.com/SED-ML/KiSAO/deploy/kisao.owl",
        source="https://raw.githubusercontent.com/SED-ML/KiSAO/dev/kisao.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "SBO",
        name="Systems Biology Ontology",
        format=OntologyFormat.OWL,
        source="https://raw.githubusercontent.com/EBI-BioModels/SBO/master/SBO_OWL.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "NCIT",
        name="National Cancer Institute Thesaurus",
        format=OntologyFormat.OWL,
        source="http://purl.obolibrary.org/obo/ncit.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "PBPKO",
        name="PBPK (Physiologically Based Pharmacokinetic) Ontology",
        format=OntologyFormat.OWL,
        source="http://purl.obolibrary.org/obo/pbpko.owl",
        bioportal=True,
        ols=True,
    ),
]


ontology_files: dict[str, OntologyFile] = {
    ontology.id: ontology for ontology in _ontology_files
}


def update_ontology_file(ofile: OntologyFile) -> None:
    """Download one ontology and store it gzipped in the resources.

    Args:
        ofile: ontology to download
    """
    oid = ofile.id

    logger.info("Update ontology: `%s`", oid)

    with tempfile.TemporaryDirectory() as tmp_dir:
        # download in tmp location
        owl_path = Path(tmp_dir) / f"{oid.lower()}.owl"
        url = ofile.source
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(owl_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # only store gzip version
        with open(owl_path, "rb") as f_in:
            gzip_path = RESOURCES_DIR / "ontologies" / f"{oid.lower()}.owl.gz"
            with gzip.open(gzip_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)


def update_ontology_files(ontology_ids: list[str] | None = None) -> None:
    """Download the current release of ontologies.

    Args:
        ontology_ids: ids of the ontologies to download, all of
            `ontology_files` if none are given
    """
    ids = ontology_ids if ontology_ids is not None else list(ontology_files)
    with ThreadPoolExecutor(max_workers=4) as pool:
        for oid in ids:
            pool.submit(update_ontology_file, ontology_files[oid])


class Ontology:
    """An ontology read from its local OWL file with pronto.

    Attributes:
        ontology_id: id of the ontology, e.g., `SBO`
    """

    def __init__(self, ontology_id: str):
        """Read the ontology from the local file.

        Args:
            ontology_id: id of an ontology in `ontology_files`, e.g., `SBO`
        """
        try:
            import pronto
            import pronto.utils.warnings
        except ImportError as err:  # pragma: no cover - depends on the install
            raise ImportError(_ONTOLOGY_EXTRA_MSG) from err

        ontology_file = ontology_files[ontology_id]
        logger.info("Read ontology: `%s`", ontology_id)
        self.ontology_id = ontology_id

        # read ontology with pronto
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", pronto.utils.warnings.SyntaxWarning)
            warnings.simplefilter("ignore", pronto.utils.warnings.NotImplementedWarning)
            # instance state; a class attribute would be overwritten by the
            # next ontology which is read
            self._ontology: ProntoOntology | None = pronto.Ontology(
                ontology_file.filename
            )

    def get_pronto_ontology(self) -> "ProntoOntology | None":
        """Get the underlying pronto ontology.

        Returns:
            The pronto ontology, or None if no ontology was read.
        """
        return self._ontology


#: annotation properties which carry the definition of a term; the ontologies
#: use different ones, e.g., SBO the `rdfs:comment` and KISAO `skos:definition`
_DEFINITION_PROPERTIES: tuple[str, ...] = (
    "http://www.w3.org/2004/02/skos/core#definition",
    "http://purl.obolibrary.org/obo/IAO_0000115",
    "http://www.w3.org/2000/01/rdf-schema#comment",
)

#: annotation properties which carry alternative names of a term
_SYNONYM_PROPERTIES: tuple[str, ...] = (
    "http://www.w3.org/2004/02/skos/core#altLabel",
    "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym",
    "http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym",
)


def _annotation_literals(
    pronto_term: "ProntoTerm | ProntoRelationship", properties: tuple[str, ...]
) -> list[str]:
    """Collect the literals of the given annotation properties of a term.

    Args:
        pronto_term: term or relationship read with pronto
        properties: annotation properties to collect, e.g., `skos:definition`

    Returns:
        The literals in the order of the annotations.
    """
    literals: list[str] = []
    for annotation in pronto_term.annotations:
        literal = getattr(annotation, "literal", None)
        if literal and str(annotation.property) in properties:
            literals.append(str(literal))
    return literals


def _term_data(pronto_term: "ProntoTerm | ProntoRelationship") -> TermData:
    """Collect the information of a term of the ontology.

    The definition is taken from the definition of the term, its comment or the
    annotations, whichever the ontology provides.

    Args:
        pronto_term: term or relationship read with pronto

    Returns:
        The label, definition, synonyms and deprecation of the term.
    """
    definition: str | None = None
    for candidate in (
        pronto_term.definition,
        pronto_term.comment,
        *_annotation_literals(pronto_term, _DEFINITION_PROPERTIES),
    ):
        if candidate:
            definition = " ".join(str(candidate).split())
            break

    label = str(pronto_term.name)
    synonyms = tuple(
        sorted(
            {
                synonym
                for synonym in (
                    *(s.description for s in pronto_term.synonyms),
                    *_annotation_literals(pronto_term, _SYNONYM_PROPERTIES),
                )
                if synonym and synonym != label
            }
        )
    )
    return (label, definition, synonyms, bool(pronto_term.obsolete))


def _render_module(ontology_id: str, pattern: str, terms: dict[str, TermData]) -> str:
    r"""Render the python module of an ontology.

    Args:
        ontology_id: id of the ontology, e.g., `SBO`
        pattern: regular expression the term ids match, e.g., `^SBO_\d{7}$`
        terms: information of every term, keyed by id

    Returns:
        The source of the module.
    """
    members: list[str] = []
    data: list[str] = []
    var_names: set[str] = set()

    for term_id, term_data in terms.items():
        label = term_data[0]
        members.append(f"    # {label}")
        members.append(f'    {term_id} = "{term_id}"')

        var_name = re.sub(r"\W|^(?=\d)", "_", label).upper()
        if var_name != term_id and var_name not in var_names:
            var_names.add(var_name)
            members.append(f'    {var_name} = "{term_id}"')
        members.append("")

        data.append(f"    {term_id!r}: {term_data!r},")

    return "\n".join(
        [
            f'"""{ontology_id} ontology.',
            "",
            "Generated from the ontology release by",
            "`pymetadata.ontologies._ontology_builder`, do not edit.",
            '"""',
            "",
            "from pymetadata.ontologies.term import OntologyEnum, TermData",
            "",
            f'pattern = r"{pattern}"',
            "",
            "",
            f"class {ontology_id}(OntologyEnum):",
            f'    """{ontology_id} ontology."""',
            "",
            *members,
            f"{ontology_id}Type = str | {ontology_id}",
            "",
            "#: information of every term, assigned to the enum below",
            "_terms: dict[str, TermData] = {",
            *data,
            "}",
            "",
            f"{ontology_id}._terms = _terms",
            "",
            "__all__ = [",
            f'    "{ontology_id}",',
            f'    "{ontology_id}Type",',
            "]",
            "",
        ]
    )


def create_ontology_enum(ontology_id: str, pattern: str) -> None:
    r"""Generate the python enum module for an ontology.

    The module is written to `ENUM_DIR`, i.e.,
    `pymetadata/ontologies/<ontology_id>.py`; run `ruff format` on it
    afterwards, the rendered output is not formatted.

    Args:
        ontology_id: id of an ontology in `ontology_files`, e.g., `SBO`
        pattern: regular expression the term ids match, e.g., `^SBO_\d{7}$`

    Raises:
        ValueError: if the ontology could not be read
    """
    logger.info("Create enum: `%s`", ontology_id)

    terms: dict[str, TermData] = {}
    ontology: Ontology = Ontology(ontology_id=ontology_id)
    pronto_ontology = ontology.get_pronto_ontology()
    if not pronto_ontology:
        raise ValueError(f"No Pronto Ontology for `{ontology_id}`")

    pronto_term: ProntoTerm | ProntoRelationship
    for term_id in pronto_ontology:
        try:
            pronto_term = pronto_ontology.get_relationship(term_id)
        except KeyError:
            try:
                pronto_term = pronto_ontology.get_term(term_id)
            except KeyError:
                # neither relationship nor term; without `continue` the entry of
                # the previous iteration would be processed a second time
                logger.warning("Term could not be resolved: `%s`", term_id)
                continue

        if not isinstance(pronto_term.name, str):
            logger.warning("Pronto name is none: `%s`", pronto_term)
            continue

        # fix the ids
        term_id = pronto_term.id
        if ontology_id == "KISAO":
            term_id = term_id.replace("http://www.biomodels.net/kisao/KISAO#", "")
        if ontology_id == "SBO":
            term_id = term_id.replace("http://biomodels.net/SBO/", "")
        term_id = term_id.replace(":", "_")

        terms[term_id] = _term_data(pronto_term)

    terms = {term_id: terms[term_id] for term_id in sorted(terms)}

    path_module = ENUM_DIR / f"{ontology_id.lower()}.py"
    logger.info("Write module: `%s`", path_module)
    with open(path_module, "w") as f_py:
        f_py.write(_render_module(ontology_id, pattern, terms))


def try_ontology_import(ontology_id: str) -> None:
    """Check that the generated module for an ontology can be imported.

    Args:
        ontology_id: id of an ontology in `ontology_files`, e.g., `SBO`

    Raises:
        ModuleNotFoundError: if the module was not generated
    """
    # try to import
    importlib.import_module(f"pymetadata.ontologies.{ontology_id.lower()}")


if __name__ == "__main__":
    #: the packaged ontologies with the pattern their term ids match
    ontology_patterns: dict[str, str] = {
        "SBO": r"^SBO_\d{7}$",
        "KISAO": r"^KISAO_\d{7}$",
        "PBPKO": r"^PBPKO_\d{5}$",
    }

    update_ontology_files(list(ontology_patterns))

    for oid, id_pattern in ontology_patterns.items():
        create_ontology_enum(oid, id_pattern)

    for oid in ontology_patterns:
        try_ontology_import(oid)
