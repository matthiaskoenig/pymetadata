"""Tests of the bridge to `pymetadata-core`."""

import io
import shutil
import subprocess
import zipfile
from pathlib import Path
from typing import Any, cast

import pytest
from pymetadata_core import Archive, ArchiveBusyError

from pymetadata._core_bridge import (
    HEAD_SIZE,
    ConcurrentUseError,
    PasswordError,
    _head_of,
    declares_manifest,
    entries_for_archive,
    has_bytes,
    materialize,
    open_archive,
    write_archive,
)
from pymetadata.omex import (
    EntryFormat,
    ManifestEntry,
    Omex,
    _format_from_suffix_and_head,
)

DATA = Path(__file__).parent / "data" / "omex"
MANIFEST = (
    '<?xml version="1.0"?><omexManifest '
    'xmlns="http://identifiers.org/combine.specifications/omex-manifest">'
    '<content location="." '
    'format="http://identifiers.org/combine.specifications/omex"/>'
    "</omexManifest>"
)


def _open(name: str) -> Archive:
    """Open a fixture archive."""
    return open_archive((DATA / f"{name}.omex").read_bytes(), None)


def _zip(members: dict[str, bytes], method: int = zipfile.ZIP_DEFLATED) -> bytes:
    """Build a zip with the given members."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", method) as zf:
        for name, content in members.items():
            zf.writestr(name, content)
    return buffer.getvalue()


def test_a_zip_without_a_manifest_is_a_value_error_naming_the_manifest() -> None:
    """A zip which holds no `manifest.xml` is no archive."""
    with pytest.raises(ValueError, match="manifest"):
        open_archive(_zip({"a.txt": b"x"}), None)


def test_data_which_is_not_a_zip_is_a_value_error_naming_the_manifest() -> None:
    """Bytes which are no zip have no manifest either."""
    with pytest.raises(ValueError, match="manifest"):
        open_archive(b"not a zip at all, but long enough", None)


def _encrypted(tmp_path: Path) -> bytes:
    """Build a ZipCrypto protected archive with the `zip` tool."""
    (tmp_path / "manifest.xml").write_text(MANIFEST)
    (tmp_path / "a.txt").write_text("hi")
    out = tmp_path / "enc.omex"
    subprocess.run(
        ["zip", "-q", "-P", "secret", str(out), "manifest.xml", "a.txt"],
        cwd=tmp_path,
        check=True,
    )
    return out.read_bytes()


@pytest.mark.skipif(
    shutil.which("zip") is None,
    reason="needs the zip tool to make a ZipCrypto archive, absent on Windows",
)
def test_a_wrong_password_is_a_value_error_naming_the_password(tmp_path: Path) -> None:
    """A wrong or a missing password is reported as such."""
    data = _encrypted(tmp_path)
    for password in (None, b"wrong"):
        with pytest.raises(ValueError, match="password"):
            open_archive(data, password)
    assert open_archive(data, b"secret").has_bytes("./a.txt")


@pytest.mark.skipif(
    shutil.which("zip") is None,
    reason="needs the zip tool to make a ZipCrypto archive, absent on Windows",
)
def test_a_refused_password_is_told_apart_from_a_manifest_which_is_absent(
    tmp_path: Path,
) -> None:
    """A protected `manifest.xml` is a member, a missing one is not.

    A caller which only asks whether a file is an archive reads the one as a
    yes and the other as a no, see `Omex.is_omex`.
    """
    data = _encrypted(tmp_path)
    for password in (None, b"wrong"):
        with pytest.raises(PasswordError):
            open_archive(data, password)

    with pytest.raises(ValueError, match="manifest") as error:
        open_archive(_zip({"a.txt": b"x"}), None)
    assert not isinstance(error.value, PasswordError)


def test_entries_drop_a_manifest_entry_without_bytes() -> None:
    """iCGB21FR lists ./iCGB21FR_memote.html, which no member provides."""
    archive = _open("iCGB21FR")
    locations = [
        e["location"]
        for e in entries_for_archive(archive, _format_from_suffix_and_head)
    ]
    assert "./iCGB21FR_memote.html" not in locations
    assert "." not in locations
    assert "./manifest.xml" not in locations


@pytest.mark.parametrize(
    ("name", "count"),
    [
        ("iCGB21FR", 23),
        ("BIOMD0000000001", 16),
        ("CombineArchiveShowCase", 22),
        ("CompModels", 6),
    ],
)
def test_entries_count(name: str, count: int) -> None:
    """The two entries `Manifest` holds make the count `pymetadata` reports."""
    entries = entries_for_archive(_open(name), _format_from_suffix_and_head)
    assert len(entries) + 2 == count
    assert len({e["location"] for e in entries}) == len(entries)


def test_entries_append_the_unlisted_members_sorted() -> None:
    """The 16 unlisted members of iCGB21FR follow the listed ones, sorted."""
    archive = _open("iCGB21FR")
    declared = [loc for loc, _, _ in archive.declared_entries]
    entries = entries_for_archive(archive, _format_from_suffix_and_head)
    locations = [str(e["location"]) for e in entries]
    # a declared format is the one of the manifest, not a guess
    sbml = next(e for e in entries if e["location"] == "./iCGB21FR.xml")
    assert sbml["format"] == (
        "https://identifiers.org/combine.specifications/sbml.level-3.version-1"
    )
    listed = [loc for loc in locations if loc in declared]
    unlisted = locations[len(listed) :]
    assert locations[: len(listed)] == listed
    assert listed == [loc for loc in declared if loc in listed]
    assert len(unlisted) == 16
    assert unlisted == sorted(unlisted)
    assert not set(unlisted) & set(declared)


def test_entries_guess_the_format_of_an_unlisted_member() -> None:
    """BIOMD0000000001 has metadata.rdf, which the manifest does not list."""
    by_location = {
        e["location"]: e
        for e in entries_for_archive(
            _open("BIOMD0000000001"), _format_from_suffix_and_head
        )
    }
    entry = by_location["./metadata.rdf"]
    assert entry["format"] == Omex.lookup_format("rdf")
    assert entry["master"] is False


def test_an_unlisted_sedml_member_is_master() -> None:
    """A SED-ML file the manifest does not list is the entry point."""
    archive = open_archive(
        _zip(
            {
                "manifest.xml": MANIFEST.encode(),
                "study.xml": b'<?xml version="1.0"?><sedML level="1" version="3"/>',
            }
        ),
        None,
    )
    (entry,) = entries_for_archive(archive, _format_from_suffix_and_head)
    assert entry["location"] == "./study.xml"
    assert ManifestEntry.is_format("sedml", str(entry["format"]))
    assert entry["master"] is True


def test_materialize_writes_the_bytes_and_makes_the_parents(tmp_path: Path) -> None:
    """The bytes of the entry land in the target, below new directories."""
    archive = _open("BIOMD0000000001")
    target = tmp_path / "a" / "b" / "rdf.xml"
    materialize(archive, "./metadata.rdf", target)
    assert target.read_bytes() == archive.entry_bytes("./metadata.rdf")


def test_materialize_raises_key_error_for_a_location_without_bytes(
    tmp_path: Path,
) -> None:
    """Unknown, declared without a member and derived locations have no bytes."""
    archive = _open("iCGB21FR")
    for location in (
        "./nope.txt",
        "./iCGB21FR_memote.html",
        ".",
        "./manifest.xml",
    ):
        with pytest.raises(KeyError):
            materialize(archive, location, tmp_path / "x")
    assert not (tmp_path / "x").exists()


def _patch_method(data: bytes, name: bytes, method: int) -> bytes:
    """Set the compression method of one member in both of its headers."""
    out = bytearray(data)
    local = bytes(out).find(b"PK\x03\x04")
    while local != -1:
        n = int.from_bytes(out[local + 26 : local + 28], "little")
        if bytes(out[local + 30 : local + 30 + n]) == name:
            out[local + 8 : local + 10] = method.to_bytes(2, "little")
        local = bytes(out).find(b"PK\x03\x04", local + 4)
    central = bytes(out).find(b"PK\x01\x02")
    while central != -1:
        n = int.from_bytes(out[central + 28 : central + 30], "little")
        if bytes(out[central + 46 : central + 46 + n]) == name:
            out[central + 10 : central + 12] = method.to_bytes(2, "little")
        central = bytes(out).find(b"PK\x01\x02", central + 4)
    return bytes(out)


def _unsupported(method: int) -> bytes:
    """Build an archive whose member `b.txt` uses a method the core lacks."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        zf.writestr("b.txt", "x" * 100, compress_type=zipfile.ZIP_BZIP2)
    return _patch_method(buffer.getvalue(), b"b.txt", method)


