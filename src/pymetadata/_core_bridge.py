"""Bridge between `pymetadata.omex` and the Rust core `pymetadata-core`.

This is the only module which imports `pymetadata_core`. It translates the core's
errors into the `ValueError` and `KeyError` the public API of `pymetadata.omex`
raises, derives the manifest entries `pymetadata` wants from an opened archive,
and applies the changes of an `Omex` to the archive when it is written.
"""

from __future__ import annotations

import logging
import re
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING

from pymetadata_core import Archive, OmexError

if TYPE_CHECKING:
    from pymetadata.omex import ManifestEntry

logger = logging.getLogger(__name__)

_MANIFEST = "./manifest.xml"
_ARCHIVE = "."
# the locations the core writes itself, they are never set or removed by hand
_DERIVED = frozenset({_ARCHIVE, _MANIFEST})


def _is_sedml(format: str) -> bool:
    """Return whether a format URI is a SED-ML format of any level and version.

    Args:
        format: the format URI

    Returns:
        True for a SED-ML format.
    """
    # imported here: `pymetadata.omex` imports this module
    from pymetadata.omex import ManifestEntry

    return ManifestEntry.is_format("sedml", format)


def _map_error(error: OmexError, *, opening: bool = False) -> ValueError:
    """Translate an error of the core into a `ValueError`.

    The message of the core starts with the kind of the failure and names the
    member (a location) for an unsupported method or a member over the inflate
    cap, and the password for a wrong or missing one; those are kept. A malformed
    archive is reported as one without a readable manifest, as the manifest is
    what makes a zip an archive.

    Args:
        error: the error of the core
        opening: whether the archive was being opened

    Returns:
        The `ValueError` to raise.
    """
    message = str(error)
    if message.startswith("malformed") and opening:
        return ValueError(f"Not an OMEX archive, no readable manifest.xml: {message}")
    # spell a member the way pymetadata spells a location
    message = re.sub(r'member "(?!\./)([^"]+)"', r'member "./\1"', message)
    return ValueError(message)


def open_archive(data: bytes, password: bytes | None) -> Archive:
    """Open the bytes of an `.omex` file.

    Args:
        data: the bytes of the archive
        password: the password of a ZipCrypto protected archive, or None

    Returns:
        The archive.

    Raises:
        ValueError: if the data is not a zip or has no readable `manifest.xml`
            (the message names the manifest), if the password is wrong or missing
            (the message names the password). An unsupported compression method
            and a member over the inflate cap are refused when the bytes of a
            member are read, see `materialize`, except for `manifest.xml`, which
            is read here and named as `./manifest.xml`. The declared entries of the
            archive are read here and fixed; they do not change under `set_entry`
            or `remove_entry`.
    """
    try:
        return Archive.from_bytes(data, password)
    except OmexError as error:
        raise _map_error(error, opening=True) from error


def entries_for_archive(
    archive: Archive, guess_format: Callable[[str, bytes], str]
) -> list[dict[str, str | bool]]:
    """Return the manifest entries of an archive, in the order `pymetadata` keeps.

    These are the entries which the container's `manifest.xml` declared and
    which have bytes, in the order of the manifest, followed by the members no
    declared entry lists, sorted by location, with the format guessed and SED-ML
    as master. `archive.entries` is not used: it holds the entries the core
    invents for the unlisted members in the order of the container. The archive
    itself (`.`) and `./manifest.xml` are not included, `Manifest` holds them.

    An unlisted member with an `.xml` suffix is inflated when this is called,
    because its format is classified from its first bytes and the core has no
    partial read. The core caches those bytes, so a later `materialize` of that
    member does not inflate it a second time. Every other member is described
    from the central directory alone, nothing is inflated. This is still less
    work than `from_omex` before the swap, which extracted every member.
    `declared_entries` is fixed when the archive is opened, so the declared half
    is the same after a `set_entry` or a `remove_entry`.

    Args:
        archive: the opened archive
        guess_format: classifier of an unlisted member, called with the lower
            case suffix without the dot and the first 256 bytes for `xml` (empty
            for every other suffix); it returns the format URI.

    Returns:
        One dict per entry with the keys `location`, `format` and `master`.
    """
    entries: list[dict[str, str | bool]] = []
    declared: set[str] = set()
    for location, format, master in archive.declared_entries:
        declared.add(location)
        if location in _DERIVED:
            continue
        if not archive.has_bytes(location):
            logger.warning("Entry in manifest.xml without a file: '%s'", location)
            continue
        entries.append({"location": location, "format": format, "master": master})

    unlisted = sorted(
        location
        for location, _, _, _ in archive.members
        if location not in declared and location not in _DERIVED
    )
    for location in unlisted:
        logger.warning("Entry with location missing in manifest.xml: '%s'", location)
        suffix = Path(location).suffix[1:].lower()
        head = archive.entry_bytes(location)[:256] if suffix == "xml" else b""
        format = guess_format(suffix, head)
        entries.append(
            {"location": location, "format": format, "master": _is_sedml(format)}
        )
    return entries


