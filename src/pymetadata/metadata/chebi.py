"""Module for working with chebi."""
import logging
from pathlib import Path
from pprint import pprint
from typing import Dict

import numpy as np
from libchebipy import ChebiEntity, ChebiException

from pymetadata import CACHE_PATH, CACHE_USE
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache


logger = logging.getLogger(__name__)


class ChebiQuery:
    """Class to query information from ChEBI."""

    @staticmethod
    def query(
        chebi: str, cache: bool = CACHE_USE, cache_path: Path = CACHE_PATH
    ) -> Dict:
        """Query additional chebi information."""

        if not chebi:
            return dict()

        # caching
        chebi_base_path = cache_path / "chebi"
        if not chebi_base_path.exists():
            chebi_base_path.mkdir(parents=True)

        chebi_path = chebi_base_path / f"{chebi.replace(':', '%3A')}.json"
        data = read_json_cache(cache_path=chebi_path) if cache else None

        # fetch and cache data
        if data is None:
            try:
                chebi_entity = ChebiEntity(chebi)
                logger.warning(f"Query: {chebi}")
            except ChebiException:
                logger.error(f"CHEBI information could not be retrieved for: {chebi}")
                return dict()
            formula = chebi_entity.get_formula()
            charge = chebi_entity.get_charge()
            if np.isnan(charge):
                charge = None
            mass = chebi_entity.get_mass()
            if np.isnan(mass):
                mass = None

            inchikey = chebi_entity.get_inchi_key()

            data = {
                "chebi": chebi,
                "formula": formula,
                "charge": charge,
                "mass": mass,
                "inchikey": inchikey,
            }

            write_json_cache(
                data=data, cache_path=chebi_path, json_encoder=DataclassJSONEncoder
            )

        return data


if __name__ == "__main__":
    chebis = ["CHEBI:2668", "CHEBI:138366", "CHEBI:9637", "CHEBI:155897"]
    for chebi in chebis:
        print(chebi)
        d = ChebiQuery.query(chebi=chebi, cache=False)
        pprint(d)
        d = ChebiQuery.query(chebi=chebi, cache=True)