@pytest.mark.parametrize("method", [12, 99])
def test_a_member_with_an_unsupported_method_is_a_value_error_naming_the_location(
    method: int, tmp_path: Path
) -> None:
    """A bzip2 member and an AES member: the message names the location."""
    data = _unsupported(method)
    with pytest.raises(ValueError, match=r"\./b\.txt"):
        materialize(open_archive(data, None), "./b.txt", tmp_path / "b.txt")


def test_a_member_over_the_inflate_cap_is_a_value_error_naming_the_location(
    tmp_path: Path,
) -> None:
    """The core refuses to inflate a member above 1 GiB, a lie of the header."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        with zf.open("big.bin", "w", force_zip64=True) as f:
            block = bytes(1 << 24)
            for _ in range(65):
                f.write(block)
    archive = open_archive(buffer.getvalue(), None)
    with pytest.raises(ValueError, match=r"\./big\.bin"):
        materialize(archive, "./big.bin", tmp_path / "big.bin")
    assert not (tmp_path / "big.bin").exists()


def test_members_carry_the_method_so_the_compression_warning_survives() -> None:
    """A stored and a deflated member are told apart by the method."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        zf.writestr("s.txt", "x", compress_type=zipfile.ZIP_STORED)
        zf.writestr("d.txt", "x" * 100)
    methods = {
        location: method
        for location, _, _, method in open_archive(buffer.getvalue(), None).members
    }
    assert methods["./s.txt"] == 0
    assert methods["./d.txt"] == 8
    assert {m for *_, m in _open("CombineArchiveShowCase").members} <= {0, 8}


