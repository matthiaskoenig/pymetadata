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
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any, ClassVar

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
    """Database known to UniChem, see the `sources` endpoint of the web service.

    Only `sourceID` and `name` are required. UniChem adds and removes the
    descriptive fields without notice, so they are optional, and
    `UnichemSource.from_dict` ignores fields which are not declared here.

    Attributes:
        sourceID: id of the source in UniChem
        name: unique name of the source in UniChem, always lower case
        nameLabel: name suitable as label of the source, in the case used by
            the source
        nameLong: full name of the source, as defined by the source
        srcUrl: home page of the source
        baseIdUrl: base url for links to a compound in the source; the
            identifier of the compound is appended or replaces `{$id}`
        description: description of the content of the source
        UCICount: number of UniChem compound identifiers in the source
        created: date the source was added to UniChem
        lastChecked: date UniChem checked the source for an update
        srcLastUpdated: date of the last update of the source
        srcDetails: details on the source
        updateComments: comments on the update of the source
        private: the source is not public
    """

    sourceID: int
    name: str
    nameLabel: str | None = field(default=None, repr=False)
    nameLong: str | None = field(default=None, repr=False)
    srcUrl: str | None = None
    baseIdUrl: str | None = field(default=None, repr=False)
    description: str | None = field(default=None, repr=False)
    UCICount: int | None = field(default=None, repr=False)
    created: str | None = field(default=None, repr=False)
    lastChecked: str | None = field(default=None, repr=False)
    srcLastUpdated: str | None = field(default=None, repr=False)
    srcDetails: str | None = field(default=None, repr=False)
    updateComments: str | None = field(default=None, repr=False)
    private: bool | None = field(default=None, repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "UnichemSource":
        """Create a source from a source of the web service or of the cache.

        Args:
            data: fields of the source, fields unknown to `UnichemSource` are
                ignored

        Returns:
            The source.
        """
        names = {f.name for f in fields(cls)}
        unknown = sorted(set(data) - names)
        if unknown:
            logger.debug("Ignored fields of UniChem source: %s", unknown)
        return cls(**{k: v for k, v in data.items() if k in names})


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
                return {int(k): UnichemSource.from_dict(v) for k, v in data.items()}

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
                    return {
                        int(k): UnichemSource.from_dict(v) for k, v in fallback.items()
                    }
            raise

        sources_list: list[UnichemSource] = [
            UnichemSource.from_dict(v) for v in data["sources"]
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
