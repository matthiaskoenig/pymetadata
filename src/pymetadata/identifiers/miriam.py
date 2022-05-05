"""Module for working with MIRIAM qualifiers."""

from enum import Enum

from pymetadata import log


logger = log.get_logger(__name__)

__all__ = [
    "BQM",
    "BQB",
]


class BQM(Enum):
    """MIRIAM model qualifier."""

    IS = "BQM_IS"
    IS_DESCRIBED_BY = "BQM_IS_DESCRIBED_BY"
    IS_DERIVED_FROM = "BQM_IS_DERIVED_FROM"
    IS_INSTANCE_OF = "BQM_IS_INSTANCE_OF"
    HAS_INSTANCE = "BQM_HAS_INSTANCE"
    UNKNOWN = "BQM_UNKNOWN"


class BQB(Enum):
    """MIRIAM biological qualifier."""

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
