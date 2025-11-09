"""Module for working with chebi."""

from pathlib import Path
from typing import Any, Dict, Optional
import requests

import pymetadata
from pymetadata import log
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache
from pymetadata.console import console

logger = log.get_logger(__name__)


class ChebiQuery:
    """Class to query information from ChEBI."""

    @staticmethod
    def query(
        chebi: str, cache: Optional[bool] = None, cache_path: Optional[Path] = None
    ) -> Dict:
        """Query additional ChEBI information."""

        if not chebi:
            return dict()
        if cache is None:
            cache = pymetadata.CACHE_USE
        if cache_path is None:
            cache_path = pymetadata.CACHE_PATH

        # caching
        chebi_base_path = Path(cache_path) / "chebi"
        if not chebi_base_path.exists():
            chebi_base_path.mkdir(parents=True)

        chebi_path = chebi_base_path / f"{chebi.replace(':', '%3A')}.json"
        data: Dict[str, Any] = {}
        if cache:
            try:
                data = read_json_cache(cache_path=chebi_path)
            except IOError:
                pass

        # fetch and cache data
        if not data:
            response = requests.get(
                url=f"https://www.ebi.ac.uk/chebi/backend/api/public/compounds/?chebi_ids={chebi}"
            )
            if response.status_code == 200:
                result = response.json()
            else:
                logger.error(f"CHEBI information could not be retrieved for: {chebi}")
                return dict()

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
