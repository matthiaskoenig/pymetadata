"""Caching of information."""
import json
import logging
from json.encoder import JSONEncoder
from pathlib import Path
from typing import Any, Dict, Optional


logger = logging.getLogger(__name__)


class DataclassJSONEncoder(JSONEncoder):
    """JSON serialization of dataclasses."""

    def default(self, o: Any) -> Dict:
        """Serialize to JSON."""
        return o.__dict__


def read_json_cache(cache_path: Path) -> Optional[Dict]:
    """Read JSON cache file.

    :param cache_path:
    :return: Dictionary with content or None if cache file does not exist.
    """
    if cache_path.exists():
        with open(cache_path) as fp:
            logger.debug(f"Read cache: {cache_path}")
            return json.load(fp)

    return None


def write_json_cache(data: Dict, cache_path: Path, json_encoder: JSONEncoder = None):
    """Write JSON cache file.

    :param data:
    :param cache_path:
    :param json_encoder:
    :return:
    """
    with open(cache_path, "w") as fp:
        logger.info(f"Write cache: {cache_path}")
        if json_encoder:
            json.dump(data, fp=fp, indent=2, cls=json_encoder)
        else:
            json.dump(data, fp=fp, indent=2)