def test_write_archive_applies_removals_changes_and_the_manifest(
    tmp_path: Path,
) -> None:
    """Removed entries vanish, changed files replace bytes, new entries appear."""
    archive = _open("BIOMD0000000001")
    entries = [
        ManifestEntry(**e)  # ty: ignore[invalid-argument-type]
        for e in entries_for_archive(archive, _format_from_suffix_and_head)
    ]
    removed = entries.pop(-1)
    new_file = tmp_path / "new.txt"
    new_file.write_bytes(b"new")
    entries.append(
        ManifestEntry(location="./new.txt", format=EntryFormat.TXT, master=False)
    )
    data = write_archive(archive, entries, {"./new.txt": new_file})
    result = open_archive(data, None)
    assert result.entry_bytes("./new.txt") == b"new"
    assert not result.has_bytes(removed.location)
    assert {e.location for e in entries} <= {
        str(e["location"])
        for e in entries_for_archive(result, _format_from_suffix_and_head)
    }


def test_write_archive_without_an_archive_writes_the_files_alone(
    tmp_path: Path,
) -> None:
    """An `Omex` which was built by hand has no archive to copy from."""
    source = tmp_path / "model.xml"
    source.write_bytes(b"<sbml/>")
    entries = [
        ManifestEntry(location=".", format=EntryFormat.OMEX),
        ManifestEntry(location="./manifest.xml", format=EntryFormat.OMEX_MANIFEST),
        ManifestEntry(location="./model.xml", format=EntryFormat.SBML_L3V2),
    ]
    data = write_archive(None, entries, {"./model.xml": source})
    result = open_archive(data, None)
    assert result.entry_bytes("./model.xml") == b"<sbml/>"
    assert [
        e["location"] for e in entries_for_archive(result, _format_from_suffix_and_head)
    ] == ["./model.xml"]


