"""Systems biology ontology (SBO) terms and information."""



from typing import Dict


class OntologyLookup:
    """Helper class for simple lookup by name or definition.
    
    
    - access by id attribute
    - access by name attribute
    - search functionality
    - get resource term.
    """

    mapping: Dict[str, str] = {
        "SBO_0000628": "DEMAND_REACTION"
    }
    mapping_reverse: Dict[str, str] = {v: k for k, v in mapping.items()}

    def __init__(self):

        for key, value in {"SBO_0000628": "DEMAND_REACTION"}.items():
            setattr(self, key, value)
            setattr(self, key, key)

        self.EXCHANGE_REACTION = "SBO:0000627"
        self.SBO_0000627 = "SBO:0000627"

    def __getattr__(self, item):
        if item in self.mapping:
            return self.mapping[item]
        elif item in self.mapping_reverse:
            return self.mapping_reverse[item]

    def __dir__(self):
        return self.mapping.keys() +  self.mapping_reverse.keys()


class OntologyLookupFactory():

    @staticmethod
    def parse_obo(obo_path) -> OntologyLookup:
        pass 


class SBO(OntologyLookup):
    pass

SBO = OntologyLookup()



#FIXME: create an SBO enum with all terms.

SBO.exchange_reaction = "SBO:0000627"

SBO.EXCHANGE_REACTION = "SBO:0000627"
SBO.DEMAND_REACTION = "SBO:0000628"
SBO.SINK_REACTION = "SBO:0000632"

SBO.BIOCHEMICAL_REACTION = "SBO:0000176"
SBO.TRANSPORT_REACTION = "SBO:0000655"

SBO.SIMPLE_CHEMICAL = "SBO:0000247"
SBO.MACROMOLECULE = "SBO:0000245"

SBO.FLUX_BOUND = "SBO:0000612"

SBO.MAXIMAL_VELOCITY = "SBO:0000186"
SBO.MICHAELIS_CONSTANT = "SBO:0000371"
SBO.KINETIC_CONSTANT = "SBO:0000009"

SBO.PHYSICAL_COMPARTMENT = "SBO:0000290"

SBO.CONTINOUS_FRAMEWORK = "SBO:0000293"
SBO.FLUX_BALANCE_FRAMEWORK = "SBO:0000624"


__all__ = [
    "SBO",
]
