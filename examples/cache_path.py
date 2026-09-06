"""Customizing the cache path.

Run with `python examples/cache_path.py`. The responses are written to
`pymetadata.CACHE_PATH`, so the second run answers the same terms from disk
instead of querying ChEBI again.
"""

from pathlib import Path

import pymetadata
from pymetadata.console import console
from pymetadata.webservices.chebi import ChebiQuery

pymetadata.CACHE_PATH = Path.home() / ".cache" / "pymetadata"

if __name__ == "__main__":
    chebis = ["CHEBI:2668", "CHEBI:138366", "CHEBI:9637", "CHEBI:155897"]
    for chebi in chebis:
        data = ChebiQuery.query(chebi=chebi, cache=True)
        console.print(f"{chebi}: {data.get('name')}")
