"""Module for working with chebi."""

from pathlib import Path
from pprint import pprint
from typing import Any, Dict, Optional

from zeep import Client


import pymetadata
from pymetadata import log
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache

logger = log.get_logger(__name__)

# FIXME: copy the file to the cache dir
client = Client(str(pymetadata.RESOURCES_DIR / "chebi_webservice_wsdl.xml"))


class ChebiQuery:
    """Class to query information from ChEBI.

    An overview over available methods:
        python -mzeep https://www.ebi.ac.uk/webservices/chebi/2.0/webservice?wsdl
    """

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
            try:
                result = client.service.getCompleteEntity(chebi)
                # print(result)
            except Exception:
                logger.error(f"CHEBI information could not be retrieved for: {chebi}")
                return dict()

            # parse formula
            formula = None
            formulae = result["Formulae"]
            if formulae:
                formula = formulae[0]["data"]

            data = {
                "chebi": chebi,
                "name": result["chebiAsciiName"],
                "definition": result["definition"],
                "formula": formula,
                "charge": result["charge"],
                "mass": result["mass"],
                "inchikey": result["inchiKey"],
            }

            logger.info(f"Write chebi: {chebi_path}")
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
