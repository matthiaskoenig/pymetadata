"""Hardcoded ontologies."""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Tuple
import pronto
import tempfile
import gzip
import shutil
import importlib
import requests
import logging
import re
from pronto.term import Term as ProntoTerm
from pronto.ontology import Ontology as ProntoOntology
from pathlib import Path
import rich
from jinja2 import Template
import warnings
from concurrent.futures import ThreadPoolExecutor

from pymetadata.log import *
from pymetadata import RESOURCES_DIR, ENUM_DIR


logger = logging.getLogger(__name__)
console = Console()


class OntologyFormat(str, Enum):
    OBO = 'obo'
    OWL = 'owl'

@dataclass
class OntologyFile:
    id: str
    name: str
    format: OntologyFormat
    source: str
    bioportal: bool
    ols: bool

    @property
    def path(self) -> Path:
        """Path of ontology file."""
        return RESOURCES_DIR / "ontologies" / f"{self.id.lower()}.{self.format}.gz"

    @property
    def filename(self) -> str:
        """Filename of ontology file.

        :return: ontolgoy filename
        :rtype: str
        """
        data = str(self.path)
        print(data)
        return data
    
    @property
    def bioportal_url(self) -> str:
        return f"https://bioportal.bioontology.org/ontologies/{self.id}"
    

_ontology_files: List[OntologyFile] = [
    OntologyFile(
        "BTO", 
        name="The BRENDA Tissue Ontology (BTO)", 
        format=OntologyFormat.OWL,
        source="https://www.ebi.ac.uk/ols/ontologies/bto/download",
        bioportal=False,
        ols=True,
    ),
    OntologyFile(
        "CHEBI", 
        name="Chemical Entities of Biological Interest Ontology", 
        format=OntologyFormat.OWL,
        source="https://www.ebi.ac.uk/ols/ontologies/chebi/download",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "FMA", 
        name="Foundational Model of Anatomy", 
        format=OntologyFormat.OWL,
        source="https://www.ebi.ac.uk/ols/ontologies/fma/download",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "ECO", 
        name="Evidence & Conclusion Ontology (ECO)", 
        format=OntologyFormat.OWL,
        source="https://www.ebi.ac.uk/ols/ontologies/eco/download",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "GO", 
        name="Gene Ontology", 
        format=OntologyFormat.OWL,
        source="https://www.ebi.ac.uk/ols/ontologies/go/download",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "KISAO", 
        name="Kinetic Simulation Algorithm Ontology", 
        format=OntologyFormat.OWL,
        source="https://raw.githubusercontent.com/SED-ML/KiSAO/deploy/kisao.owl",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "SBO", 
        name="Systems Biology Ontology", 
        format=OntologyFormat.OWL,
        source="https://www.ebi.ac.uk/ols/ontologies/sbo/download",
        bioportal=True,
        ols=True,
    ),
    OntologyFile(
        "NCIT", 
        name="National Cancer Institute Thesaurus", 
        format=OntologyFormat.OWL,
        source="https://www.ebi.ac.uk/ols/ontologies/ncit/download",
        bioportal=True,
        ols=True,
    ),
    #     OntologyFile(
    #     "NCBITAXON", 
    #     name="NCBI organismal classification", 
    #     format=OntologyFormat.OWL,
    #     source="https://www.ebi.ac.uk/ols/ontologies/ncbitaxon/download",
    #     bioportal=False,
    #     ols=True,
    # ),
]


ontology_files: Dict[str, OntologyFile] = {
    ontology.id: ontology for ontology in _ontology_files
}


