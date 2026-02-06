"""OMEX example for biomodels."""

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
            entry_path=Path(f"./files/{fname}"),
            entry=ManifestEntry(
                location=f"./{fname}",
                format=entry_format,
                master=(fname == master_file),
            ),
        )

omex.to_omex(Path("MODEL2402290004.4_pymetadata.omex"))
console.print(omex)
