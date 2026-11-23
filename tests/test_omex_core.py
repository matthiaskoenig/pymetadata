"""Tests that the formats the bridge guesses are the ones `pymetadata` guesses."""

from pathlib import Path

import pytest

from pymetadata._core_bridge import entries_for_archive, open_archive
from pymetadata.omex import Omex, format_from_suffix_and_head

DATA = Path(__file__).parent / "data" / "omex"
FIXTURES = sorted(p.stem for p in DATA.glob("*.omex"))


GUESSED = {
    "BIOMD0000000001": 1,
    "CombineArchiveShowCase": 0,
    "CompModels": 0,
    "iCGB21FR": 16,
}


@pytest.mark.parametrize("name", FIXTURES)
def test_guessed_formats_equal_omex_guess_format(name: str, tmp_path: Path) -> None:
    """The unlisted members get what `Omex.guess_format` gives the file."""
    archive = open_archive((DATA / f"{name}.omex").read_bytes(), None)
    declared = {loc for loc, _, _ in archive.declared_entries}
    checked = 0
    for entry in entries_for_archive(archive, format_from_suffix_and_head):
        location = str(entry["location"])
        if location in declared:
            continue
        target = tmp_path / location
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(archive.entry_bytes(location))
        assert entry["format"] == Omex.guess_format(target), location
        checked += 1
    assert checked == GUESSED[name]
