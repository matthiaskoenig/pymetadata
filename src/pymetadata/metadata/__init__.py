"""Ontology terms as python enums.

The ontologies are shipped as enums generated from the ontology releases, so
terms can be used with autocompletion and are checked at runtime instead of
being passed around as strings.

| enum | ontology |
| --- | --- |
| `SBO` | Systems Biology Ontology, roles of model components |
| `KISAO` | Kinetic Simulation Algorithm Ontology, simulation algorithms |
| `ECO` | Evidence & Conclusion Ontology, evidence types |
| `PBPKO` | PBPK Ontology, physiologically based pharmacokinetic modeling |

Every term is available under its identifier and under its name, and `validate`
accepts both the underscore and the colon notation:

```python
from pymetadata.metadata import SBO

SBO.SBO_0000247            # by id
SBO.SIMPLE_CHEMICAL        # by name
SBO.validate("SBO:0000247")  # SBO.SBO_0000247
SBO.get_name(SBO.SIMPLE_CHEMICAL)  # 'simple chemical'
```

The `<ONTOLOGY>Type` aliases are `Union[str, <ONTOLOGY>]` and are the type to
accept in a signature which takes either an enum member or the term as a string.

The modules are generated, see `pymetadata.ontologies.ontology`.
"""

from .sbo import SBO, SBOType
from .kisao import KISAO, KISAOType
from .eco import ECO, ECOType
from .pbpko import PBPKO, PBPKOType

__all__ = [
    "SBO",
    "SBOType",
    "KISAO",
    "KISAOType",
    "ECO",
    "ECOType",
    "PBPKO",
    "PBPKOType",
]
