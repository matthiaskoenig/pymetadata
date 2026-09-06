"""Reading, inspecting, creating and writing COMBINE archives.

Run with `python -m pymetadata.examples.omex_example`. All output is written to
a temporary directory.
"""

import tempfile
from pathlib import Path

from pymetadata import log
from pymetadata.console import console
from pymetadata.omex import EntryFormat, ManifestEntry, Omex

EXAMPLE_OMEX: Path = Path(__file__).parent / "test.omex"


def read_archive(omex_path: Path) -> None:
    """Read an archive and inspect its content.

    The entries of the archive are available from the manifest; `get_path`
    resolves an entry to a file which can be passed on to a model reader.
    """
    console.rule("Read archive", style="white")
    omex = Omex.from_omex(omex_path)
    console.print(omex)

    console.print(f"Entries: {len(omex.manifest)}")
    console.print(f"Contains './README.md': {'./README.md' in omex.manifest}")

    # select entries by format instead of matching format strings
    for entry in omex.entries_by_format("sbml"):
        console.print(f"SBML: {entry.location} -> {omex.get_path(entry.location)}")


def extract_archive(omex_path: Path, output_dir: Path) -> None:
    """Extract an archive to a directory.

    The `manifest.xml` is written as well, so the directory can be read back
    with `Omex.from_directory`.
    """
    console.rule("Extract archive", style="white")
    omex = Omex.from_omex(omex_path)
    omex.to_directory(output_dir)
    console.print(sorted(str(p.relative_to(output_dir)) for p in output_dir.rglob("*")))


def create_archive_from_files(model_path: Path, omex_path: Path) -> None:
    """Create an archive by adding single files.

    Every file needs a `ManifestEntry` with the location in the archive and the
    format of the file. Files are copied when they are added.
    """
    console.rule("Create archive from files", style="white")
    omex = Omex()
    omex.add_entry(
        entry_path=model_path,
        entry=ManifestEntry(
            location="./models/model.xml",
            format=EntryFormat.SBML_L3V1,
            master=True,
        ),
    )
    omex.to_omex(omex_path)
    console.print(omex)


def create_archive_from_directory(directory: Path, omex_path: Path) -> None:
    """Create an archive from a directory.

    Formats are taken from an existing `manifest.xml` and guessed from the file
    content and suffix for everything else.
    """
    console.rule("Create archive from directory", style="white")
    omex = Omex.from_directory(directory)
    omex.to_omex(omex_path)
    console.print(omex)


if __name__ == "__main__":
    log.enable_rich_logging()
    with tempfile.TemporaryDirectory() as tmp_dir:
        results_dir = Path(tmp_dir)

        read_archive(EXAMPLE_OMEX)

        extracted_dir = results_dir / "extracted"
        extract_archive(EXAMPLE_OMEX, extracted_dir)

        create_archive_from_files(
            model_path=extracted_dir / "models" / "omex_comp_flat.xml",
            omex_path=results_dir / "from_files.omex",
        )
        create_archive_from_directory(
            directory=extracted_dir,
            omex_path=results_dir / "from_directory.omex",
        )
