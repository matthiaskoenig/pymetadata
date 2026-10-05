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
import re
from pathlib import Path
from typing import Any

import pymetadata
from pymetadata.cache import (
    CACHE_DURATION_ONTOLOGY,
    DataclassJSONEncoder,
    cache_age,
    cache_file,
    read_json_cache,
    read_json_cache_fallback,
    write_json_cache,
)
from pymetadata.webservices.webservice import (
    WebserviceError,
    WebserviceNotFoundError,
    get_bytes,
    get_json,
)

logger = logging.getLogger(__name__)

#: ChEBI term with optional prefix, e.g., `CHEBI:15377`, `chebi:15377`, `15377`
CHEBI_PATTERN = re.compile(r"^(?:CHEBI:)?(\d+)$", flags=re.IGNORECASE)

#: endpoint of the ChEBI compounds, queried with the `chebi_ids` parameter
CHEBI_URL = "https://www.ebi.ac.uk/chebi/backend/api/public/compounds/"

#: endpoint of the structure (svg image) of a compound, formatted with its number
CHEBI_STRUCTURE_URL = (
    "https://www.ebi.ac.uk/chebi/backend/api/public/compound/{}/structure/"
)


class ChebiQuery:
    """Queries against the ChEBI web service.

    Responses are cached on disk for `CACHE_DURATION_ONTOLOGY` hours, see
    `pymetadata.CACHE_USE`. If ChEBI cannot be reached, cached content is used
    however old it is.
    """

    @staticmethod
    def normalize_id(chebi: str) -> str | None:
        """Normalize the spelling of a ChEBI term.

        Args:
            chebi: ChEBI term, e.g., `CHEBI:15377`, `chebi:15377` or `15377`

        Returns:
            The term as `CHEBI:<number>`, or None if it is not a ChEBI term.
        """
        match = CHEBI_PATTERN.match(chebi.strip())
        if not match:
            return None
        return f"CHEBI:{match.group(1)}"

    @staticmethod
    def query(
        chebi: str, cache: bool | None = None, cache_path: Path | None = None
    ) -> dict:
        """Query the information stored for a ChEBI term.

        Args:
            chebi: ChEBI term, e.g., `CHEBI:33699`; `chebi:33699` and `33699`
                are accepted as well
            cache: cache the response, defaults to `pymetadata.CACHE_USE`
            cache_path: directory for cached responses, defaults to
                `pymetadata.CACHE_PATH`

        Returns:
            The ChEBI information, empty if the term is invalid or could not be
            resolved.
        """
        if not chebi:
            return {}
        term = ChebiQuery.normalize_id(chebi)
        if term is None:
            logger.error("Invalid ChEBI term: '%s'", chebi)
            return {}
        chebi = term

        if cache is None:
            cache = pymetadata.CACHE_USE
        if cache_path is None:
            cache_path = pymetadata.CACHE_PATH

        chebi_path = cache_file(Path(cache_path) / "chebi", chebi)
        data: dict[str, Any] = {}
        if cache:
            with contextlib.suppress(OSError):
                # cache does not exist or is outdated
                data = read_json_cache(
                    cache_path=chebi_path, max_age=CACHE_DURATION_ONTOLOGY
                )

        # fetch and cache data
        if not data:
            try:
                result = get_json(CHEBI_URL, params={"chebi_ids": chebi})
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

            entry = result.get(chebi) if isinstance(result, dict) else None
            result = entry.get("data") if isinstance(entry, dict) else None
            if not result:
                logger.error("CHEBI term is unknown: '%s'", chebi)
                return {}

            chemical_data = result.get("chemical_data")
            default_structure = result.get("default_structure")
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

            if cache:
                write_json_cache(
                    data=data, cache_path=chebi_path, json_encoder=DataclassJSONEncoder
                )

        return data

    @staticmethod
    def structure(
        chebi: str, cache: bool | None = None, cache_path: Path | None = None
    ) -> bytes | None:
        """Get the structure of a ChEBI compound as an svg image.

        Args:
            chebi: ChEBI term, e.g., `CHEBI:33699`
            cache: cache the image, defaults to `pymetadata.CACHE_USE`
            cache_path: directory for cached responses, defaults to
                `pymetadata.CACHE_PATH`

        Returns:
            The svg image, None if the id is invalid, the compound has no
            structure, or ChEBI cannot be reached and nothing is cached.
        """
        match = CHEBI_PATTERN.match(chebi.strip()) if chebi else None
        if not match:
            logger.error("Invalid ChEBI id: '%s'", chebi)
            return None
        number = match.group(1)
        if cache is None:
            cache = pymetadata.CACHE_USE
        if cache_path is None:
            cache_path = pymetadata.CACHE_PATH
        path = Path(cache_path) / "chebi" / f"CHEBI%3A{number}.svg"
        age = cache_age(path) if cache else None
        if age is not None and age <= CACHE_DURATION_ONTOLOGY:
            return path.read_bytes()
        try:
            svg = get_bytes(CHEBI_STRUCTURE_URL.format(number))
        except WebserviceNotFoundError:
            return None
        except WebserviceError as err:
            if age is not None:
                logger.warning(
                    "Using outdated structure of 'CHEBI:%s': %s", number, err
                )
                return path.read_bytes()
            logger.error(
                "ChEBI structure could not be retrieved for 'CHEBI:%s': %s",
                number,
                err,
            )
            return None
        if cache:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(svg)
        return svg


if __name__ == "__main__":
    from pymetadata.console import console

    chebis = ["CHEBI:2668", "CHEBI:138366", "CHEBI:9637", "CHEBI:155897"]
    for chebi in chebis:
        console.rule(chebi, align="left", style="bold white")
        d = ChebiQuery.query(chebi=chebi, cache=False)
        console.print(d)
        d = ChebiQuery.query(chebi=chebi, cache=True)