def test_write_archive_raises_file_not_found_for_a_file_which_is_gone(
    tmp_path: Path,
) -> None:
    """A manifest entry whose file does not exist is an error, not an empty member."""
    entries = [ManifestEntry(location="./gone.txt", format=EntryFormat.TXT)]
    with pytest.raises(FileNotFoundError):
        write_archive(None, entries, {"./gone.txt": tmp_path / "gone.txt"})


def test_write_archive_refuses_a_level_outside_of_the_range() -> None:
    """The core checks the deflate level, the bridge reports it as a `ValueError`."""
    with pytest.raises(ValueError, match="level"):
        write_archive(None, [], {}, recompress=True, level=10)


def test_has_bytes_is_false_for_a_location_the_archive_has_no_content_for() -> None:
    """A dangling entry, a derived location and a location nothing can normalize."""
    archive = _open("iCGB21FR")
    assert has_bytes(archive, "./iCGB21FR.xml") is True
    assert has_bytes(archive, "./iCGB21FR_memote.html") is False
    assert has_bytes(archive, "./manifest.xml") is False
    assert has_bytes(archive, "../outside.txt") is False


class _BusyArchive:
    """An archive which another thread holds, as the binding reports it.

    Every attribute the bridge asks for raises the `ArchiveBusyError` of the
    core. The refusal of the real core needs a second thread inside one of its
    calls, which cannot be provoked deterministically from python, while the
    translation of that refusal can be.
    """

    def __getattr__(self, name: str) -> Any:
        """Refuse the attribute the bridge asks for.

        Args:
            name: name of the attribute

        Returns:
            Nothing, every access raises.

        Raises:
            ArchiveBusyError: always, as the core does for an archive in use.
        """
        raise ArchiveBusyError(
            f"this Archive is already in use by another thread ('{name}')"
        )


def _busy() -> Archive:
    """Get a stand-in for an archive which another thread holds."""
    return cast("Archive", _BusyArchive())


def test_concurrent_use_error_is_a_runtime_error() -> None:
    """Not a `ValueError`: the values of the caller are fine, the moment is not."""
    assert issubclass(ConcurrentUseError, RuntimeError)
    assert not issubclass(ConcurrentUseError, ValueError)


def test_entries_for_archive_of_a_busy_archive_raises_concurrent_use() -> None:
    """The busy error of the core does not reach the caller as it is."""
    with pytest.raises(ConcurrentUseError, match="concurrently"):
        entries_for_archive(_busy(), _format_from_suffix_and_head)


def test_materialize_of_a_busy_archive_raises_concurrent_use(tmp_path: Path) -> None:
    """A busy archive is not a member which cannot be read."""
    with pytest.raises(ConcurrentUseError, match="concurrently"):
        materialize(_busy(), "./a.txt", tmp_path / "a.txt")


def test_has_bytes_of_a_busy_archive_raises_instead_of_answering_false() -> None:
    """A busy archive is not an archive without the bytes of the location."""
    with pytest.raises(ConcurrentUseError, match="concurrently"):
        has_bytes(_busy(), "./a.txt")


def test_write_archive_of_a_busy_archive_raises_concurrent_use() -> None:
    """The write translates the busy error as well."""
    entries = [ManifestEntry(location="./a.txt", format=EntryFormat.TXT)]
    with pytest.raises(ConcurrentUseError, match="concurrently"):
        write_archive(_busy(), entries, {})