def update_ontology_file(ofile: OntologyFile) -> None:
    """Downloads latest versions of ontologies."""
    
    oid = ofile.id
    
    console.log(f"Update ontology: `{oid}`")

    with tempfile.TemporaryDirectory() as tmp_dir:
        # download in tmp location
        owl_path = Path(tmp_dir) / f"{oid.lower()}.owl"
        url = ofile.source
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(owl_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 

                    f.write(chunk)

        #only store gzip version
        with open(owl_path, 'rb') as f_in:
            gzip_path = RESOURCES_DIR / "ontologies" / f"{oid.lower()}.owl.gz"
            with gzip.open(gzip_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


def update_ontology_files() -> None:
    with ThreadPoolExecutor(max_workers=4) as pool:
        for ofile in ontology_files.values():
            pool.submit(update_ontology_file, ofile)


class Ontology:
    """Ontology."""
    _ontology: ProntoOntology = None

    def __init__(self, ontology_id):
        
        ontology_file = ontology_files[ontology_id]
        logger.info(f"Read ontology: `{ontology_id}`")
        
        # read ontology with pronto
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", pronto.utils.warnings.SyntaxWarning)
            warnings.simplefilter("ignore", pronto.utils.warnings.NotImplementedWarning)
            self.__class__._ontology = pronto.Ontology(ontology_file.filename)

    def get_proto_ontology(self):
        """Get a proto object for the ontology.

        :return: `pronto.Ontology`: pronto object for the ontology
        :rtype: [type]
        """
        return self._ontology


def create_ontology_enum(ontology_id: str, dir: Path):
    """Create enum of the ontology."""

    console.log(f"Create enum: `{ontology_id}`")

    def name_to_variable(name: str) -> str:
        """Clean string to python variable name."""
        if name is None:
            return None
        name = re.sub('\W|^(?=\d)','_', name)
        return name.upper()

    # load ontology
    terms: Dict[str, Dict] = {}
    ontology: Ontology = Ontology(ontology_id=ontology_id)
    
    names = set()
    pronto_term: ProntoTerm

    for term_id in ontology._ontology:    
        pronto_term = ontology._ontology[term_id]
        # print(pronto_term)
        
        var_name = name_to_variable(pronto_term.name)
        if var_name in names:
            logger.error(f"Duplicate name in ontology: `{var_name}`")
        elif var_name is None:
            logger.error(f"Name is none: `{pronto_term}`")
        else:
            names.add(var_name)
            term_id = pronto_term.id
            if ontology_id == "KISAO":
                term_id = term_id.replace("http://www.biomodels.net/kisao/KISAO#", "")
            if ":" in term_id:
                term_id = term_id.replace(":", "_")

            terms[term_id] = {
                "id": term_id,
                "var_name": var_name,
                "name": pronto_term.name,
                "definition": pronto_term.definition,
            }
    terms_sorted = {}
    for key in sorted(terms.keys()):
        terms_sorted[key] = terms[key]
    
    with open(RESOURCES_DIR / "templates" / "ontology_enum.pytemplate", "r") as f_template:
        template = Template(
            f_template.read(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        context={
            "ontology_id": ontology_id,
            "terms": terms_sorted,
        }
        module_str = template.render(**context)
        # print(module_str)
        path_module = ENUM_DIR / f"{ontology_id.lower()}.py"
        print(path_module)
        with open(path_module, "w") as f_py:
            f_py.write(module_str)

    # try to import
    importlib.import_module("pymetadata.metadata.sbo")


if __name__ == "__main__":
    # download latest versions
    # update_ontology_files()
    
    # load OWL files
    # ofile: OntologyFile
    # for oid, ofile in ontology_files.items():
        
    #     print("-" * 80)
    #     ontology = Ontology(ontology_id=oid)
    #     console.print(ontology)

    # convert to python module
    create_ontology_enum("SBO", dir=ENUM_DIR)
    create_ontology_enum("KISAO", dir=ENUM_DIR)
    create_ontology_enum("ECO", dir=ENUM_DIR)
    create_ontology_enum("BTO", dir=ENUM_DIR)

    for ontology_id in ontology_files:
        create_ontology_enum(ontology_id, dir=ENUM_DIR)
