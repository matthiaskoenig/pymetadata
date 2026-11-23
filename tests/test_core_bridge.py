"""Tests of the bridge to `pymetadata-core`."""

import io
import shutil
import subprocess
import zipfile
from pathlib import Path

import pytest
from pymetadata_core import Archive

from pymetadata._core_bridge import (
    PasswordError,
    entries_for_archive,
    materialize,
    open_archive,
    write_archive,
)
from pymetadata.omex import (
    EntryFormat,
    ManifestEntry,
    Omex,
    format_from_suffix_and_head,
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
        e["location"] for e in entries_for_archive(archive, format_from_suffix_and_head)
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
    entries = entries_for_archive(_open(name), format_from_suffix_and_head)
    assert len(entries) + 2 == count
    assert len({e["location"] for e in entries}) == len(entries)


def test_entries_append_the_unlisted_members_sorted() -> None:
    """The 16 unlisted members of iCGB21FR follow the listed ones, sorted."""
    archive = _open("iCGB21FR")
    declared = [loc for loc, _, _ in archive.declared_entries]
    entries = entries_for_archive(archive, format_from_suffix_and_head)
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
            _open("BIOMD0000000001"), format_from_suffix_and_head
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
    (entry,) = entries_for_archive(archive, format_from_suffix_and_head)
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
        for e in entries_for_archive(archive, format_from_suffix_and_head)
    ]
    removed = entries.pop(-1)
    new_file = tmp_path / "new.txt"
    new_file.write_bytes(b"new")
    entries.append(
        ManifestEntry(location="./new.txt", format=EntryFormat.TXT, master=False)
    )
    data = write_archive(archive, entries, {"./new.txt": new_file}, {removed.location})
    result = open_archive(data, None)
    assert result.entry_bytes("./new.txt") == b"new"
    assert not result.has_bytes(removed.location)
    assert {e.location for e in entries} <= {
        str(e["location"])
        for e in entries_for_archive(result, format_from_suffix_and_head)
    }
