"""Caching of web service responses.

Queries to identifiers.org, OLS, ChEBI and UniChem can be cached on disk so that
repeated lookups of the same term do not hit the network again. Caching is off
by default and controlled by `pymetadata.CACHE_USE` and `pymetadata.CACHE_PATH`,
which are read at query time.
"""

import json
from json.encoder import JSONEncoder
from pathlib import Path
from typing import Any

from pymetadata import log

logger = log.get_logger(__name__)


class DataclassJSONEncoder(JSONEncoder):
    """JSON encoder which serializes dataclasses via their `__dict__`."""

    def default(self, o: Any) -> Any:
        """Serialize an object which json cannot serialize itself."""
        return o.__dict__


def read_json_cache(cache_path: Path) -> dict:
    """Read a JSON cache file.

    Args:
        cache_path: path of the cache file

    Returns:
        The cached content.

    Raises:
        IOError: if the cache file does not exist
    """
    if cache_path.exists():
        with open(cache_path) as fp:
            logger.debug("Read cache: %s", cache_path)
            return json.load(fp)

    raise OSError(f"Cache path does not exist: '{cache_path}'")


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
