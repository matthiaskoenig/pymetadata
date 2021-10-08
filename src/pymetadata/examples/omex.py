"""Example for reading and writing omex archives."""
from pathlib import Path

from pymetadata import RESOURCES_DIR
from pymetadata.console import console
from pymetadata.omex import Omex


# read existing archive
# omex_example: Path = RESOURCES_DIR / "testdata" / "omex" / "CombineArchiveShowCase.omex"
omex_example: Path = RESOURCES_DIR / "testdata" / "omex" / "CompModels.omex"
omex = Omex.from_omex(omex_example)
console.print(omex.manifest.dict())


omex.to_directory(Path("./testomex"))
omex.to_omex(Path("./test.omex"))
