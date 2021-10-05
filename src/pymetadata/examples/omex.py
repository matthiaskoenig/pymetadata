"""Example for reading and writing omex archives."""
from pathlib import Path

from pymetadata import RESOURCES_DIR
from pymetadata.omex import Creator, Omex


# read existing archive
omex_example: Path = RESOURCES_DIR / "testdata" / "omex" / "CombineArchiveShowCase.omex"
omex = Omex(omex_path=omex_example, working_dir=Path("."))
print(omex)

# create archive from directory
creator = Creator(
    givenName="Matthias",
    familyName="König",
    organization="Humboldt University Berlin",
    site="https://livermetabolism.com",
    email="konigmatt@googlemail.com",
)
omex = Omex.from_directory(
    omex_path=RESOURCES_DIR / "testdata" / "omex" / "omex1.omex",
    directory=RESOURCES_DIR / "testdata" / "omex" / "omex1",
    creators=[creator],
)
print(omex)
