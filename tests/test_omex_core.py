"""Tests of the archive `Omex` reads through `pymetadata-core`.

The public behaviour of `pymetadata.omex` is pinned by `tests/test_omex.py`;
these are the tests of the core backed read path: nothing is extracted before a
caller asks for it, the order and the count of the entries are the ones
`pymetadata` reported before the swap, and the local changes of an archive are
recorded for the write path.
"""

import logging
import shutil
import subprocess
import zipfile
from pathlib import Path

import pytest

from pymetadata._core_bridge import PasswordError, entries_for_archive, open_archive
from pymetadata.omex import (
    EntryFormat,
    ManifestEntry,
    Omex,
    format_from_suffix_and_head,
)

DATA = Path(__file__).parent / "data" / "omex"
FIXTURES = sorted(p.stem for p in DATA.glob("*.omex"))

COMPMODELS = DATA / "CompModels.omex"
ICGB21FR = DATA / "iCGB21FR.omex"

#: a `manifest.xml` which declares the archive and nothing else
MANIFEST = (
    '<?xml version="1.0"?><omexManifest '
    'xmlns="http://identifiers.org/combine.specifications/omex-manifest">'
    '<content location="." '
    'format="http://identifiers.org/combine.specifications/omex"/>'
    "</omexManifest>"
)

#: the entries `pymetadata` reported for `iCGB21FR.omex` before the swap: the
#: two required ones, the declared entries which have a member, in the order of
#: the manifest, then the 16 members the manifest does not list, sorted by
#: location. The declared `./iCGB21FR_memote.html` has no member and is dropped.
ICGB21FR_LOCATIONS = [
    ".",
    "./manifest.xml",
    "./metadata.rdf",
    "./iCGB21FR.xml",
    "./iCGB21FR_map.sbgn",
    "./iCGB21FR_map.json",
    "./FROG/iCGB21FR_FROG_Report.txt",
    "./FROG/.DS_Store",
    "./FROG/cameo/01_objective.tsv",
    "./FROG/cameo/02_fva.tsv",
    "./FROG/cameo/03_gene_deletion.tsv",
    "./FROG/cameo/04_reaction_deletion.tsv",
    "./FROG/cameo/metadata.json",
    "./FROG/cobrapy/01_objective.tsv",
    "./FROG/cobrapy/02_fva.tsv",
    "./FROG/cobrapy/03_gene_deletion.tsv",
    "./FROG/cobrapy/04_reaction_deletion.tsv",
    "./FROG/cobrapy/metadata.json",
    "./__MACOSX/._iCGB21FR.xml",
    "./__MACOSX/._iCGB21_memote.html",
    "./__MACOSX/._manifest.xml",
    "./__MACOSX/FROG/._.DS_Store",
    "./iCGB21_memote.html",
]


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


def _files_in(directory: Path) -> list[str]:
    """Return the files below a directory, as sorted relative POSIX paths."""
    return sorted(
        path.relative_to(directory).as_posix()
        for path in directory.rglob("*")
        if path.is_file()
    )


def test_from_omex_does_not_extract_anything_eagerly() -> None:
    """The temporary directory is empty directly after `from_omex`."""
    with Omex.from_omex(COMPMODELS) as omex:
        assert len(omex.manifest) == 6
        assert list(omex._tmp_dir.rglob("*")) == []


def test_get_path_materializes_the_entry_on_demand() -> None:
    """The file of an entry exists once its path was asked for."""
    with Omex.from_omex(COMPMODELS) as omex, zipfile.ZipFile(COMPMODELS) as zf:
        path = omex.get_path("./README.md")
        assert path == omex._tmp_dir / "README.md"
        assert path.read_bytes() == zf.read("README.md")


def test_get_path_materializes_only_that_entry() -> None:
    """No other entry is extracted, and a second ask does not extract again."""
    with Omex.from_omex(COMPMODELS) as omex:
        for _ in range(2):
            omex.get_path("./models/omex_comp.xml")
        assert _files_in(omex._tmp_dir) == ["models/omex_comp.xml"]
        assert omex._materialized == {"./models/omex_comp.xml"}


def test_get_path_of_a_derived_location_extracts_nothing() -> None:
    """The archive itself and the manifest have no file of their own."""
    with Omex.from_omex(COMPMODELS) as omex:
        assert omex.get_path(".") == omex._tmp_dir
        assert omex.get_path("./manifest.xml") == omex._tmp_dir / "manifest.xml"
        assert list(omex._tmp_dir.rglob("*")) == []


