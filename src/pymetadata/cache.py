"""Caching of web service responses.

Queries to identifiers.org, OLS, ChEBI and UniChem are cached on disk so that
repeated lookups of the same term do not hit the network again. Caching is on
by default and controlled by `pymetadata.CACHE_USE` and `pymetadata.CACHE_PATH`,
which are read at query time.

A cached response is refreshed once it is older than the cache duration of its
service, see `CACHE_DURATION_ONTOLOGY` and `CACHE_DURATION_REGISTRY`. If the
refresh fails, because the service is unreachable or answers with an error, the
outdated content is used instead of failing the query and a warning is logged,
see `read_json_cache_fallback`. Working offline therefore keeps working with
whatever was cached before.

The cache can be shared by processes which run at the same time, e.g., the
workers of pytest-xdist. A cache file is written to a temporary file next to it,
which then replaces it atomically, so a reader never sees a partially written
file. On Windows a file which another process has open cannot be replaced, and a
file which is being replaced cannot be opened; both are retried, see
`CACHE_IN_USE_ATTEMPTS`. Writing the cache is best effort: the caller already
has the content, so a cache file which cannot be written is a warning and not an
error, and the cache file which is there is kept.
"""

import hashlib
import json
import logging
import os
import secrets
import time
import urllib.parse
from collections.abc import Callable
from json.encoder import JSONEncoder
from pathlib import Path
from typing import Any, TypeVar

logger = logging.getLogger(__name__)

#: hours a cached ontology response stays valid, i.e., the responses of OLS,
#: ChEBI and UniChem. They describe the terms of an ontology release, which
#: changes with the release and not from one day to the next
CACHE_DURATION_ONTOLOGY: float = 30 * 24

#: hours the cached identifiers.org registry stays valid. Namespaces and the
#: patterns their terms match are added and corrected continuously, so the
#: registry is refreshed daily
CACHE_DURATION_REGISTRY: float = 24

#: maximum length in bytes of a cache file name; longer names are hashed. Most
#: file systems allow 255 bytes, the margin leaves room for temporary suffixes
CACHE_FILENAME_MAX_BYTES: int = 200

#: attempts to open or replace a cache file which another process uses. On
#: Windows a file cannot be replaced while another process has it open, and it
#: cannot be opened while another process replaces it (`PermissionError`). This
#: lasts only as long as the other process reads or replaces the file
CACHE_IN_USE_ATTEMPTS: int = 8

#: seconds before the second attempt, doubled before every further one, i.e.,
#: about 1.3 seconds over all attempts
CACHE_IN_USE_DELAY: float = 0.01

_T = TypeVar("_T")


class DataclassJSONEncoder(JSONEncoder):
    """JSON encoder which serializes dataclasses via their `__dict__`."""

    def default(self, o: Any) -> Any:
        """Serialize an object which json cannot serialize itself."""
        return o.__dict__


def cache_file(directory: Path, key: str) -> Path:
    """Get the path of the cache file for a key.

    The key, e.g., a term or an IRI, is percent-quoted into a single file name,
    so that it cannot contain path separators and leave the directory. A key
    whose file name would exceed `CACHE_FILENAME_MAX_BYTES` is replaced by its
    sha256 hash, which keeps the name within the limits of the file system.

    Args:
        directory: directory of the cache files
        key: what is cached, e.g., `CHEBI:2668`

    Returns:
        The path of the JSON cache file inside `directory`.

    Raises:
        ValueError: if the key is empty or the file would be outside `directory`
    """
    if not key:
        raise ValueError("Cache key must not be empty.")

    filename = f"{urllib.parse.quote(key, safe='')}.json"
    if len(filename.encode("utf-8")) > CACHE_FILENAME_MAX_BYTES:
        digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
        filename = f"{digest}.json"

    path = directory / filename
    if path.resolve().parent != directory.resolve():
        raise ValueError(f"Cache file for '{key}' is outside of '{directory}'.")

    return path


def cache_age(cache_path: Path) -> float | None:
    """Get the age of a cache file in hours.

    Args:
        cache_path: path of the cache file

    Returns:
        The age in hours, or None if the file does not exist.
    """
    if not cache_path.exists():
        return None

    return (time.time() - cache_path.stat().st_mtime) / 3600


def _retry_in_use(operation: Callable[[], _T]) -> _T:
    """Run a file operation, retrying while another process uses the file.

    Args:
        operation: opens or replaces a cache file

    Returns:
        The result of the operation.

    Raises:
        PermissionError: if the file is still in use after
            `CACHE_IN_USE_ATTEMPTS` attempts
    """
    delay = CACHE_IN_USE_DELAY
    for _ in range(CACHE_IN_USE_ATTEMPTS - 1):
        try:
            return operation()
        except PermissionError:
            time.sleep(delay)
            delay *= 2
    return operation()


