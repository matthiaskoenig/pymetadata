"""Tests of the archive `Omex` reads and writes through `pymetadata-core`.

The public behaviour of `pymetadata.omex` is pinned by `tests/test_omex.py`;
these are the tests of the core backed read and write path: nothing is extracted
before a caller asks for it, the order and the count of the entries are the ones
`pymetadata` reported before the swap, and a member nobody touched is copied as
the compressed blob it is instead of being inflated and deflated again.
"""

import logging
import os
import random
import shutil
import stat
import subprocess
import tracemalloc
import zipfile
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path

import pytest

from pymetadata._core_bridge import PasswordError, entries_for_archive, open_archive
from pymetadata.omex import (
    EntryFormat,
    ManifestEntry,
    Omex,
    _format_from_suffix_and_head,
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
    for entry in entries_for_archive(archive, _format_from_suffix_and_head):
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


@pytest.mark.parametrize("name", FIXTURES)
def test_to_directory_writes_every_entry(name: str, tmp_path: Path) -> None:
    """Every entry lands in the directory with the bytes of its member.

    Every fixture: the unlisted members and the nesting of `iCGB21FR` are
    written as the listed ones, and its dangling entry, which the read dropped,
    does not make the write fail.
    """
    omex_path = DATA / f"{name}.omex"
    with Omex.from_omex(omex_path) as omex, zipfile.ZipFile(omex_path) as zf:
        omex.to_directory(tmp_path)
        written = []
        for entry in omex.manifest.entries:
            if entry.location in (".", "./manifest.xml"):
                continue
            member = entry.location.removeprefix("./")
            assert (tmp_path / member).read_bytes() == zf.read(member)
            written.append(member)
    assert _files_in(tmp_path) == sorted([*written, "manifest.xml"])


@pytest.mark.parametrize("name", FIXTURES)
def test_to_directory_writes_every_member_once(name: str, tmp_path: Path) -> None:
    """The destination is written straight from the archive, not through a copy.

    The temporary directory of the archive stays empty: a member which was not
    extracted before is written to its destination, nowhere else.
    """
    with Omex.from_omex(DATA / f"{name}.omex") as omex:
        omex.to_directory(tmp_path)
        assert list(omex._tmp_dir.rglob("*")) == []
        assert omex._materialized == set()


def test_to_directory_writes_an_extracted_entry_from_its_file(tmp_path: Path) -> None:
    """A file in the temporary directory is the content of its entry.

    A caller which changed the file of an extracted entry sees the change in the
    directory, as it did before the content was read lazily.
    """
    with Omex.from_omex(COMPMODELS) as omex:
        omex.get_path("./README.md").write_text("edited", encoding="utf-8")
        omex.to_directory(tmp_path)
    assert (tmp_path / "README.md").read_text(encoding="utf-8") == "edited"


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
def test_to_omex_of_a_password_protected_archive(tmp_path: Path) -> None:
    """A protected archive is written plain, not as half of an encrypted one.

    Encrypted archives cannot be written: the members of the written archive are
    deflated from the bytes which were read, with no member left encrypted, and
    the result is read back without a password.
    """
    omex_path = _encrypted(tmp_path, "manifest.xml", "a.txt")
    target = tmp_path / "plain.omex"
    with Omex.from_omex(omex_path, password=b"secret") as omex:
        omex.to_omex(target)

    with zipfile.ZipFile(target) as zf:
        # bit 0 of the general purpose flags marks an encrypted member
        assert [info.filename for info in zf.infolist() if info.flag_bits & 0x1] == []
    with Omex.from_omex(target) as result:
        assert "./a.txt" in result.manifest
        assert result.get_path("./a.txt").read_text(encoding="utf-8") == "hi"


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


def test_remove_entry_for_location_drops_the_file_of_the_entry() -> None:
    """A removed location loses its file and is materialized no more."""
    with Omex.from_omex(COMPMODELS) as omex:
        path = omex.get_path("README.md")
        assert omex._materialized == {"./README.md"}

        assert omex.remove_entry_for_location("README.md")
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


def test_add_entry_after_a_removal_keeps_the_added_file(tmp_path: Path) -> None:
    """A location which is removed and added again is written from the new file."""
    source = tmp_path / "README.md"
    source.write_text("replaced", encoding="utf-8")
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.remove_entry_for_location("./README.md")
        omex.add_entry(
            source,
            ManifestEntry(location="./README.md", format=EntryFormat.MARKDOWN),
        )
        assert omex._changed == {"./README.md": omex._tmp_dir / "README.md"}
        omex.to_omex(target)

    with zipfile.ZipFile(target) as zf:
        assert zf.read("README.md") == b"replaced"


def test_get_path_of_an_entry_the_archive_has_no_content_for() -> None:
    """An entry a caller appended by hand has no content to extract."""
    with Omex.from_omex(COMPMODELS) as omex:
        omex.manifest.add_entry(ManifestEntry(location="./ghost.txt", format="txt"))
        assert not omex.get_path("./ghost.txt").exists()


def _blobs(omex_path: Path) -> dict[str, tuple[int, int, int]]:
    """Return method, compressed size and CRC of every file member of a zip.

    The directory members some containers hold are left out: they are no entry
    of an archive and are not written back.

    Args:
        omex_path: path of the zip container

    Returns:
        The method, the compressed size and the CRC per member name.
    """
    with zipfile.ZipFile(omex_path) as zf:
        return {
            info.filename: (info.compress_type, info.compress_size, info.CRC)
            for info in zf.infolist()
            if not info.is_dir()
        }


@pytest.mark.parametrize("name", FIXTURES)
def test_a_write_without_a_change_copies_every_member(
    name: str, tmp_path: Path
) -> None:
    """Read an archive and write it back: every member keeps its compressed blob.

    Nothing is inflated and nothing is deflated again, which is what the swap
    exists for; only the `manifest.xml` is written anew.
    """
    omex_path = DATA / f"{name}.omex"
    target = tmp_path / "out.omex"
    with Omex.from_omex(omex_path) as omex:
        omex.to_omex(target)

    before = _blobs(omex_path)
    del before["manifest.xml"]
    after = _blobs(target)
    assert {member: after[member] for member in before} == before


def test_a_compresslevel_of_minus_one_is_the_default(tmp_path: Path) -> None:
    """`-1` is the default level of `zipfile`, and writes the same archive."""
    default, minus_one = tmp_path / "default.omex", tmp_path / "minus_one.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.to_omex(default)
        omex.to_omex(minus_one, compresslevel=-1)
    assert minus_one.read_bytes() == default.read_bytes()


@pytest.mark.parametrize("level", [10, -2])
def test_a_compresslevel_outside_of_zero_to_nine_raises(
    level: int, tmp_path: Path
) -> None:
    """A level outside of 0 to 9 is a `ValueError` and writes no file."""
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex, pytest.raises(ValueError, match="level"):
        omex.to_omex(target, compresslevel=level)
    assert not target.exists()


def test_an_untouched_member_is_copied_as_its_compressed_blob(tmp_path: Path) -> None:
    """Read, change one entry, write: every other member keeps its blob."""
    source = tmp_path / "README.md"
    source.write_text("replaced", encoding="utf-8")
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.add_entry(
            source, ManifestEntry(location="./README.md", format=EntryFormat.MARKDOWN)
        )
        omex.to_omex(target)

    before, after = _blobs(COMPMODELS), _blobs(target)
    untouched = {
        member: blob
        for member, blob in before.items()
        if member not in ("README.md", "manifest.xml")
    }
    assert len(untouched) == 3
    assert {member: after[member] for member in untouched} == untouched
    assert after["README.md"] != before["README.md"]


def test_a_changed_entry_is_written_from_the_new_bytes(tmp_path: Path) -> None:
    """The file of the changed entry is the content of its member."""
    source = tmp_path / "README.md"
    source.write_text("replaced", encoding="utf-8")
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.add_entry(
            source, ManifestEntry(location="./README.md", format=EntryFormat.MARKDOWN)
        )
        omex.to_omex(target)

    with zipfile.ZipFile(target) as zf:
        assert zf.read("README.md") == b"replaced"
    with Omex.from_omex(target) as result:
        assert result.manifest["./README.md"].format == EntryFormat.MARKDOWN.value


def test_a_member_changed_in_place_is_written_from_its_file(tmp_path: Path) -> None:
    """A file a caller changed in the temporary directory is written.

    The temporary directory is the working copy of the archive: a file which is
    in it wins over the member of the archive it was read from, which is what
    `to_omex` did before the content was read lazily.
    """
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.get_path("./README.md").write_text("edited", encoding="utf-8")
        omex.to_omex(target)

    with zipfile.ZipFile(target) as zf:
        assert zf.read("README.md") == b"edited"


def test_a_manifest_entry_whose_file_is_missing_still_raises_file_not_found(
    tmp_path: Path,
) -> None:
    """An entry the caller appended without a file is no silent empty member."""
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.manifest.add_entry(
            ManifestEntry(location="./ghost.txt", format=EntryFormat.TXT)
        )
        with pytest.raises(FileNotFoundError):
            omex.to_omex(target)

    assert list(tmp_path.iterdir()) == []


def test_the_target_is_untouched_when_the_write_fails(tmp_path: Path) -> None:
    """A failing write keeps the existing archive and leaves no temporary file."""
    target = tmp_path / "out.omex"
    target.write_bytes(b"existing")
    with Omex.from_omex(COMPMODELS) as omex:
        omex.manifest.add_entry(
            ManifestEntry(location="./ghost.txt", format=EntryFormat.TXT)
        )
        with pytest.raises(FileNotFoundError):
            omex.to_omex(target)

    assert target.read_bytes() == b"existing"
    assert list(tmp_path.iterdir()) == [target]


def test_a_location_removed_and_declared_again_keeps_its_member(
    tmp_path: Path,
) -> None:
    """A location the manifest declares again is written, not dropped.

    `Manifest` is public and mutable: a location which is removed and declared
    again by hand is wanted, and its member is still in the archive, so it is
    written with the bytes it has.
    """
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex, zipfile.ZipFile(COMPMODELS) as zf:
        omex.remove_entry_for_location("./README.md")
        omex.manifest.add_entry(
            ManifestEntry(location="./README.md", format=EntryFormat.MARKDOWN)
        )
        omex.to_omex(target)
        expected = zf.read("README.md")

    with zipfile.ZipFile(target) as zf:
        assert zf.read("README.md") == expected


def test_a_removed_location_is_not_written(tmp_path: Path) -> None:
    """A removed entry and its member are gone from the written archive."""
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.remove_entry_for_location("./README.md")
        omex.to_omex(target)

    assert "README.md" not in _blobs(target)
    with Omex.from_omex(target) as result:
        assert "./README.md" not in result.manifest
        assert len(result.manifest) == 5


def test_a_dangling_entry_of_the_source_archive_does_not_make_a_write_raise(
    tmp_path: Path,
) -> None:
    """iCGB21FR declares `./iCGB21FR_memote.html`, which no member provides."""
    target = tmp_path / "out.omex"
    with Omex.from_omex(ICGB21FR) as omex:
        omex.to_omex(target)

    with Omex.from_omex(target) as result:
        assert "./iCGB21FR_memote.html" not in result.manifest
        assert sorted(e.location for e in result.manifest.entries) == sorted(
            ICGB21FR_LOCATIONS
        )


@pytest.mark.parametrize("name", FIXTURES)
def test_a_round_trip_keeps_every_entry_with_its_format_and_master_flag(
    name: str, tmp_path: Path
) -> None:
    """Read, write, read: the same entries with the same formats and flags.

    The `manifest.xml` of a written archive is serialized by the core from the
    entries `Omex` holds, and the format which `pymetadata` guesses for a member
    no manifest lists is not the one the core invents for it, which comes from
    the suffix alone. The entries of `pymetadata` are the ones which have to
    survive a write, formats and master flags included. The order of the entries
    is the one of the container, so they are compared as a set.
    """
    target = tmp_path / "out.omex"
    with Omex.from_omex(DATA / f"{name}.omex") as omex:
        before = {(e.location, e.format, e.master) for e in omex.manifest.entries}
        omex.to_omex(target)

    with Omex.from_omex(target) as result:
        after = {(e.location, e.format, e.master) for e in result.manifest.entries}
    assert after == before


@pytest.mark.skipif(os.name == "nt", reason="POSIX file modes")
def test_the_written_archive_has_the_mode_of_a_freshly_created_file(
    tmp_path: Path,
) -> None:
    """The archive is created with the permissions of a regular new file."""
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.to_omex(target)
    reference = tmp_path / "reference"
    reference.touch()

    assert stat.S_IMODE(target.stat().st_mode) == stat.S_IMODE(reference.stat().st_mode)


def test_to_omex_of_an_archive_built_from_a_directory(tmp_path: Path) -> None:
    """An archive without a source container is written from its files."""
    directory = tmp_path / "study"
    (directory / "models").mkdir(parents=True)
    (directory / "models" / "model.xml").write_text("<sbml/>", encoding="utf-8")
    (directory / "README.md").write_text("# study", encoding="utf-8")
    target = tmp_path / "out.omex"
    with Omex.from_directory(directory) as omex:
        locations = [e.location for e in omex.manifest.entries]
        omex.to_omex(target)

    with Omex.from_omex(target) as result:
        assert [e.location for e in result.manifest.entries] == locations
        assert (
            result.get_path("./models/model.xml").read_text(encoding="utf-8")
            == "<sbml/>"
        )
    assert set(_blobs(target)) == {
        "manifest.xml",
        "README.md",
        "models/model.xml",
    }


def test_a_location_with_xml_special_characters_round_trips_through_the_core(
    tmp_path: Path,
) -> None:
    """The manifest of the core escapes a location, as `pymetadata` does."""
    # `"`, `<` and `>` are not allowed in file names on Windows
    location = "./a&b 'c'.txt" if os.name == "nt" else "./a&b \"c\" <d> 'e'.txt"
    source = tmp_path / "source.txt"
    source.write_text("content", encoding="utf-8")
    target = tmp_path / "special.omex"
    with Omex() as omex:
        omex.add_entry(source, ManifestEntry(location=location, format=EntryFormat.TXT))
        omex.to_omex(target)

    with Omex.from_omex(target) as result:
        assert location in result.manifest
        assert result.get_path(location).read_text(encoding="utf-8") == "content"


def test_a_backslash_location_is_normalized_before_it_reaches_the_core(
    tmp_path: Path,
) -> None:
    r"""`a\b.xml` is the location `./a/b.xml` in the written manifest."""
    source = tmp_path / "source.xml"
    source.write_text("<sbml/>", encoding="utf-8")
    target = tmp_path / "backslash.omex"
    with Omex() as omex:
        omex.add_entry(source, ManifestEntry(location="a\\b.xml", format="sbml"))
        omex.to_omex(target)

    with zipfile.ZipFile(target) as zf:
        assert 'location="./a/b.xml"' in zf.read("manifest.xml").decode("utf-8")
        assert zf.read("a/b.xml") == b"<sbml/>"


def test_zip_stored_is_written_deflated_at_level_zero(tmp_path: Path) -> None:
    """The core has no stored path, so `ZIP_STORED` is deflate at level 0.

    The parameter is kept and nothing fails; a COMBINE archive is deflated by
    definition, so the request is logged and the members are not compressed.
    """
    target = tmp_path / "stored.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.to_omex(target, compression=zipfile.ZIP_STORED)

    blobs = _blobs(target)
    assert {method for method, _, _ in blobs.values()} == {zipfile.ZIP_DEFLATED}
    assert (
        blobs["models/omex_comp.xml"][1] > _blobs(COMPMODELS)["models/omex_comp.xml"][1]
    )
    with Omex.from_omex(target) as result:
        assert len(result.manifest) == 6


def test_a_compression_level_other_than_nine_recompresses_every_member(
    tmp_path: Path,
) -> None:
    """A caller which asks for a level gets it, for every member.

    The yardstick is an archive which holds the same content and was written at
    the same level with nothing to copy: every member of the recompressed write
    has the size that level gives it, where a copied member would still have the
    size of the source archive.
    """
    target = tmp_path / "level.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.to_omex(target, compresslevel=1)

    directory = tmp_path / "content"
    built = tmp_path / "built.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.to_directory(directory)
    with Omex.from_directory(directory) as fresh:
        fresh.to_omex(built, compresslevel=1)

    def members(path: Path) -> dict[str, tuple[int, int, int]]:
        """Return the blobs of the data members, i.e., without the manifest."""
        return {
            name: blob for name, blob in _blobs(path).items() if name != "manifest.xml"
        }

    assert len(members(target)) == 4
    assert members(target) == members(built)
    assert members(target) != members(COMPMODELS)
    assert {method for method, _, _ in _blobs(target).values()} == {
        zipfile.ZIP_DEFLATED
    }


def test_a_changed_format_is_written_without_a_file_from_the_caller(
    tmp_path: Path,
) -> None:
    """A format or a master flag a caller assigned reaches the written manifest.

    The entries are the contract of the write: the content of such an entry is
    the one it has, the manifest of the archive is the one of `Omex`.
    """
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.manifest["./README.md"].format = EntryFormat.PLAIN
        omex.manifest["./models/omex_comp.xml"].master = True
        omex.to_omex(target)

    with Omex.from_omex(target) as result:
        assert result.manifest["./README.md"].format == EntryFormat.PLAIN.value
        assert result.manifest["./models/omex_comp.xml"].master is True
    with zipfile.ZipFile(COMPMODELS) as source, zipfile.ZipFile(target) as written:
        assert written.read("README.md") == source.read("README.md")


def _content_locations(omex: Omex) -> list[str]:
    """Get the locations of an archive which have content, i.e., a file."""
    return [
        entry.location
        for entry in omex.manifest.entries
        if entry.location not in {".", "./manifest.xml"}
    ]


def test_get_path_from_several_threads_extracts_every_entry() -> None:
    """One `Omex` is read from eight threads, as one could be before the swap.

    The core gives access to one archive to one thread at a time and refuses a
    second one; `Omex` serializes the extractions with a lock of the instance,
    so the property the pre-swap `get_path`, a dict lookup plus a path join,
    had by construction is kept. Without the lock most of these calls fail with
    the `ArchiveBusyError` of the binding.
    """
    with Omex.from_omex(ICGB21FR) as omex, Omex.from_omex(ICGB21FR) as reference:
        locations = _content_locations(omex)
        assert len(locations) == 21

        with ThreadPoolExecutor(max_workers=8) as pool:
            paths = list(pool.map(omex.get_path, locations))

        assert len(paths) == len(locations)
        for location, path in zip(locations, paths, strict=True):
            assert path.is_file(), location
            # the bytes of the threaded extraction are the ones of a read which
            # extracts the same member alone
            assert path.read_bytes() == reference.get_path(location).read_bytes()


def test_get_path_races_a_write(tmp_path: Path) -> None:
    """Extracting entries in several threads while the archive is written works.

    `to_omex` reaches the same archive as `get_path`, so both hold the lock of
    the instance; the writes and the extractions happen one after the other
    instead of refusing each other.
    """
    targets = [tmp_path / f"out{i}.omex" for i in range(3)]
    with Omex.from_omex(ICGB21FR) as omex:
        locations = _content_locations(omex)
        reads: list[Future[Path]] = []
        writes: list[Future[None]] = []
        with ThreadPoolExecutor(max_workers=8) as pool:
            for index, location in enumerate(locations):
                reads.append(pool.submit(omex.get_path, location))
                if index % 7 == 0:
                    writes.append(pool.submit(omex.to_omex, targets[index // 7]))

            paths = [read.result() for read in reads]
            # a failing write raises here
            assert [write.result() for write in writes] == [None, None, None]

        assert all(path.is_file() for path in paths)

    for target in targets:
        with Omex.from_omex(target) as result:
            assert {entry.location for entry in result.manifest.entries} == set(
                ICGB21FR_LOCATIONS
            )


def test_a_removed_file_of_an_extracted_entry_is_not_written_from_the_archive(
    tmp_path: Path,
) -> None:
    """A caller who removes the file of an entry does not get the old content.

    Before the swap every member was extracted when the archive was read, so a
    removed file made the write raise. The archive the content was read from
    must not answer for a location the caller touched, otherwise a write
    silently restores content the caller got rid of.
    """
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        missing = omex.get_path("./README.md")
        missing.unlink()
        with pytest.raises(FileNotFoundError, match=r"README\.md") as error:
            omex.to_omex(target)

    # the file is named in the message and in `filename`, which is what a
    # caller needs to tell which entry went missing. `match` is on the message
    # of `open`, which names the file on every platform
    assert error.value.filename == str(missing)
    assert not target.exists()


def test_a_removed_file_of_an_added_entry_does_not_resurrect_the_original(
    tmp_path: Path,
) -> None:
    """A replacement whose file goes missing is not written from the archive.

    This is the case the fallback to the archive is dangerous in: the write
    would restore the content the caller replaced, without an error.
    """
    replacement = tmp_path / "README.md"
    replacement.write_text("replaced", encoding="utf-8")
    target = tmp_path / "out.omex"
    with Omex.from_omex(COMPMODELS) as omex:
        omex.add_entry(
            entry_path=replacement,
            entry=ManifestEntry(
                location="./README.md", format=EntryFormat.MARKDOWN, master=False
            ),
        )
        missing = omex.get_path("./README.md")
        missing.unlink()
        with pytest.raises(FileNotFoundError, match=r"README\.md") as error:
            omex.to_omex(target)

    assert error.value.filename == str(missing)
    assert not target.exists()


def test_to_directory_does_not_write_the_archive_content_of_a_removed_file(
    tmp_path: Path,
) -> None:
    """`to_directory` fails for a removed file instead of falling back.

    The error names the missing file on every platform: `shutil.copy2` copies
    through the `CopyFile2` API on windows, whose error names no file, so
    `Omex._extract` raises about the file itself.
    """
    with Omex.from_omex(COMPMODELS) as omex:
        missing = omex.get_path("./README.md")
        missing.unlink()
        with pytest.raises(FileNotFoundError, match=r"README\.md") as error:
            omex.to_directory(tmp_path / "out")

    assert error.value.filename == str(missing)


def test_is_omex_of_a_container_whose_manifest_is_named_with_a_prefix(
    tmp_path: Path,
) -> None:
    """`is_omex` normalizes the names of the container, as the core does.

    A container whose manifest member is stored as `./manifest.xml` is read by
    `from_omex`, so `is_omex` must not answer False for it: the two have to
    agree, because the documentation offers `is_omex` as the gate of `from_omex`.
    """
    omex_path = tmp_path / "prefixed.omex"
    with zipfile.ZipFile(omex_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("./manifest.xml", MANIFEST)
        zf.writestr("./a.txt", "hi")

    assert Omex.is_omex(omex_path) is True
    with Omex.from_omex(omex_path) as omex:
        assert [entry.location for entry in omex.manifest.entries] == [
            ".",
            "./manifest.xml",
            "./a.txt",
        ]


def _manifest_order(omex_path: Path) -> list[str]:
    """Return the locations of the `manifest.xml` of a container, in its order.

    Args:
        omex_path: path of the zip container

    Returns:
        The locations of the `content` elements, in document order.
    """
    import re

    with zipfile.ZipFile(omex_path) as zf:
        xml = zf.read("manifest.xml").decode("utf-8")
    return re.findall(r'location="([^"]+)"', xml)


def test_the_written_manifest_is_in_the_order_of_the_entries(tmp_path: Path) -> None:
    """A written archive lists its entries in the order the `Omex` holds them.

    `iCGB21FR.omex` is the case which tells the two orders apart: its manifest
    declares 8 entries and the container holds 22 members, so the entries the
    archive did not list are many and their container order is not their sorted
    order. The core writes the order of its own manifest unless it is told
    otherwise, which is what `write_archive` does.
    """
    omex = Omex.from_omex(DATA / "iCGB21FR.omex")
    expected = [entry.location for entry in omex.manifest.entries]
    target = tmp_path / "written.omex"
    omex.to_omex(target)

    assert _manifest_order(target) == expected
    # the members follow the manifest, so a reader walks them in that order too
    members = [name for name in _blobs(target) if not name.endswith("/")]
    assert members == [location[2:] for location in expected if location != "."]


def test_the_written_order_survives_a_round_trip(tmp_path: Path) -> None:
    """Reading a written archive gives the entries in the same order again."""
    first = tmp_path / "first.omex"
    Omex.from_omex(DATA / "iCGB21FR.omex").to_omex(first)
    second = tmp_path / "second.omex"
    omex = Omex.from_omex(first)
    locations = [entry.location for entry in omex.manifest.entries]
    omex.to_omex(second)

    assert _manifest_order(second) == locations
    assert _manifest_order(first) == _manifest_order(second)


def test_a_changed_format_keeps_the_member_as_it_is(tmp_path: Path) -> None:
    """Changing the metadata of an entry does not rewrite its content.

    The format and the master flag live in the manifest, not in the member, so
    an entry whose format changes keeps the compressed blob it has: the member
    is copied, not inflated and deflated again.
    """
    source = DATA / "BIOMD0000000001.omex"
    omex = Omex.from_omex(source)
    entry = next(
        e
        for e in omex.manifest.entries
        if e.location.endswith(".xml") and e.location != "./manifest.xml"
    )
    entry.format = EntryFormat.XML
    entry.master = not entry.master
    target = tmp_path / "changed.omex"
    omex.to_omex(target)

    name = entry.location[2:]
    assert _blobs(target)[name] == _blobs(source)[name]
    manifest = _manifest_order(target)
    assert entry.location in manifest
    with zipfile.ZipFile(target) as zf:
        xml = zf.read("manifest.xml").decode("utf-8")
    assert f'location="{entry.location}" format="{EntryFormat.XML.value}"' in xml


def test_a_changed_format_of_an_added_entry_keeps_its_bytes(tmp_path: Path) -> None:
    """The same holds for a member which was added in this session."""
    source = tmp_path / "added.txt"
    source.write_text("content", encoding="utf-8")
    omex = Omex()
    omex.add_entry(
        source, ManifestEntry(location="./added.txt", format=EntryFormat.TXT)
    )
    first = tmp_path / "first.omex"
    omex.to_omex(first)

    omex = Omex.from_omex(first)
    omex.manifest.entries[-1].master = True
    second = tmp_path / "second.omex"
    omex.to_omex(second)

    assert _blobs(second)["added.txt"] == _blobs(first)["added.txt"]


def test_to_omex_does_not_hold_the_archive_in_memory(tmp_path: Path) -> None:
    """The write streams into the file, so python never holds the archive.

    The members are incompressible, so the archive is about as large as they
    are, and large enough that holding it would show. What python allocates
    while the archive is written is the staging of the entries and the buffers
    of the core's call, not the archive.
    """
    source = tmp_path / "members"
    source.mkdir()
    block = random.randbytes(1 << 20)
    for index in range(8):
        (source / f"data{index}.bin").write_bytes(block)
    omex = Omex()
    for index in range(8):
        omex.add_entry(
            source / f"data{index}.bin",
            ManifestEntry(location=f"./data{index}.bin", format=EntryFormat.BIN),
        )
    target = tmp_path / "big.omex"

    tracemalloc.start()
    omex.to_omex(target)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    size = target.stat().st_size
    assert size > 8 * (1 << 20) // 2, size
    assert peak * 4 < size, (peak, size)
    assert Omex.is_omex(target)


def test_to_omex_raises_os_error_when_the_file_cannot_be_written(
    tmp_path: Path,
) -> None:
    """A sink which cannot take the bytes is an `OSError`, not a `ValueError`."""
    if os.name == "nt":  # a read only directory does not stop a write on windows
        pytest.skip("the mode of a directory does not refuse a write on windows")
    directory = tmp_path / "locked"
    directory.mkdir()
    directory.chmod(stat.S_IRUSR | stat.S_IXUSR)
    try:
        with Omex.from_omex(COMPMODELS) as omex:
            with pytest.raises(OSError) as error:
                omex.to_omex(directory / "out.omex")
            assert not isinstance(error.value, ValueError)
    finally:
        directory.chmod(stat.S_IRWXU)

    assert list(directory.iterdir()) == []
