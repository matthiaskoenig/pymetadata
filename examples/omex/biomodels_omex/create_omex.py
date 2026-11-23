"""Creating the COMBINE archive of a biomodels entry from a directory of files.

Run with `python examples/omex/biomodels_omex/create_omex.py`. The archive is
written to a temporary directory and read back, so a run does not modify a file
of the repository.
"""

import tempfile
from pathlib import Path

from pymetadata.console import console
from pymetadata.omex import EntryFormat, ManifestEntry, Omex

files_dir: Path = Path(__file__).parent / "files"

omex = Omex()

# add matlab files
entry_info = [
    ("*.m", EntryFormat.M),
    ("*.mat", EntryFormat.MAT),
    ("*.csv", EntryFormat.CSV),
    ("*.rdf", EntryFormat.OMEX_METADATA),
]
master_file = "Zhou2024_Updated-model.m"

for extension, entry_format in entry_info:
    for f in files_dir.glob(extension):
        fname = f.name
        omex.add_entry(
            entry_path=f,
            entry=ManifestEntry(
                location=f"./{fname}",
                format=entry_format,
                master=(fname == master_file),
            ),
        )

with tempfile.TemporaryDirectory() as tmp_dir:
    omex_path = Path(tmp_dir) / "MODEL2402290004.4_pymetadata.omex"
    omex.to_omex(omex_path)
    with Omex.from_omex(omex_path) as written:
        console.print(written)