def materialize(archive: Archive, location: str, target: Path) -> None:
    """Write the bytes of one entry to a file.

    Args:
        archive: the opened archive
        location: the location of the entry
        target: the file to write, its parents are created

    Raises:
        KeyError: if the archive has no bytes for the location, which holds for
            a declared entry no member provides and for the derived locations `.`
            and `./manifest.xml`. `Omex` owns the bytes of `./manifest.xml`
            through `Manifest.to_manifest_xml`, not the bridge.
        ValueError: if the member cannot be read. An unsupported compression
            method and a member over the inflate cap are refused here, when the
            bytes are read, not when the archive is opened (`manifest.xml` is
            the exception); the message names the member as `./location`.
    """
    if location in _DERIVED:
        raise KeyError(location)
    try:
        data = archive.entry_bytes(location)
    except OmexError as error:
        if str(error).startswith("not found"):
            raise KeyError(location) from error
        raise _map_error(error) from error
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def write_archive(
    archive: Archive,
    entries: list[ManifestEntry],
    changed: dict[str, Path],
    removed: set[str],
) -> bytes:
    """Apply the changes of an `Omex` to the archive and write it.

    Every entry of `entries` is the manifest of the result: a location of the
    archive which is not in `entries` is removed, a location in `changed` is set
    from the file, and an entry whose format or master flag differ from the
    archive is set again with its current bytes. The unchanged rest is copied by
    the core as the compressed blobs they are.

    A location in `removed` which the archive does not have is ignored
    (`remove_entry` returns false instead of raising), so adding and then
    removing an entry before a write is safe.

    The core serializes `manifest.xml` from the entries set into the archive, so
    the entries are the contract. `Manifest.to_manifest_xml` remains the
    authority for `to_directory`.

    Args:
        archive: the archive the `Omex` was opened from, or an empty one
        entries: the manifest entries of the `Omex`
        changed: file of every location whose content was added or replaced
        removed: locations removed since the archive was opened

    Returns:
        The bytes of the archive.

    Raises:
        ValueError: if the core refuses an entry or a member cannot be read.
    """
    wanted = {e.location: e for e in entries if e.location not in _DERIVED}
    try:
        for location in sorted(removed | set(_locations(archive) - set(wanted))):
            if location not in _DERIVED:
                archive.remove_entry(location)
        current = {loc: (fmt, master) for loc, fmt, master in archive.entries}
        for location, entry in wanted.items():
            format, master = str(entry.format), bool(entry.master)
            if location in changed:
                archive.set_entry(
                    location, format, master, changed[location].read_bytes()
                )
            elif current.get(location) != (format, master) and archive.has_bytes(
                location
            ):
                archive.set_entry(
                    location, format, master, archive.entry_bytes(location)
                )
        data = archive.to_bytes()
    except OmexError as error:
        raise _map_error(error) from error
    return data


def _locations(archive: Archive) -> set[str]:
    """Return the locations the archive holds as entries.

    Args:
        archive: the archive

    Returns:
        The locations of `archive.entries`.
    """
    return {location for location, _, _ in archive.entries}
