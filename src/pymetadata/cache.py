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

import json
import logging
import time
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


class DataclassJSONEncoder(JSONEncoder):
    """JSON encoder which serializes dataclasses via their `__dict__`."""

    def default(self, o: Any) -> Any:
        """Serialize an object which json cannot serialize itself."""
        return o.__dict__


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
        IOError: if the cache file does not exist or is older than `max_age`
    """
    age = cache_age(cache_path)
    if age is None:
        raise OSError(f"Cache path does not exist: '{cache_path}'")

    if max_age is not None and age > max_age:
        logger.debug("Cache outdated after %.1f h: %s", age, cache_path)
        raise OSError(f"Cache is older than {max_age} h: '{cache_path}'")

    with open(cache_path) as fp:
        logger.debug("Read cache: %s", cache_path)
        return json.load(fp)


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
        with open(cache_path) as fp:
            data = json.load(fp)
    except (OSError, json.JSONDecodeError) as err:
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

    Missing parent directories are created.

    Args:
        data: data to serialize
        cache_path: path of the cache file
        json_encoder: encoder for objects json cannot serialize, e.g.
            `DataclassJSONEncoder` for dataclasses
    """
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_path, "w") as fp:
        logger.info("Write cache: %s", cache_path)
        if json_encoder:
            json.dump(data, fp=fp, indent=2, cls=json_encoder)
        else:
            json.dump(data, fp=fp, indent=2)
