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

    sourceID: int
    srcUrl: str
    name: str
    nameLabel: str = field(repr=False)
    nameLong: str = field(repr=False)
    UCICount: int = field(repr=False)
    baseIdUrl: str = field(repr=False)
    description: str = field(repr=False)
    created: str = field(repr=False)
    lastUpdated: str = field(repr=False)
    srcDetails: str = field(repr=False)
    srcReleaseDate: str = field(repr=False)
    srcReleaseNumber: int = field(repr=False)
    updateComments: str = field(repr=False)
    private: bool = field(repr=False)


class UnichemQuery:
    """Query unichem."""

    sources: Dict[int, UnichemSource] = {}

    def __init__(self, cache_path: Path = CACHE_PATH, cache: bool = CACHE_USE):
        """Initialize UnichemQuery."""
        self.cache_path: Path = cache_path
        self.cache: bool = cache

        if not self.sources:
            self.sources = self.get_sources(
                cache_path=self.cache_path, cache=self.cache
            )

    @classmethod
    def get_sources(
        cls, cache_path: Path = CACHE_PATH, cache: bool = CACHE_USE
    ) -> Dict[int, UnichemSource]:
        """Retrieve or query the sources."""

        sources: Dict[int, UnichemSource]
        unichem_sources_path = cache_path / "unichem_sources.json"

        data: Dict
        if cache and unichem_sources_path.exists():
            data = read_json_cache(unichem_sources_path)
            sources = {int(k): UnichemSource(**v) for k, v in data.items()}
        else:
            # query data
            url = "https://www.ebi.ac.uk/unichem/api/v1/sources/"
            response = requests.get(url)
            data = response.json()
            if data["response"].lower() != "success":
                raise IOError(f"Could not query UniChem sources: '{data}'")

            sources_list: List[UnichemSource] = [
                UnichemSource(**v) for v in data["sources"]
            ]
            sources = {source.sourceID: source for source in sources_list}

            # write cache
            write_json_cache(
                data=sources,
                cache_path=unichem_sources_path,
                json_encoder=DataclassJSONEncoder,
            )

        return sources

    def query_xrefs_for_inchikey(self, inchikey: str) -> List[CrossReference]:
        """Get the cross references for a given inchikey."""

        # cache files
        xref_base_path = self.cache_path / "unichem"
        if not xref_base_path.exists():
            xref_base_path.mkdir(parents=True)
        xref_path = xref_base_path / f"{inchikey}.json"

        # retrieve or query data
        data: Dict
        if self.cache and xref_path.exists():
            data = read_json_cache(xref_path)
        else:
            url = f"https://www.ebi.ac.uk/unichem/rest/inchikey/{inchikey}"
            response = requests.get(url)
            data = response.json()
            write_json_cache(
                data=data, cache_path=xref_path, json_encoder=DataclassJSONEncoder
            )

        xrefs: List[CrossReference] = []
        if data:
            if "error" in data:
                logger.error(f"No xrefs for inchikey: '{inchikey}'")
                return []

            # process data
            item: Dict[str, str]
            for item in data:
                source_id: int = int(item["src_id"])
                if source_id not in self.sources:
                    if source_id != 40:
                        # number 40 is missing from definitions
                        logger.error(
                            f"No UniChem source for source id '{source_id}', in item "
                            f"'{item}'"
                        )
                    continue

                source: UnichemSource = self.sources[source_id]
                accession = item["src_compound_id"]
                if source.baseIdUrl:

                    # create and clean url
                    if not source.baseIdUrl:
                        continue

                    url = f"{source.baseIdUrl}{accession}"

                    url_accession = urllib.parse.quote(accession)
                    url = url.replace("{$Id}", url_accession)
                    url = url.replace("{$id}", url_accession)

                    # handle special case
                    if source.name == "clinicaltrials":
                        url = f"{url}%22"

                    # escape whitespace for dailymed | clinicaltrials | ...
                    url = url.replace(" ", "%20")

                    xref = CrossReference(
                        name=source.name, accession=accession, url=url
                    )
                    xrefs.append(xref)

        return xrefs


if __name__ == "__main__":

    # query sources
    sources = UnichemQuery.get_sources()

    # query xrefs
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    xrefs = UnichemQuery(cache=False).query_xrefs_for_inchikey(inchikey=inchikey)
    print(xrefs)
    # results = UnichemQuery(cache=True).query_xrefs_for_inchikey(inchikey=inchikey)

    inchikey = "yxsdfasdfs"
    xrefs = UnichemQuery(cache=False).query_xrefs_for_inchikey(inchikey=inchikey)
