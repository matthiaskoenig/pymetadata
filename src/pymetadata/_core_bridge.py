"""Bridge between `pymetadata.omex` and the Rust core `pymetadata-core`.

This is the only module which imports `pymetadata_core`. It translates the core's
errors into the `ValueError` and `KeyError` the public API of `pymetadata.omex`
raises, and the refusal of an archive which another thread holds into
`ConcurrentUseError`; it derives the manifest entries `pymetadata` wants from an
opened archive, and applies the changes of an `Omex` to the archive when it is
written.
"""

from __future__ import annotations

import logging
import re
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING

from pymetadata_core import (
    Archive,
    ArchiveBusyError,
    MalformedError,
    NotFoundError,
    OmexError,
    has_manifest,
)
from pymetadata_core import PasswordError as CorePasswordError

if TYPE_CHECKING:
    from pymetadata.omex import ManifestEntry

logger = logging.getLogger(__name__)

#: the normalized location of the manifest of an archive; `pymetadata.omex`
#: shares this one definition
MANIFEST_LOCATION = "./manifest.xml"
_ARCHIVE = "."
#: the locations the core writes itself, they are never set or removed by hand and
#: hold no file of their own; `pymetadata.omex` shares this one definition
DERIVED_LOCATIONS = frozenset({_ARCHIVE, MANIFEST_LOCATION})


#: how many bytes of a member the format is guessed from; an XML declaration and
#: the root element of an SBML, SED-ML or CellML document fit in them
HEAD_SIZE = 256


class PasswordError(ValueError):
    """A member of an archive which the given password does not open.

    A subclass of `ValueError`, so code which catches the `ValueError` of the
    bridge keeps working. It is raised for a password which is wrong and for a
    password which is missing, and it proves that the member exists. A caller
    can tell it from a container which has no manifest at all, but
    `Omex.is_omex` does not need to: it asks about the structure of the zip
    and never reads a member.
    """


class ConcurrentUseError(RuntimeError):
    """One archive used by two threads at the same time.

    The core gives access to one archive to one thread at a time and refuses a
    second one instead of waiting. `Omex` serializes the calls of its own
    methods, so one `Omex` can be used from several threads; this error is the
    backstop for an archive which is shared in another way, e.g., for two
    `Omex` instances built around the same `Archive` object.

    A `RuntimeError`, not a `ValueError`: nothing is wrong with the values the
    caller passed, the call came at the wrong moment and can be repeated.

    It cannot be raised by `open_archive`, which builds a new archive no other
    thread can hold yet.
    """


