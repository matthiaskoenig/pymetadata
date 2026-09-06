"""pymetadata - Python utilities for metadata."""

import logging
from pathlib import Path

# the package does not configure logging, see `pymetadata.log`
logging.getLogger(__name__).addHandler(logging.NullHandler())

__author__ = "Matthias Koenig"
__version__ = "0.5.12"


program_name: str = "pymetadata"
RESOURCES_DIR: Path = Path(__file__).parent / "resources"
#: the generated ontology modules, see `pymetadata.ontologies._ontology_builder`
ONTOLOGY_DIR: Path = Path(__file__).parent / "ontologies"

CACHE_USE: bool = False
CACHE_PATH: Path = Path.home() / ".cache" / "pymetadata"
