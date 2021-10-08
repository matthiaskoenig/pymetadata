"""
Example for reading and writing omex archives.
"""
from pathlib import Path

from pymetadata import RESOURCES_DIR
from pymetadata.omex import Omex
from pymetadata.console import console

# read existing archive
# omex_example: Path = RESOURCES_DIR / "testdata" / "omex" / "CombineArchiveShowCase.omex"
omex_example: Path = RESOURCES_DIR / "testdata" / "omex" / "CompModels.omex"
omex = Omex.from_omex(omex_example)
console.print(omex.manifest.dict())

# omex.to_directory(Path("./testomex"))


# omex.
# omex = Omex.from_directory(
#     omex_path=RESOURCES_DIR / "testdata" / "omex" / "omex1.omex",
#     directory=RESOURCES_DIR / "testdata" / "omex" / "omex1",
#     creators=[creator],
# )
# print(omex)