def _busy_error(error: ArchiveBusyError) -> ConcurrentUseError:
    """Translate the busy error of the core into a `ConcurrentUseError`.

    Args:
        error: the error of the core

    Returns:
        The `ConcurrentUseError` to raise.
    """
    return ConcurrentUseError(
        f"The archive is used by another thread, one archive cannot be read or "
        f"written concurrently: {error}"
    )


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

    A refusal over a password becomes a `PasswordError`, so that a caller can
    tell a member it may not read from a member which is not there. The kind of
    a failure is the class the core raises, not the start of its message: since
    `pymetadata-core` 0.3.0 every kind has a class of its own, so nothing here
    depends on the wording. The message is still passed on, because it names
    the member and the password, which the class does not.

    Args:
        error: the error of the core
        opening: whether the archive was being opened

    Returns:
        The `ValueError` to raise, a `PasswordError` for a refused password.
    """
    message = str(error)
    if isinstance(error, MalformedError) and opening:
        return ValueError(f"Not an OMEX archive, no readable manifest.xml: {message}")
    # spell a member the way pymetadata spells a location
    message = re.sub(r'member "(?!\./)([^"]+)"', r'member "./\1"', message)
    if isinstance(error, CorePasswordError):
        return PasswordError(message)
    return ValueError(message)


def open_archive(data: bytes, password: bytes | None) -> Archive:
    """Open the bytes of an `.omex` file.

    Args:
        data: the bytes of the archive
        password: the password of a ZipCrypto protected archive, or None

    Returns:
        The archive.

    Raises:
        PasswordError: if the password is wrong or missing, which proves that
            `manifest.xml` is a member of the container.
        ValueError: if the data is not a zip or has no readable `manifest.xml`
            (the message names the manifest). An unsupported compression method
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

    A member whose bytes the core refuses, e.g. one compressed with an
    unsupported method or one over the inflate cap, does not make this fail: the
    format is classified from the suffix alone, which is all the information
    there is for a member nothing can read, and the refusal reaches the caller
    when the bytes are asked for, see `materialize`.

    Args:
        archive: the opened archive
        guess_format: classifier of an unlisted member, called with the lower
            case suffix without the dot and the first 256 bytes for `xml` (empty
            for every other suffix); it returns the format URI.

    Returns:
        One dict per entry with the keys `location`, `format` and `master`.

    Raises:
        ConcurrentUseError: if another thread uses the same archive.
    """
    entries: list[dict[str, str | bool]] = []
    declared: set[str] = set()
    try:
        for location, format, master in archive.declared_entries:
            declared.add(location)
            if location in DERIVED_LOCATIONS:
                continue
            if not archive.has_bytes(location):
                logger.warning("Entry in manifest.xml without a file: '%s'", location)
                continue
            entries.append({"location": location, "format": format, "master": master})

        unlisted = sorted(
            location
            for location, _, _, _ in archive.members
            if location not in declared and location not in DERIVED_LOCATIONS
        )
        for location in unlisted:
            logger.warning(
                "Entry with location missing in manifest.xml: '%s'", location
            )
            suffix = Path(location).suffix[1:].lower()
            format = guess_format(suffix, _head_of(archive, location, suffix))
            entries.append(
                {"location": location, "format": format, "master": _is_sedml(format)}
            )
    except ArchiveBusyError as error:
        raise _busy_error(error) from error
    return entries


def _head_of(archive: Archive, location: str, suffix: str) -> bytes:
    """Return the first bytes of a member, for the suffixes which need them.

    The bytes of a member the core refuses cannot be read, here no more than
    anywhere else; the refusal is logged and no head is returned, so that an
    archive with such a member can still be read. Only the classification of
    that one member is less precise, and its refusal reaches the caller when
    its bytes are asked for.

    Args:
        archive: the opened archive
        location: the location of the member
        suffix: the lower case suffix of the location, without the dot

    Returns:
        The first `HEAD_SIZE` bytes of the member for an `xml` suffix, nothing
        for every other suffix and for a member which cannot be read.

    Raises:
        ArchiveBusyError: if another thread uses the same archive; the caller
            translates it, a busy archive is not a member which cannot be read.
    """
    if suffix != "xml":
        return b""
    try:
        # the head stops after `HEAD_SIZE` bytes, where `entry_bytes` would
        # inflate the whole member to look at its first bytes
        return archive.head(location, HEAD_SIZE)
    except OmexError as error:
        logger.warning(
            "The format of '%s' is guessed from its suffix, its content cannot be "
            "read: %s",
            location,
            _map_error(error),
        )
        return b""


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
        ConcurrentUseError: if another thread uses the same archive.
    """
    if location in DERIVED_LOCATIONS:
        raise KeyError(location)
    try:
        data = archive.entry_bytes(location)
    except ArchiveBusyError as error:
        raise _busy_error(error) from error
    except NotFoundError as error:
        raise KeyError(location) from error
    except OmexError as error:
        raise _map_error(error) from error
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def has_bytes(archive: Archive, location: str) -> bool:
    """Return whether the archive holds the bytes of a location.

    Nothing is inflated: the question is whether the content of that location
    can be written without a file, which holds for a member of the container
    the archive was opened from and for a location which was set into it. It is
    false for the derived locations and for a declared entry no member provides.

    Args:
        archive: the archive
        location: the location of an entry

    Returns:
        True if the archive can write the content of the location by itself. A
        location the core cannot normalize, which a `ManifestEntry` cannot
        carry, is reported as one without bytes.

    Raises:
        ConcurrentUseError: if another thread uses the same archive. A busy
            archive is not an archive without the bytes, so this is raised
            instead of being answered with False.
    """
    try:
        return archive.has_bytes(location)
    except ArchiveBusyError as error:
        raise _busy_error(error) from error
    except OmexError:
        return False


