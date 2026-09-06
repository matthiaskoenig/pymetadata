"""Package handling ontologies."""

from .sbo import SBO, SBOType
from .kisao import KISAO, KISAOType
from .pbpko import PBPKO, PBPKOType

__all__ = ["SBO", "SBOType", "KISAO", "KISAOType", "PBPKO", "PBPKOType"]