class _HeadOnly:
    """An archive which serves a head and fails if the whole member is read."""

    def __init__(self, head: bytes) -> None:
        """Remember the head to serve and record the calls.

        Args:
            head: the bytes to answer a head with
        """
        self.head_bytes = head
        self.limits: list[int] = []

    def head(self, location: str, limit: int) -> bytes:
        """Answer the head, recording the limit it was asked with.

        Args:
            location: the location of the member
            limit: how many bytes the caller wants

        Returns:
            The head, cut to the limit.
        """
        self.limits.append(limit)
        return self.head_bytes[:limit]

    def entry_bytes(self, location: str) -> bytes:
        """Fail: the format is told from a head, not from the whole member.

        Args:
            location: the location of the member

        Raises:
            AssertionError: always, this must not be called
        """
        raise AssertionError(f"the whole member was inflated for '{location}'")


def test_the_format_is_guessed_from_a_head_not_from_the_whole_member() -> None:
    """`_head_of` reads a bounded head, where it used to inflate everything."""
    archive = _HeadOnly(
        b'<?xml version="1.0"?><sbml level="3" version="1">' + b"x" * 4096
    )
    head = _head_of(cast(Archive, archive), "./model.xml", "xml")

    assert archive.limits == [HEAD_SIZE]
    assert len(head) == HEAD_SIZE
    assert ManifestEntry.is_format("sbml", _format_from_suffix_and_head("xml", head))


def test_no_head_is_read_for_a_suffix_which_does_not_need_one() -> None:
    """A suffix which decides the format alone costs no read at all."""
    archive = _HeadOnly(b"ignored")
    assert _head_of(cast(Archive, archive), "./table.tsv", "tsv") == b""
    assert archive.limits == []


def test_the_format_of_a_huge_unlisted_xml_member_is_read_from_its_head(
    tmp_path: Path,
) -> None:
    """A member too large to inflate still has a head, so it is classified.

    The core refuses to inflate a member above its 1 GiB cap, which is what
    `materialize` reports for one. A head is bounded by its own limit, so the
    cap does not apply to it: the format of such a member comes from its
    content, where before the whole member had to be inflated for it and the
    suffix was all that was left.
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.xml", MANIFEST)
        with zf.open("huge.xml", "w", force_zip64=True) as f:
            f.write(b'<?xml version="1.0"?><sbml level="3" version="1">')
            block = bytes(1 << 24)
            for _ in range(65):
                f.write(block)
    archive = open_archive(buffer.getvalue(), None)

    (entry,) = entries_for_archive(archive, _format_from_suffix_and_head)
    assert entry["location"] == "./huge.xml"
    assert ManifestEntry.is_format("sbml", str(entry["format"]))
    # the member itself is still beyond the cap of the reader
    with pytest.raises(ValueError, match=r"\./huge\.xml"):
        materialize(archive, "./huge.xml", tmp_path / "huge.xml")


def test_declares_manifest_answers_from_the_structure(tmp_path: Path) -> None:
    """The probe recognizes an archive without reading a member of it."""
    assert declares_manifest(DATA / "CompModels.omex") is True

    plain = tmp_path / "plain.txt"
    plain.write_text("not a zip at all, but long enough", encoding="utf-8")
    assert declares_manifest(plain) is False

    without = tmp_path / "without.zip"
    without.write_bytes(_zip({"a.txt": b"x"}))
    assert declares_manifest(without) is False


@pytest.mark.skipif(
    shutil.which("zip") is None,
    reason="the `zip` tool builds the ZipCrypto fixture",
)
def test_declares_manifest_of_an_archive_it_cannot_open(tmp_path: Path) -> None:
    """An encrypted archive is an archive: its manifest is declared."""
    encrypted = tmp_path / "enc.omex"
    encrypted.write_bytes(_encrypted(tmp_path))

    assert declares_manifest(encrypted) is True
    with pytest.raises(PasswordError):
        open_archive(encrypted.read_bytes(), None)


def test_declares_manifest_raises_for_a_file_it_cannot_read(tmp_path: Path) -> None:
    """Being unable to read a file is no answer about its content."""
    with pytest.raises(OSError):
        declares_manifest(tmp_path / "missing.omex")