def write_archive(
    archive: Archive | None,
    entries: list[ManifestEntry],
    files: dict[str, Path],
    *,
    recompress: bool = False,
    level: int = 9,
) -> bytes:
    """Apply the changes of an `Omex` to the archive and write it.

    Every entry of `entries` is the manifest of the result: a location of the
    archive which is not in `entries` is removed, a location in `files` is set
    from that file, and an entry whose format or master flag differ from the
    archive is set again with its current bytes. The rest is copied by the core
    as the compressed blobs they are, unless `recompress` asks for all of them
    to be deflated again.

    A removal is derived from `entries` alone, so a location which was removed
    and declared again keeps the member it has, and an entry can be added and
    removed again before a write without losing anything.

    The core serializes `manifest.xml` from the entries set into the archive, so
    the entries are the contract. `Manifest.to_manifest_xml` remains the
    authority for `to_directory`.

    `entries` is also the order of the result: its locations are laid into the
    archive in that order, so the written `manifest.xml` lists them as `Omex`
    holds them and the members follow that order, as they did before the swap.
    An entry whose format or master flag changed keeps its member: the manifest
    entry is set alone, without inflating and deflating content which does not
    change.

    Args:
        archive: the archive the `Omex` was opened from, or None for an archive
            which was built by hand and is written from its files alone. It is
            changed in place as the write proceeds, so a write is not free of
            side effects: a second write of the same `Omex` after further
            changes of its manifest can fail on a member whose bytes the
            archive no longer holds. The cause is that the first write already
            dropped the bytes of a removed member from the archive, so a
            location which was removed, written and then declared again has no
            content left and fails with the `FileNotFoundError` of its missing
            file. A write which repeats the same entries is unaffected
            and gives the same bytes again.
        entries: the manifest entries of the `Omex`
        files: the file of every location whose content is written from one
            instead of being copied from the archive
        recompress: deflate every member again, instead of copying the members
            which were not replaced
        level: the deflate level, 0 to 9, used with `recompress`

    Returns:
        The bytes of the archive.

    Raises:
        FileNotFoundError: if a file of `files` does not exist, which is what a
            manifest entry without content gives, as it did before the swap.
        ValueError: if the core refuses an entry, if `level` is outside of 0 to
            9 or if a member cannot be read, which includes an entry with
            neither a file in `files` nor bytes in the archive.
        ConcurrentUseError: if another thread uses the same archive.
    """
    target = _staged(archive, entries, files)
    try:
        data = target.to_bytes(recompress=recompress, level=level)
    except ArchiveBusyError as error:
        raise _busy_error(error) from error
    except OmexError as error:
        raise _map_error(error) from error
    return data


