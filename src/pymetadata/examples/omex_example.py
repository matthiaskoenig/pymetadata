"""Example for reading and writing omex archives."""
import zipfile
from pathlib import Path

from pymetadata import RESOURCES_DIR
from pymetadata.console import console
from pymetadata.omex import EntryFormat, ManifestEntry, Omex


"""
# COMBINE archives in `pymetadata`
COMBINE archives are a convenient method to exchange files and resources relevant
for modeling studies. `pymetadata` provides functionality for reading, writing
and validating archives.

## Read archive from OMEX
To read a COMBINE archive use the `Omex` helper methods which can either read from
a given directory or
"""
omex_example: Path = RESOURCES_DIR / "data" / "omex" / "CompModels.omex"
omex = Omex.from_omex(omex_example)
console.print(omex)

"""
## Write archive to directory or archive
"""
omex.to_directory(Path("./results/testomex"))
omex.to_omex(Path("./results/test_from_omex.omex"))

"""
## Create archive from files
In the following a new archive is created by adding entries to the archive.
"""
omex = Omex()
omex.add_entry(
    entry_path=Path("results/testomex/models/omex_comp_flat.xml"),
    entry=ManifestEntry(location="./model.xml", format=EntryFormat.SBML, master=False),
)
omex.add_entry(
    entry_path=Path("results/testomex/README.md"),
    entry=ManifestEntry(
        location="./README.md", format=EntryFormat.MARKDOWN, master=False
    ),
)
omex.to_omex(Path("results/test_from_files.omex"))
console.print(omex)
