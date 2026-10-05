"""Protein information from UniProt.

```python
from pymetadata.webservices.uniprot import UniprotQuery

info = UniprotQuery.query("P69905")
```

See <https://www.uniprot.org/>.
"""

import contextlib
import logging
import re
from pathlib import Path
from typing import Any

import pymetadata
from pymetadata.cache import (
    CACHE_DURATION_ONTOLOGY,
    cache_file,
    read_json_cache,
    read_json_cache_fallback,
    write_json_cache,
)
from pymetadata.webservices.webservice import (
    WebserviceError,
    WebserviceNotFoundError,
    get_json,
)

logger = logging.getLogger(__name__)

UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/{}.json"

# the accession format of UniProt, with an optional isoform
UNIPROT_PATTERN = re.compile(
    r"^(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})(?:-\d+)?$"
)


def _entry_info(entry: dict[str, Any]) -> dict[str, Any]:
    """Reduce an entry of UniProt to the information shown for an annotation."""
    description = entry.get("proteinDescription") or {}
    names = description.get("recommendedName") or next(
        iter(description.get("submissionNames") or []), {}
    )
    function = next(
        (
            comment["texts"][0].get("value")
            for comment in entry.get("comments") or []
            if comment.get("commentType") == "FUNCTION" and comment.get("texts")
        ),
        None,
    )
    return {
        "accession": entry.get("primaryAccession"),
        "entry": entry.get("uniProtkbId"),
        "name": (names.get("fullName") or {}).get("value"),
        "organism": (entry.get("organism") or {}).get("scientificName"),
        "genes": [
            gene["geneName"]["value"]
            for gene in entry.get("genes") or []
            if "geneName" in gene
        ],
        "length": (entry.get("sequence") or {}).get("length"),
        "function": function,
    }


class UniprotQuery:
    """Queries against the UniProt web service.

    Responses are cached on disk for `CACHE_DURATION_ONTOLOGY` hours, see
    `pymetadata.CACHE_USE`. If UniProt cannot be reached, cached content is used
    however old it is.
    """

    @staticmethod
    def query(
        accession: str, cache: bool | None = None, cache_path: Path | None = None
    ) -> dict[str, Any]:
        """Query the information of a protein.

        Args:
            accession: accession of UniProt, e.g., `P69905`
            cache: cache the response, defaults to `pymetadata.CACHE_USE`
            cache_path: directory for cached responses, defaults to
                `pymetadata.CACHE_PATH`

        Returns:
            The protein information, empty if the accession is invalid, unknown
            or inactive, or if UniProt cannot be reached and nothing is cached.
        """
        accession = accession.strip().upper() if accession else ""
        if not UNIPROT_PATTERN.match(accession):
            logger.error("Invalid UniProt accession: '%s'", accession)
            return {}
        if cache is None:
            cache = pymetadata.CACHE_USE
        if cache_path is None:
            cache_path = pymetadata.CACHE_PATH

        path = cache_file(Path(cache_path) / "uniprot", accession)
        if cache:
            with contextlib.suppress(OSError, ValueError):
                # cache does not exist, is outdated or corrupt
                data = read_json_cache(cache_path=path, max_age=CACHE_DURATION_ONTOLOGY)
                if data:
                    return data

        try:
            entry = get_json(UNIPROT_URL.format(accession))
        except WebserviceNotFoundError:
            logger.error("UniProt accession is unknown: '%s'", accession)
            return {}
        except WebserviceError as err:
            # prefer outdated information over none, e.g., when offline
            if cache:
                fallback = read_json_cache_fallback(path, reason=str(err))
                if fallback is not None:
                    return fallback
            logger.error(
                "UniProt information could not be retrieved for '%s': %s",
                accession,
                err,
            )
            return {}

        if not isinstance(entry, dict):
            logger.error("Unexpected response of UniProt for '%s'", accession)
            return {}
        if entry.get("entryType") == "Inactive":
            logger.error("UniProt entry is inactive: '%s'", accession)
            return {}

        data = _entry_info(entry)
        if cache:
            write_json_cache(data=data, cache_path=path)
        return data
