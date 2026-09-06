"""Substance information from ChEBI.

Queries the ChEBI web service for the information stored for a term, such as the
InChIKey, which can then be used to look up cross references with
`pymetadata.unichem`.

```python
from pymetadata.chebi import ChebiQuery

info = ChebiQuery.query("CHEBI:33699")
```

See <https://www.ebi.ac.uk/chebi/>.
"""

import contextlib
from pathlib import Path
from typing import Any

import requests

import pymetadata
from pymetadata import log
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache
from pymetadata.console import console

logger = log.get_logger(__name__)


class ChebiQuery:
    """Queries against the ChEBI web service.

    Responses can be cached on disk, see `pymetadata.CACHE_USE`.
    """

    @staticmethod
    def query(
        chebi: str, cache: bool | None = None, cache_path: Path | None = None
    ) -> dict:
        """Query the information stored for a ChEBI term.

        Args:
            chebi: ChEBI term, e.g., `CHEBI:33699`
            cache: cache the response, defaults to `pymetadata.CACHE_USE`
            cache_path: directory for cached responses, defaults to
                `pymetadata.CACHE_PATH`

        Returns:
            The ChEBI information, empty if the term could not be resolved.
        """
        if not chebi:
            return {}
        if cache is None:
            cache = pymetadata.CACHE_USE
        if cache_path is None:
            cache_path = pymetadata.CACHE_PATH

        # caching
        chebi_base_path = Path(cache_path) / "chebi"
        if not chebi_base_path.exists():
            chebi_base_path.mkdir(parents=True)

        chebi_path = chebi_base_path / f"{chebi.replace(':', '%3A')}.json"
        data: dict[str, Any] = {}
        if cache:
            with contextlib.suppress(OSError):
                # cache does not exist
                data = read_json_cache(cache_path=chebi_path)

        # fetch and cache data
        if not data:
            response = requests.get(
                url=f"https://www.ebi.ac.uk/chebi/backend/api/public/compounds/?chebi_ids={chebi}"
            )
            if response.status_code == 200:
                result = response.json()
            else:
                logger.error(f"CHEBI information could not be retrieved for: {chebi}")
                return {}

            result = result[chebi]["data"]
            chemical_data = result["chemical_data"]
            default_structure = result["default_structure"]
            data = {
                "chebi": chebi,
                "name": result["ascii_name"],
                "definition": result["definition"],
                "formula": chemical_data["formula"] if chemical_data else None,
                "charge": chemical_data["charge"] if chemical_data else None,
                "mass": chemical_data["mass"] if chemical_data else None,
                "inchikey": default_structure["standard_inchi_key"]
                if default_structure
                else None,
            }

            logger.info(f"Write chebi: {chebi_path}")
            write_json_cache(
                data=data, cache_path=chebi_path, json_encoder=DataclassJSONEncoder
            )

        return data


if __name__ == "__main__":
    chebis = ["CHEBI:2668", "CHEBI:138366", "CHEBI:9637", "CHEBI:155897"]
    for chebi in chebis:
        console.rule(chebi, align="left", style="bold white")
        d = ChebiQuery.query(chebi=chebi, cache=False)
        console.print(d)
        d = ChebiQuery.query(chebi=chebi, cache=True)
