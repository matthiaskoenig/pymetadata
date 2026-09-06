"""Ontologies: term enums, lookup and generation.

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
from pymetadata.ontologies import SBO

SBO.SBO_0000247                    # by id
SBO.SIMPLE_CHEMICAL                # by name
SBO.validate("SBO:0000247")        # SBO.SBO_0000247
SBO.get_name(SBO.SIMPLE_CHEMICAL)  # 'simple chemical'
```

The `<ONTOLOGY>Type` aliases are `Union[str, <ONTOLOGY>]` and are the type to
accept in a signature which takes either an enum member or the term as a string.

The generated modules are large, so they are imported on first access instead of
with the package: looking up a term in OLS (`pymetadata.ontologies.ols`) does not
pay for them. The modules are generated with `pymetadata.ontologies.ontology`
and should never be edited by hand.
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .eco import ECO, ECOType
    from .kisao import KISAO, KISAOType
    from .pbpko import PBPKO, PBPKOType
    from .sbo import SBO, SBOType

__all__ = [
    "ECO",
    "KISAO",
    "PBPKO",
    "SBO",
    "ECOType",
    "KISAOType",
    "PBPKOType",
    "SBOType",
]

#: module of the generated enums, keyed by the name they are exported under
_ENUM_MODULES: dict[str, str] = {
    "ECO": "eco",
    "ECOType": "eco",
    "KISAO": "kisao",
    "KISAOType": "kisao",
    "PBPKO": "pbpko",
    "PBPKOType": "pbpko",
    "SBO": "sbo",
    "SBOType": "sbo",
}


def __getattr__(name: str) -> Any:
    """Import a generated enum module on first access.

    Args:
        name: name of an enum or of one of the type aliases

    Returns:
        The enum or type alias.

    Raises:
        AttributeError: if the package has no such attribute
    """
    module_name = _ENUM_MODULES.get(name)
    if module_name is None:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

    attribute = getattr(importlib.import_module(f".{module_name}", __name__), name)
    # cache the attribute, the next access does not enter `__getattr__` again
    globals()[name] = attribute
    return attribute


def __dir__() -> list[str]:
    """List the attributes of the package, including the enums not yet imported.

    Returns:
        The attribute names.
    """
    return sorted(set(globals()) | set(__all__))