def write_archive_to_path(
    archive: Archive | None,
    entries: list[ManifestEntry],
    files: dict[str, Path],
    target_path: Path,
    *,
    recompress: bool = False,
    level: int = 9,
) -> int:
    """Apply the changes of an `Omex` to the archive and write it to a file.

    This is `write_archive` into a file: the core hands every member to the file
    as it produces it, so the memory a write needs is the largest member and not
    the whole archive. The file holds the bytes `write_archive` returns for the
    same `Omex`, so the two are the same write.

    Args:
        archive: the archive the `Omex` was opened from, or None, see
            `write_archive`, whose side effects on it are the ones described there
        entries: the manifest entries of the `Omex`, and the order of the result
        files: the file of every location whose content is written from one
        target_path: the file to write, created or truncated
        recompress: deflate every member again, instead of copying the members
            which were not replaced
        level: the deflate level, 0 to 9, used with `recompress`

    Returns:
        The number of bytes written.

    Raises:
        FileNotFoundError: if a file of `files` does not exist, as `write_archive`
            raises, which is what a manifest entry without content gives.
        ValueError: as `write_archive` raises, for the archive itself.
        OSError: if the file cannot be created or written. A write which fails
            part way leaves what it had written behind, so a caller which needs
            the file to be the archive or nothing writes to a temporary file and
            moves it, which is what `Omex.to_omex` does.
        ConcurrentUseError: if another thread uses the same archive.
    """
    target = _staged(archive, entries, files)
    try:
        return target.to_path(target_path, recompress=recompress, level=level)
    except ArchiveBusyError as error:
        raise _busy_error(error) from error
    except OmexError as error:
        raise _map_error(error) from error


def _staged(
    archive: Archive | None,
    entries: list[ManifestEntry],
    files: dict[str, Path],
) -> Archive:
    """Apply the entries and the files of an `Omex` to the archive it writes.

    The archive is changed in place and is the one to write afterwards; see
    `write_archive` for what the changes are and what they cost.

    Args:
        archive: the archive the `Omex` was opened from, or None for one which
            is written from its files alone
        entries: the manifest entries of the `Omex`, and the order of the result
        files: the file of every location whose content comes from one

    Returns:
        The archive to write.

    Raises:
        FileNotFoundError: if a file of `files` does not exist.
        ValueError: if the core refuses an entry or a member cannot be read.
        ConcurrentUseError: if another thread uses the same archive.
    """
    target = Archive() if archive is None else archive
    wanted = {e.location: e for e in entries if e.location not in DERIVED_LOCATIONS}
    try:
        for location in sorted(_locations(target) - set(wanted)):
            if location not in DERIVED_LOCATIONS:
                target.remove_entry(location)
        current = {loc: (fmt, master) for loc, fmt, master in target.entries}
        for location, entry in wanted.items():
            format, master = str(entry.format), bool(entry.master)
            path = files.get(location)
            if path is not None:
                target.set_entry(location, format, master, path.read_bytes())
            elif current.get(location) != (format, master):
                # only the manifest entry changes, so the member stays the
                # compressed blob the write copies; `set_entry` would inflate
                # it and deflate it again for a change it does not carry
                target.set_entry_format(location, format, master)
        # the manifest of the result is written in the order of `entries`, which
        # is the order `Omex` keeps and the order a caller sees; without this the
        # core would write its own order, which for an opened archive is what its
        # `manifest.xml` declared and then the members it did not list
        target.reorder_entries([entry.location for entry in entries])
    except ArchiveBusyError as error:
        raise _busy_error(error) from error
    except OmexError as error:
        raise _map_error(error) from error
    return target


def declares_manifest(path: Path) -> bool:
    """Return whether the file is a COMBINE archive, by its structure alone.

    The core reads the end of the file, which says where the central directory
    is, and then that directory, which lists the names of the members; a name
    is normalized as `Omex` normalizes a location, and a container which
    declares `./manifest.xml` is an archive. No member is inflated and none is
    decrypted, so the answer costs the size of the central directory rather
    than the size of the archive, and an encrypted archive is an archive: its
    manifest is declared whether or not a caller can read it.

    Args:
        path: the file to look at, which must exist

    Returns:
        True if the container declares a `manifest.xml`. False for a file which
        is no zip container and for a container without one, as
        `zipfile.is_zipfile` answers False for what is not a zip.

    Raises:
        OSError: if the file cannot be opened or read. Being unable to read a
            file is not an answer about its content.
    """
    return has_manifest(path)


def _locations(archive: Archive) -> set[str]:
    """Return the locations the archive holds as entries.

    Args:
        archive: the archive

    Returns:
        The locations of `archive.entries`.
    """
    return {location for location, _, _ in archive.entries}
