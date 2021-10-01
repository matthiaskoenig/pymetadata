"""
Unichem metadata.

Additional substance information based on inchikeys

https://www.ebi.ac.uk/unichem/info/webservices#GetSrcCpdIdsFromKey
https://www.ebi.ac.uk/unichem/rest/inchikey/AAOVKJBEBIDNHE-UHFFFAOYSA-N
"""
import urllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import requests

from pymetadata import CACHE_PATH, CACHE_USE, log
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache
from pymetadata.core.xref import CrossReference


logger = log.get_logger(__name__)


@dataclass
class UnichemSource:
    """Unichem source.

    src_id (the src_id for this source),
    src_url (the main home page of the source),
    name (the unique name for the source in UniChem, always lower case),
    name_long (the full name of the source, as defined by the source),
    name_label (A name for the source suitable for use as a 'label' for the source within a web-page. Correct case setting for source, and always less than 30 characters),
    description (a description of the content of the source),
    base_id_url_available (an flag indicating whether this source provides a valid base_id_url for creating cpd-specific links [1=yes, 0=no]).
    base_id_url (the base url for constructing hyperlinks to this source [append an identifier from this source to the end of this url to create a valid url to a specific page for this cpd], unless aux_for_url=1),
    aux_for_url (A flag to indicate whether the aux_src field should be used to create hyperlinks instead of the src_compound_id [1=yes, 0=no]
    """

    src_id: int
    src_url: str
    name: str
    base_id_url: str = field(repr=False)
    aux_for_url: int = field(repr=False)
    base_id_url_available: int = field(repr=False)
    description: str = field(repr=False)
    name_label: str = field(repr=False)
    name_long: str = field(repr=False)


class UnichemQuery:
    """Query unichem."""

    sources = None

    @classmethod
    def _get_all_src_information(
        cls, cache_path: Path = CACHE_PATH, cache: bool = CACHE_USE
    ) -> Dict[int, UnichemSource]:

        unichem_sources_path = cache_path / "unichem_sources.json"

        data = read_json_cache(unichem_sources_path) if cache else None
        if data:
            # casting
            data = {k: UnichemSource(**v) for k, v in data.items()}
        else:
            logger.warning("Query: unichem sources")
            data = {}
            for src_id in range(50):
                source = cls._get_src_information(src_id)
                if source is not None:
                    data[source.src_id] = source

            write_json_cache(
                data=data,
                cache_path=unichem_sources_path,
                json_encoder=DataclassJSONEncoder,
            )

        return data

    @staticmethod
    def _get_src_information(src_id: int) -> Optional[UnichemSource]:
        """Get unichem source information for given source id."""
        url = f"https://www.ebi.ac.uk/unichem/rest/sources/{src_id}"
        response = requests.get(url)
        d = response.json()
        if "error" in d or len(d) == 0:
            return None
        else:
            return UnichemSource(**d[0])

    @classmethod
    def query_xrefs(
        cls, inchikey: str, cache_path: Path = CACHE_PATH, cache: bool = CACHE_USE
    ) -> List[CrossReference]:
        """Get the cross references for a given inchikey."""
        if cls.sources is None:
            cls.sources = cls._get_all_src_information(
                cache_path=cache_path, cache=cache
            )

        xref_base_path = cache_path / "unichem"
        if not xref_base_path.exists():
            xref_base_path.mkdir(parents=True)
        xref_path = xref_base_path / f"{inchikey}.json"

        data = read_json_cache(xref_path) if cache else None
        if data:
            for item in data:
                if "source" in item:
                    item["source"] = UnichemSource(**item["source"])
                else:
                    logger.warning(f"No source information for item: {item}")
        else:
            url = f"https://www.ebi.ac.uk/unichem/rest/inchikey/{inchikey}"
            response = requests.get(url)
            data = response.json()
            if data is not None:
                if "error" in data:
                    if inchikey not in [
                        "YAJCHEVQCOHZDC-QMMNLEPNSA-N",  # insulin not a small molecule
                    ]:
                        logger.error(f"inchikey could not be queried: {url}, {data}")
                    return []

                # add source information to all entries
                for d in data:
                    try:
                        d["source"] = cls.sources[d["src_id"]]
                    except KeyError:
                        logger.error(
                            f"inchikey/{inchikey}: Key <{d['src_id']}> missing from {cls.sources.keys()}"
                        )

            write_json_cache(
                data=data, cache_path=xref_path, json_encoder=DataclassJSONEncoder  # type: ignore
            )

        # process data
        xrefs = []
        if data:
            for item in data:
                source = item["source"]  # type: UnichemSource
                name = source.name
                accession = item["src_compound_id"]
                if source.base_id_url_available:

                    # create and clean url
                    if not source.base_id_url:
                        continue

                    url = f"{source.base_id_url}{accession}"

                    url_accession = urllib.parse.quote(accession)
                    url = url.replace("{$Id}", url_accession)
                    url = url.replace("{$id}", url_accession)

                    # handle special case
                    if name == "clinicaltrials":
                        url = f"{url}%22"

                    # escape whitespace for dailymed | clinicaltrials | ...
                    url = url.replace(" ", "%20")

                    xref = CrossReference(name=name, accession=accession, url=url)
                    xrefs.append(xref)

        return xrefs


if __name__ == "__main__":

    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    results = UnichemQuery.query_xrefs(inchikey=inchikey, cache=False)
    results = UnichemQuery.query_xrefs(inchikey=inchikey, cache=True)
