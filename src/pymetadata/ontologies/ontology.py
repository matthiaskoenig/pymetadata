"""Hardcoded ontologies."""
from dataclasses import dataclass
from enum import Enum

class OntologyFormat(Enum):
    OBO = 1
    OWL = 2

@dataclass
class OntologyFile:
    id: str
    name: str
    format: OntologyFormat
    version: str
    

_ontologies: List[OntologyFile] = [
    OntologyFile(
        "KISAO", 
        name="Kinetic Simulation Algorithm Ontology", 
        format=OntologyFormat.OWL,
        version="2.28",
    ),
    OntologyFile(
        "SBO", 
        name="Systems Biology Ontology", 
        format=OntologyFormat.OBO,
        version="03:02:2018",
    ),
    # OntologyFile(
    #     "NCIT", 
    #     name="National Cancer Institute Thesaurus", 
    #     format=OntologyFormat.OWL,
    #     version="21.08",
    # ),
    # OntologyFile(
    #     "CHEBI", 
    #     name="Chemical Entities of Biological Interest Ontology", 
    #     format=OntologyFormat.OBO,
    #     version="203",
    # ),
}

ontologies: Dict = {ontology.id, ontology for ontology in _ontologies}
