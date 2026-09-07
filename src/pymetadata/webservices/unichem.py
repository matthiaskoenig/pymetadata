"""Substance cross references from UniChem.

UniChem maps a structure, identified by its InChIKey, to the entries of many
chemistry databases, which gives cross references for a substance without
having to query every database separately.

```python
from pymetadata.webservices.unichem import UnichemQuery

query = UnichemQuery()
xrefs = query.query_xrefs_for_inchikey("AAOVKJBEBIDNHE-UHFFFAOYSA-N")
```

See <https://www.ebi.ac.uk/unichem/info/webservices>.
"""

import contextlib
import logging
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

import pymetadata
from pymetadata.cache import (
    CACHE_DURATION_ONTOLOGY,
    DataclassJSONEncoder,
    read_json_cache,
    read_json_cache_fallback,
    write_json_cache,
)
from pymetadata.core.xref import CrossReference
from pymetadata.webservices.webservice import WebserviceError, get_json

logger = logging.getLogger(__name__)


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
    """Queries against the UniChem web service.

    The sources of UniChem are retrieved once and shared by all instances.
    Responses are cached on disk for `CACHE_DURATION_ONTOLOGY` hours, see
    `pymetadata.CACHE_USE`. If UniChem cannot be reached, cached content is used
    however old it is.
    """

    sources: ClassVar[dict[int, UnichemSource]] = {}

    def __init__(self, cache_path: Path | None = None, cache: bool | None = None):
        """Initialize the query.

        Args:
            cache_path: directory for cached responses, defaults to
                `pymetadata.CACHE_PATH`
            cache: cache responses, defaults to `pymetadata.CACHE_USE`
        """
        if cache_path is None:
            cache_path = pymetadata.CACHE_PATH
        if cache is None:
            cache = pymetadata.CACHE_USE

        self.cache_path: Path = cache_path
        self.cache: bool = cache

        # cache the sources on the class, an instance attribute would make
        # every new query retrieve them again
        if not UnichemQuery.sources:
            UnichemQuery.sources = self.get_sources()

    def get_sources(self) -> dict[int, UnichemSource]:
        """Get the databases known to UniChem, from the cache or the service.

        Returns:
            The sources by their UniChem source id.

        Raises:
            WebserviceError: if the sources are neither cached nor retrievable
        """
        unichem_sources_path = self.cache_path / "unichem_sources.json"

        data: dict
        if self.cache:
            with contextlib.suppress(OSError):
                # cache does not exist or is outdated
                data = read_json_cache(
                    unichem_sources_path, max_age=CACHE_DURATION_ONTOLOGY
                )
                return {int(k): UnichemSource(**v) for k, v in data.items()}

        url = "https://www.ebi.ac.uk/unichem/api/v1/sources/"
        try:
            data = get_json(url)
            if data["response"].lower() != "success":
                raise WebserviceError(f"Could not query UniChem sources: '{data}'")
        except WebserviceError as err:
            # prefer outdated sources over none, e.g., when offline
            if self.cache:
                fallback = read_json_cache_fallback(
                    unichem_sources_path, reason=str(err)
                )
                if fallback is not None:
                    return {int(k): UnichemSource(**v) for k, v in fallback.items()}
            raise

        sources_list: list[UnichemSource] = [
            UnichemSource(**v) for v in data["sources"]
        ]
        sources = {source.sourceID: source for source in sources_list}

        # write cache
        if self.cache:
            write_json_cache(
                data=sources,
                cache_path=unichem_sources_path,
                json_encoder=DataclassJSONEncoder,
            )

        return sources

    def query_xrefs_for_inchikey(self, inchikey: str) -> list[CrossReference]:
        """Get the cross references for a structure.

        Args:
            inchikey: InChIKey of the structure, e.g.,
                `AAOVKJBEBIDNHE-UHFFFAOYSA-N`

        Returns:
            One cross reference per database which contains the structure.
        """
        # cache files
        xref_base_path = self.cache_path / "unichem"
        if not xref_base_path.exists():
            xref_base_path.mkdir(parents=True)
        xref_path = xref_base_path / f"{inchikey}.json"

        # retrieve or query data
        data: dict = {}
        if self.cache:
            with contextlib.suppress(OSError):
                # cache does not exist or is outdated
                data = read_json_cache(xref_path, max_age=CACHE_DURATION_ONTOLOGY)

        if not data:
            url = f"https://www.ebi.ac.uk/unichem/rest/inchikey/{inchikey}"
            try:
                data = get_json(url)
            except WebserviceError as err:
                # prefer outdated cross references over none, e.g., when offline
                if self.cache:
                    fallback = read_json_cache_fallback(xref_path, reason=str(err))
                    if fallback is not None:
                        data = fallback

                if not data:
                    logger.error(
                        "UniChem xrefs could not be retrieved for '%s': %s",
                        inchikey,
                        err,
                    )
                    return []
            else:
                write_json_cache(
                    data=data, cache_path=xref_path, json_encoder=DataclassJSONEncoder
                )

        xrefs: list[CrossReference] = []
        if data:
            if "error" in data:
                logger.warning("No xrefs for inchikey: '%s'", inchikey)
                return []

            # process data
            item: dict[str, str]
            for item in data:
                source_id: int = int(item["src_id"])
                if source_id not in self.sources:
                    if source_id not in {40, 49, 50}:
                        # number 40 is missing from definitions
                        logger.error(
                            "No UniChem source for source id '%s', in item '%s'",
                            source_id,
                            item,
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
    pymetadata.CACHE_PATH = Path.home() / ".cache" / "pymetadata"

    # query sources
    sources = UnichemQuery().get_sources()

    # query xrefs
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    xrefs = UnichemQuery(cache=False).query_xrefs_for_inchikey(inchikey=inchikey)
    print(xrefs)
    # results = UnichemQuery(cache=True).query_xrefs_for_inchikey(inchikey=inchikey)

    inchikey = "yxsdfasdfs"
    xrefs = UnichemQuery(cache=False).query_xrefs_for_inchikey(inchikey=inchikey)
