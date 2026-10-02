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
"""

import hashlib
import json
import logging
import tempfile
import time
import urllib.parse
from json.encoder import JSONEncoder
from pathlib import Path
from typing import Any

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
        with open(cache_path, encoding="utf-8") as fp:
            logger.debug("Read cache: %s", cache_path)
            return json.load(fp)
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
        with open(cache_path, encoding="utf-8") as fp:
            data = json.load(fp)
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


def write_json_cache(
    data: dict, cache_path: Path, json_encoder: type[JSONEncoder] | None = None
) -> None:
    """Write a JSON cache file.

    Missing parent directories are created. The file is replaced atomically so
    concurrent readers never see partial JSON and failed writes preserve the
    previous cache.

    Args:
        data: data to serialize
        cache_path: path of the cache file
        json_encoder: encoder for objects json cannot serialize, e.g.
            `DataclassJSONEncoder` for dataclasses
    """
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        # Use the same filesystem for atomic replacement. Close the file before
        # replacing it so this also works on Windows.
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=cache_path.parent, delete=False
        ) as fp:
            temporary_path = Path(fp.name)
            logger.info("Write cache: %s", cache_path)
            json.dump(data, fp=fp, indent=2, cls=json_encoder)
        temporary_path.replace(cache_path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
