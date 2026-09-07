"""Substance information from ChEBI.

Queries the ChEBI web service for the information stored for a term, such as the
InChIKey, which can then be used to look up cross references with
`pymetadata.webservices.unichem`.

```python
from pymetadata.webservices.chebi import ChebiQuery

info = ChebiQuery.query("CHEBI:33699")
```

See <https://www.ebi.ac.uk/chebi/>.
"""

import contextlib
import logging
from pathlib import Path
from typing import Any

import pymetadata
from pymetadata.cache import (
    CACHE_DURATION_ONTOLOGY,
    DataclassJSONEncoder,
    read_json_cache,
    read_json_cache_fallback,
    write_json_cache,
)
from pymetadata.console import console
from pymetadata.webservices.webservice import WebserviceError, get_json

logger = logging.getLogger(__name__)


class ChebiQuery:
    """Queries against the ChEBI web service.

    Responses are cached on disk for `CACHE_DURATION_ONTOLOGY` hours, see
    `pymetadata.CACHE_USE`. If ChEBI cannot be reached, cached content is used
    however old it is.
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
                # cache does not exist or is outdated
                data = read_json_cache(
                    cache_path=chebi_path, max_age=CACHE_DURATION_ONTOLOGY
                )

        # fetch and cache data
        if not data:
            url = (
                "https://www.ebi.ac.uk/chebi/backend/api/public/compounds/"
                f"?chebi_ids={chebi}"
            )
            try:
                result = get_json(url)
            except WebserviceError as err:
                # prefer outdated information over none, e.g., when offline
                if cache:
                    fallback = read_json_cache_fallback(chebi_path, reason=str(err))
                    if fallback is not None:
                        return fallback

                logger.error(
                    "CHEBI information could not be retrieved for '%s': %s", chebi, err
                )
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

            logger.info("Write chebi: %s", chebi_path)
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
