"""MIRIAM qualifiers.

A MIRIAM annotation combines a qualifier, saying how an element relates to
something else, with a resource pointing at a database entry. Biological
qualifiers (`BQB`) relate an element to a biological entity, model qualifiers
(`BQM`) describe the model itself.

```python
from pymetadata.core.annotation import RDFAnnotation
from pymetadata.identifiers.miriam import BQB

RDFAnnotation(qualifier=BQB.IS, resource="CHEBI:17234")
```

Choosing the qualifier matters: `BQB.IS` states that the element *is* the
annotated entity, whereas `BQB.IS_VERSION_OF` is the weaker claim that it is one
form of it.
"""

from enum import Enum

from pymetadata import log

logger = log.get_logger(__name__)

__all__ = [
    "BQB",
    "BQM",
]


class BQM(Enum):
    """MIRIAM model qualifier, relating a model to a resource.

    Use `BQM.IS_DESCRIBED_BY` to link a model to the publication describing it,
    and `BQM.IS_DERIVED_FROM` to link it to the model it was built from.
    """

    IS = "BQM_IS"
    IS_DESCRIBED_BY = "BQM_IS_DESCRIBED_BY"
    IS_DERIVED_FROM = "BQM_IS_DERIVED_FROM"
    IS_INSTANCE_OF = "BQM_IS_INSTANCE_OF"
    HAS_INSTANCE = "BQM_HAS_INSTANCE"
    UNKNOWN = "BQM_UNKNOWN"


class BQB(Enum):
    """MIRIAM biological qualifier, relating an element to a biological entity.

    The most common are `BQB.IS` (the element is the entity),
    `BQB.IS_VERSION_OF` (the element is one form of the entity),
    `BQB.IS_PART_OF` (the element is part of the entity) and `BQB.HAS_TAXON`
    (the entity occurs in the given taxon).
    """

    IS = "BQB_IS"
    HAS_PART = "BQB_HAS_PART"
    IS_PART_OF = "BQB_IS_PART_OF"
    IS_VERSION_OF = "BQB_IS_VERSION_OF"
    HAS_VERSION = "BQB_HAS_VERSION"
    IS_HOMOLOG_TO = "BQB_IS_HOMOLOG_TO"
    IS_DESCRIBED_BY = "BQB_IS_DESCRIBED_BY"
    IS_ENCODED_BY = "BQB_IS_ENCODED_BY"
    ENCODES = "BQB_ENCODES"
    OCCURS_IN = "BQB_OCCURS_IN"
    HAS_PROPERTY = "BQB_HAS_PROPERTY"
    IS_PROPERTY_OF = "BQB_IS_PROPERTY_OF"
    HAS_TAXON = "BQB_HAS_TAXON"
    UNKNOWN = "BQB_UNKNOWN"
