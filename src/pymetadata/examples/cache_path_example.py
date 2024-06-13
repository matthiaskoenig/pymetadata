"""Example for customizing the cache path."""

from pathlib import Path

import pymetadata
from pymetadata.chebi import ChebiQuery


pymetadata.CACHE_PATH = Path.home() / ".cache" / "pymetadata"

if __name__ == "__main__":

    chebis = ["CHEBI:2668", "CHEBI:138366", "CHEBI:9637", "CHEBI:155897"]
    for chebi in chebis:
        d = ChebiQuery.query(chebi=chebi, cache=True)