def test_get_path_raises_key_error_for_an_unknown_location() -> None:
    """A location which is not an entry of the archive has no path."""
    with Omex.from_omex(COMPMODELS) as omex, pytest.raises(KeyError):
        omex.get_path("./nope.txt")


def test_to_directory_materializes_every_entry(tmp_path: Path) -> None:
    """Every entry lands in the directory with the bytes of its member."""
    with Omex.from_omex(COMPMODELS) as omex, zipfile.ZipFile(COMPMODELS) as zf:
        omex.to_directory(tmp_path)
        for entry in omex.manifest.entries:
            if entry.location in (".", "./manifest.xml"):
                continue
            name = entry.location.removeprefix("./")
            assert (tmp_path / name).read_bytes() == zf.read(name)
    assert "manifest.xml" in _files_in(tmp_path)


def test_close_releases_the_archive() -> None:
    """A closed archive does not extract into the removed temporary directory."""
    omex = Omex.from_omex(COMPMODELS)
    tmp_dir = omex._tmp_dir
    omex.close()
    omex.close()

    assert omex._archive is None
    assert omex.get_path("./README.md") == tmp_dir / "README.md"
    assert not tmp_dir.exists()


def test_a_member_whose_name_needs_normalization_is_read(tmp_path: Path) -> None:
    """A member named with backslashes is the entry of the normalized location."""
    omex_path = tmp_path / "backslash.omex"
    with zipfile.ZipFile(omex_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        zf.writestr("models\\model.xml", "<sbml/>")

    with Omex.from_omex(omex_path) as omex:
        assert "./models/model.xml" in omex.manifest
        path = omex.get_path("./models/model.xml")
        assert path.read_text(encoding="utf-8") == "<sbml/>"


def test_from_omex_names_the_path_of_a_file_which_is_no_archive(
    tmp_path: Path,
) -> None:
    """The error of a file which is no archive names the manifest and the path."""
    omex_path = tmp_path / "plain.zip"
    with zipfile.ZipFile(omex_path, "w") as zf:
        zf.writestr("model.xml", "<sbml/>")

    with pytest.raises(ValueError, match="manifest") as error:
        Omex.from_omex(omex_path)
    assert str(omex_path) in str(error.value)


def _encrypted(tmp_path: Path, *names: str) -> Path:
    """Build a ZipCrypto protected archive of the given files with the `zip` tool."""
    (tmp_path / "manifest.xml").write_text(MANIFEST)
    (tmp_path / "a.txt").write_text("hi")
    out = tmp_path / "enc.omex"
    subprocess.run(
        ["zip", "-q", "-P", "secret", str(out), *names],
        cwd=tmp_path,
        check=True,
    )
    return out


@pytest.mark.skipif(
    shutil.which("zip") is None,
    reason="needs the zip tool to make a ZipCrypto archive, absent on Windows",
)
def test_from_omex_of_a_password_protected_archive(tmp_path: Path) -> None:
    """A protected archive is read with its password and refused without it."""
    omex_path = _encrypted(tmp_path, "manifest.xml", "a.txt")
    with Omex.from_omex(omex_path, password=b"secret") as omex:
        assert "./a.txt" in omex.manifest
        assert omex.get_path("./a.txt").read_text(encoding="utf-8") == "hi"

    for password in (None, b"wrong"):
        # a subclass of `ValueError`, and the path survives the translation
        with pytest.raises(PasswordError, match="password") as error:
            Omex.from_omex(omex_path, password=password)
        assert str(omex_path) in str(error.value)


@pytest.mark.skipif(
    shutil.which("zip") is None,
    reason="needs the zip tool to make a ZipCrypto archive, absent on Windows",
)
def test_is_omex_of_a_password_protected_archive(tmp_path: Path) -> None:
    """An encrypted archive is an archive, its manifest is only not readable."""
    assert Omex.is_omex(_encrypted(tmp_path, "manifest.xml", "a.txt")) is True


@pytest.mark.skipif(
    shutil.which("zip") is None,
    reason="needs the zip tool to make a ZipCrypto archive, absent on Windows",
)
def test_is_omex_of_an_encrypted_zip_without_a_manifest(tmp_path: Path) -> None:
    """A protected zip which holds no `manifest.xml` is no archive."""
    assert Omex.is_omex(_encrypted(tmp_path, "a.txt")) is False


def test_from_omex_keeps_the_order_of_pymetadata() -> None:
    """`.` and `./manifest.xml`, then the listed entries, then the unlisted ones."""
    with Omex.from_omex(ICGB21FR) as omex:
        assert [e.location for e in omex.manifest.entries] == ICGB21FR_LOCATIONS


def test_from_omex_drops_a_manifest_entry_without_a_member() -> None:
    """iCGB21FR lists `./iCGB21FR_memote.html`, which no member provides."""
    with Omex.from_omex(ICGB21FR) as omex:
        assert "./iCGB21FR_memote.html" not in omex.manifest


@pytest.mark.parametrize(
    ("name", "count"),
    [
        ("BIOMD0000000001", 16),
        ("CombineArchiveShowCase", 22),
        ("CompModels", 6),
        ("iCGB21FR", 23),
    ],
)
def test_from_omex_counts_the_entries_of_pymetadata(name: str, count: int) -> None:
    """The entry count of every fixture is the one reported before the swap."""
    with Omex.from_omex(DATA / f"{name}.omex") as omex:
        assert len(omex.manifest) == count


def test_is_omex_is_false_and_does_not_raise_for_a_file_which_is_not_a_zip(
    tmp_path: Path,
) -> None:
    """A file which is no archive is reported, not raised about."""
    path = tmp_path / "plain.txt"
    path.write_text("not a zip at all, but long enough", encoding="utf-8")
    assert Omex.is_omex(path) is False


def test_is_omex_raises_for_a_path_which_is_no_file(tmp_path: Path) -> None:
    """A path which does not exist or is a directory is an error, as before."""
    with pytest.raises(ValueError, match="does not exist"):
        Omex.is_omex(tmp_path / "missing.omex")
    with pytest.raises(ValueError, match="not a file"):
        Omex.is_omex(tmp_path)


def _archive_with(path: Path, name: str, method: int) -> Path:
    """Build an archive with one member written with the given method."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        zf.writestr(name, "x" * 100, compress_type=method)
    return path


def test_a_member_which_is_neither_stored_nor_deflated_warns(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """A bzip2 member is reported when the archive is read, as before the swap.

    Its bytes are refused by the core, which happens when they are asked for.
    """
    omex_path = _archive_with(tmp_path / "bzip2.omex", "b.txt", zipfile.ZIP_BZIP2)
    with caplog.at_level(logging.WARNING, logger="pymetadata.omex"):
        omex = Omex.from_omex(omex_path)
    assert [m for m in caplog.messages if "deflate" in m and "./b.txt" in m]

    with pytest.raises(ValueError, match=r"\./b\.txt"):
        omex.get_path("./b.txt")
    omex.close()


def test_an_unlisted_xml_member_which_cannot_be_read_is_guessed_by_its_suffix(
    tmp_path: Path,
) -> None:
    """A bzip2 `.xml` member does not keep the archive from being read.

    The format of an unlisted `.xml` member is classified from its first bytes,
    which a member the core refuses has none of. Such an archive was readable
    before the swap, so it stays readable, and the refusal arrives when the
    bytes of that one member are asked for.
    """
    omex_path = _archive_with(tmp_path / "bzip2.omex", "b.xml", zipfile.ZIP_BZIP2)
    with Omex.from_omex(omex_path) as omex:
        assert omex.manifest["./b.xml"].format == EntryFormat.XML.value
        with pytest.raises(ValueError, match=r"\./b\.xml"):
            omex.get_path("./b.xml")


def test_an_unlisted_xml_member_over_the_inflate_cap_is_guessed_by_its_suffix(
    tmp_path: Path,
) -> None:
    """A member above 1 GiB is refused by the core, which must not fail the read."""
    omex_path = tmp_path / "big.omex"
    with zipfile.ZipFile(omex_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        with zf.open("big.xml", "w", force_zip64=True) as member:
            block = bytes(1 << 24)
            for _ in range(65):
                member.write(block)

    with Omex.from_omex(omex_path) as omex:
        assert omex.manifest["./big.xml"].format == EntryFormat.XML.value
        with pytest.raises(ValueError, match=r"\./big\.xml"):
            omex.get_path("./big.xml")


@pytest.mark.parametrize(
    ("name", "message"),
    [("../evil.txt", "outside of the archive"), ("/abs/evil.txt", "relative")],
)
def test_a_member_which_points_outside_of_the_archive_is_refused(
    tmp_path: Path, name: str, message: str
) -> None:
    """A container with a member which escapes the archive is not read.

    Before the swap `zipfile.extractall` sanitized such a name and the member
    was read under the sanitized location; the core refuses the container,
    which is the zip slip hardening this swap keeps. The file is structurally
    an archive, so `is_omex` still answers True.
    """
    omex_path = tmp_path / "escape.omex"
    with zipfile.ZipFile(omex_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        zf.writestr(name, "x")

    assert Omex.is_omex(omex_path) is True
    with pytest.raises(ValueError, match=message) as error:
        Omex.from_omex(omex_path)
    assert str(omex_path) in str(error.value)


def test_a_stored_member_reads_without_a_warning(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """A stored member is allowed by the specification and is read."""
    omex_path = _archive_with(tmp_path / "stored.omex", "s.txt", zipfile.ZIP_STORED)
    with (
        caplog.at_level(logging.WARNING, logger="pymetadata.omex"),
        Omex.from_omex(omex_path) as omex,
    ):
        assert omex.get_path("./s.txt").read_text(encoding="utf-8") == "x" * 100
    assert not [m for m in caplog.messages if "deflate" in m]


def test_add_entry_records_the_copy_of_the_archive(tmp_path: Path) -> None:
    """The recorded file is the copy the archive owns, not the file of the caller.

    The caller may change or remove its file after `add_entry`, which must not
    change what the archive holds, nor what its write path reads.
    """
    source = tmp_path / "new.txt"
    source.write_text("new", encoding="utf-8")
    with Omex.from_omex(COMPMODELS) as omex:
        omex.add_entry(source, ManifestEntry(location="./new.txt", format="txt"))
        assert omex._changed == {"./new.txt": omex._tmp_dir / "new.txt"}
        assert omex._removed == set()

        source.write_text("changed", encoding="utf-8")
        assert omex.get_path("./new.txt").read_text(encoding="utf-8") == "new"
        assert omex._changed["./new.txt"].read_text(encoding="utf-8") == "new"


def test_add_entry_over_an_entry_of_the_source_archive_replaces_it(
    tmp_path: Path,
) -> None:
    """The added file wins over the member of the source archive."""
    source = tmp_path / "README.md"
    source.write_text("replaced", encoding="utf-8")
    with Omex.from_omex(COMPMODELS) as omex:
        omex.add_entry(
            source,
            ManifestEntry(location="./README.md", format=EntryFormat.MARKDOWN),
        )
        assert omex._changed == {"./README.md": omex._tmp_dir / "README.md"}
        assert omex.get_path("./README.md").read_text(encoding="utf-8") == "replaced"


def test_remove_entry_for_location_records_the_removal() -> None:
    """A removed location is recorded and its file is gone."""
    with Omex.from_omex(COMPMODELS) as omex:
        path = omex.get_path("README.md")
        assert omex._materialized == {"./README.md"}

        assert omex.remove_entry_for_location("README.md")
        assert omex._removed == {"./README.md"}
        assert omex._materialized == set()
        assert not path.exists()


def test_remove_entry_for_location_forgets_an_added_file(tmp_path: Path) -> None:
    """A file which was added and removed again is not read on a write."""
    source = tmp_path / "new.txt"
    source.write_text("new", encoding="utf-8")
    with Omex.from_omex(COMPMODELS) as omex:
        omex.add_entry(source, ManifestEntry(location="./new.txt", format="txt"))
        omex.remove_entry_for_location("./new.txt")
        assert omex._changed == {}
        assert omex._removed == {"./new.txt"}


def test_add_entry_after_a_removal_forgets_the_removal(tmp_path: Path) -> None:
    """A location which is removed and added again is not removed on a write."""
    source = tmp_path / "README.md"
    source.write_text("replaced", encoding="utf-8")
    with Omex.from_omex(COMPMODELS) as omex:
        omex.remove_entry_for_location("./README.md")
        omex.add_entry(
            source,
            ManifestEntry(location="./README.md", format=EntryFormat.MARKDOWN),
        )
        assert omex._changed == {"./README.md": omex._tmp_dir / "README.md"}
        assert omex._removed == set()


def test_get_path_of_an_entry_the_archive_has_no_content_for() -> None:
    """An entry a caller appended by hand has no content to extract."""
    with Omex.from_omex(COMPMODELS) as omex:
        omex.manifest.add_entry(ManifestEntry(location="./ghost.txt", format="txt"))
        assert not omex.get_path("./ghost.txt").exists()