def read_bytes_cache(cache_path: Path) -> bytes:
    """Read a cache file.

    The read is retried while another process replaces the file, which only
    fails on Windows.

    Args:
        cache_path: path of the cache file

    Returns:
        The content of the file.

    Raises:
        OSError: if the file cannot be read
    """
    return _retry_in_use(cache_path.read_bytes)


def _load_json(cache_path: Path) -> Any:
    """Read and parse a JSON cache file, see `read_bytes_cache`."""
    return json.loads(read_bytes_cache(cache_path).decode("utf-8"))


def read_json_cache(cache_path: Path, max_age: float | None = None) -> dict:
    """Read a JSON cache file.

    Args:
        cache_path: path of the cache file
        max_age: maximum age of the content in hours; older content is treated
            as if it were not cached. Any age is accepted if None

    Returns:
        The cached content.

    Raises:
        IOError: if the cache file does not exist, is older than `max_age` or
            is corrupt. A corrupt file is removed, so that it is replaced by
            the next query.
    """
    age = cache_age(cache_path)
    if age is None:
        raise OSError(f"Cache path does not exist: '{cache_path}'")

    if max_age is not None and age > max_age:
        logger.debug("Cache outdated after %.1f h: %s", age, cache_path)
        raise OSError(f"Cache is older than {max_age} h: '{cache_path}'")

    try:
        logger.debug("Read cache: %s", cache_path)
        return _load_json(cache_path)
    except ValueError as err:
        # JSONDecodeError and UnicodeDecodeError, e.g., a file written by
        # a crashed process or modified by hand
        logger.warning("Removing corrupt cache: '%s': %s", cache_path, err)
        cache_path.unlink(missing_ok=True)
        raise OSError(f"Cache is corrupt: '{cache_path}': {err}") from err


def read_json_cache_fallback(cache_path: Path, reason: str) -> dict | None:
    """Read a cache file of any age, after the query which should refresh it failed.

    The library prefers outdated content over no content, so that an
    unreachable service does not fail a query which was answered before. The
    age of the content is not checked and a warning names the reason, so that
    the fallback is visible in the log.

    Args:
        cache_path: path of the cache file
        reason: why the content could not be refreshed, e.g., the error of the
            failed query

    Returns:
        The cached content, or None if nothing is cached.
    """
    age = cache_age(cache_path)
    if age is None:
        return None

    try:
        data = _load_json(cache_path)
    except (OSError, ValueError) as err:
        logger.warning("Outdated cache could not be read: '%s': %s", cache_path, err)
        return None

    logger.warning(
        "Using the cache from %.1f h ago, it could not be refreshed: %s (%s)",
        age,
        cache_path,
        reason,
    )
    return data


def write_bytes_cache(content: bytes, cache_path: Path) -> None:
    """Write a cache file, best effort.

    Missing parent directories are created. The content is written to a
    temporary file in the directory of the cache file, which then replaces the
    cache file atomically (`os.replace`): a reader never sees a partially
    written file, and of several processes which write the same cache file at
    the same time the last one wins with its complete file.

    The caller has the content already, so a cache file which cannot be written
    is a warning and not an error, and the cache file which is there is kept.
    This covers a cache file which another process has open on Windows, where
    it cannot be replaced; the replace is retried for a while (see
    `CACHE_IN_USE_ATTEMPTS`) before the cache file of the other process is kept.

    Args:
        content: content of the file
        cache_path: path of the cache file
    """
    # unique to this write, next to the cache file so that the replace stays
    # on one file system and is atomic; it ends in `.tmp`, so that a file left
    # behind by a killed process is never read as a cache file
    temporary_path = cache_path.with_name(
        f"{cache_path.name}.{os.getpid()}.{secrets.token_hex(4)}.tmp"
    )
    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info("Write cache: %s", cache_path)
        try:
            temporary_path.write_bytes(content)
            _retry_in_use(lambda: temporary_path.replace(cache_path))
        finally:
            # nothing is left after the replace
            temporary_path.unlink(missing_ok=True)
    except OSError as err:
        logger.warning(
            "Cache could not be written, it is not updated: '%s': %s",
            cache_path,
            err,
        )


def write_json_cache(
    data: dict, cache_path: Path, json_encoder: type[JSONEncoder] | None = None
) -> None:
    """Write a JSON cache file, best effort.

    The data is serialized before anything is written, and the file is written
    with `write_bytes_cache`, i.e., atomically, and a cache file which cannot
    be written is a warning and not an error.

    Args:
        data: data to serialize
        cache_path: path of the cache file
        json_encoder: encoder for objects json cannot serialize, e.g.
            `DataclassJSONEncoder` for dataclasses

    Raises:
        TypeError: if the data cannot be serialized; nothing is written then
    """
    content = json.dumps(data, indent=2, cls=json_encoder)
    write_bytes_cache(content.encode("utf-8"), cache_path)
