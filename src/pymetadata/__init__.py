"""spymetadata - Python utilities for metadata."""
from pathlib import Path

__author__ = "Matthias Koenig"
__version__ = "0.0.14"


from depinfo import print_dependencies  # type: ignore


def show_versions() -> None:
    """Print dependency information."""
    print_dependencies("pymetadata")


program_name: str = "pymetadata"
RESOURCES_DIR: Path = Path(__file__).parent / "resources"
ENUM_DIR: Path = Path(__file__).parent / "metadata"

CACHE_USE: bool = False
CACHE_PATH: Path = RESOURCES_DIR / "cache"
