"""Module for working with chebi."""
from pathlib import Path
from pprint import pprint
from typing import Dict

from zeep import Client

from pymetadata import CACHE_PATH, CACHE_USE, RESOURCES_DIR, log
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache


logger = log.get_logger(__name__)

# client = Client('https://www.ebi.ac.uk/webservices/chebi/2.0/webservice?wsdl')
client = Client(str(RESOURCES_DIR / "chebi_webservice_wsdl.xml"))


class ChebiQuery:
    """Class to query information from ChEBI.

    An overview over available methods:
        python -mzeep https://www.ebi.ac.uk/webservices/chebi/2.0/webservice?wsdl
    """

    @staticmethod
    def query(
        chebi: str, cache: bool = CACHE_USE, cache_path: Path = CACHE_PATH
    ) -> Dict:
        """Query additional ChEBI information."""

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
