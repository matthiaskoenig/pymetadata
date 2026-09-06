"""MIRIAM annotations.

An annotation combines a qualifier (`BQB`, `BQM`) with a resource pointing at a
database entry, forming the statement *this element **is** CHEBI:17234*.

`RDFAnnotation` parses the notations found in the wild, normalizes them to
identifiers.org compact identifiers and validates them against the
identifiers.org registry. `RDFAnnotationData` resolves what an identifier refers
to via the Ontology Lookup Service.

```python
from pymetadata.core.annotation import RDFAnnotation
from pymetadata.identifiers.miriam import BQB

annotation = RDFAnnotation(qualifier=BQB.IS, resource="chebi/CHEBI:33699")
print(annotation.resource_normalized)  # https://identifiers.org/CHEBI:33699
print(annotation.validate())
```
"""

import re
import urllib.parse
from enum import Enum
from pprint import pprint
from typing import Any, ClassVar, Final

import requests

from pymetadata import log
from pymetadata.core.xref import CrossReference, is_url
from pymetadata.identifiers.miriam import BQB, BQM
from pymetadata.identifiers.registry import Namespace, get_registry
from pymetadata.ontologies.ols import ONTOLOGIES, OLSQuery

_OLS_QUERY: OLSQuery | None = None


def get_ols_query() -> OLSQuery:
    """Get the shared OLS query object, created on first use.

    Returns:
        The shared `OLSQuery` for the ontologies in `ONTOLOGIES`.
    """
    global _OLS_QUERY
    if _OLS_QUERY is None:
        _OLS_QUERY = OLSQuery(ontologies=ONTOLOGIES)
    return _OLS_QUERY


IDENTIFIERS_ORG_PREFIX: Final = "https://identifiers.org"
IDENTIFIERS_ORG_PATTERN_COMPACT: Final = re.compile(
    r"^https?://identifiers.org/([a-zA-Z0-9.]+):(.+)"
)
IDENTIFIERS_ORG_PATTERN_CLASSIC: Final = re.compile(
    r"^https?://identifiers.org/([a-zA-Z0-9.]+)/(.+)"
)

BIOREGISTRY_PREFIX: Final = "https://bioregistry.io"
BIOREGISTRY_PATTERN: Final = re.compile(r"^https?://bioregistry.io/(.+)")

MIRIAM_URN_PATTERN: Final = re.compile(r"^urn:miriam:(.+)")

logger = log.get_logger(__name__)


class ProviderType(str, Enum):
    """Resolver a resource was written for.

    `IDENTIFIERS_ORG` and `BIOREGISTRY_IO` resources can be normalized and
    validated, `NONE` marks an arbitrary url which is kept as it is.
    """

    IDENTIFIERS_ORG = "identifiers.org"
    BIOREGISTRY_IO = "bioregistry.io"
    NONE = "none"


class RDFAnnotation:
    """RDFAnnotation class.

    Basic storage of annotation information. This consists of the relation
    and the resource.
    The annotations can be attached to other objects thereby forming
    triples which can be converted to RDF.

    Resource can be either:
        - `http(s)://identifiers.org/collection/term`, i.e., a identifiers.org URI
        - `collection/term`, i.e., the combination of collection and term
        - `http(s)://arbitrary.url`, an arbitrary URL
        - urn:miriam:uniprot:P03023
        - https://bioregistry.io/chebi:15996 urls via the bioregistry provider
    """

    replaced_collections: ClassVar[dict[str, str]] = {
        "obo.go": "go",
        "biomodels.sbo": "sbo",
    }

    def __init__(self, qualifier: BQB | BQM, resource: str, validate: bool = True):
        """Parse a resource into collection and term.

        Args:
            qualifier: MIRIAM qualifier of the annotation
            resource: the annotated resource, as an identifiers.org url
                (`https://identifiers.org/CHEBI:33699`), a bioregistry.io url,
                a compact identifier (`CHEBI:33699`), a collection and term
                (`chebi/CHEBI:33699`), a MIRIAM urn
                (`urn:miriam:chebi:CHEBI%3A33699`) or an arbitrary url
            validate: log warnings and errors for an invalid annotation

        Raises:
            ValueError: if the qualifier or the resource is missing, or if the
                resource is not a string
        """
        self.qualifier: BQB | BQM = qualifier
        self.collection: str | None = None
        self.term: str | None = None
        self.resource: str = resource
        self.provider: ProviderType = ProviderType.NONE

        if not qualifier:
            raise ValueError(
                f"MIRIAM qualifiers are required for rdf annotation, but no "
                f"qualifier for resource '{resource}' was provided."
            )
        if not resource:
            raise ValueError(
                f"resource is required for annotation, but resource is emtpy "
                f"'{qualifier} {resource}'."
            )
        if not isinstance(resource, str):
            raise ValueError(
                f"resource must be string, but found '{resource} {type(resource)}'."
            )

        # handle urls
        if resource.startswith("http"):
            # tests new compact patterns
            match_compact = IDENTIFIERS_ORG_PATTERN_COMPACT.match(resource)
            if match_compact:
                self.collection = match_compact.group(1).lower()
                self.term = f"{match_compact.group(1)}:{match_compact.group(2)}"
                self.provider = ProviderType.IDENTIFIERS_ORG

            if not self.collection:
                match_classic = IDENTIFIERS_ORG_PATTERN_CLASSIC.match(resource)
                if match_classic:
                    self.collection = match_classic.group(1).lower()
                    self.term = match_classic.group(2)
                    self.provider = ProviderType.IDENTIFIERS_ORG

            if not self.collection:
                # other urls are directly stored as resources without collection
                self.collection = None
                self.term = resource
                if BIOREGISTRY_PATTERN.match(resource):
                    self.provider = ProviderType.BIOREGISTRY_IO
                else:
                    self.provider = ProviderType.NONE
                    logger.debug(
                        "%s does not conform to http(s)://identifiers.org/collection/id or http(s)://identifiers.org/id or https://bioregistry.io/id .",
                        resource,
                    )

        # handle urns
        elif resource.startswith("urn:miriam:"):
            match3 = MIRIAM_URN_PATTERN.match(resource)
            if match3:
                tokens = match3.group(1).split(":")
                self.collection = tokens[0]
                self.term = ":".join(tokens[1:]).replace("%3A", ":")
                self.provider = ProviderType.IDENTIFIERS_ORG

                logger.warning(
                    "Deprecated urn pattern `%s` updated: %s",
                    resource,
                    self.resource_normalized,
                )

        else:
            # handle short notation
            tokens = resource.split("/")
            if len(tokens) > 1:
                self.collection = tokens[0]
                self.term = "/".join(tokens[1:])
                self.provider = ProviderType.IDENTIFIERS_ORG
            elif len(tokens) == 1 and ":" in tokens[0]:
                self.collection = tokens[0].split(":")[0].lower()
                self.term = tokens[0]
                self.provider = ProviderType.IDENTIFIERS_ORG

            # validation
            if len(tokens) < 2 and not self.collection:
                logger.error(
                    "Resource `%s` could not be split in collection and term. A given resource must be of the form `collection/term` or an url starting with `http(s)://`)",
                    resource,
                )
                self.collection = None
                self.term = resource
                self.provider = ProviderType.NONE

        # shorten compact terms
        if self.term and self.collection:
            self.term = self.shorten_compact_term(
                term=self.term, collection=self.collection
            )

        # clean legacy collections
        if self.collection in self.replaced_collections:
            self.collection = self.replaced_collections[self.collection]

        if validate:
            self.validate()

    @staticmethod
    def shorten_compact_term(term: str, collection: str) -> str:
        """Shorten the compact terms and return term.

        If the namespace is not embedded in the term return the shortened term.
        """
        namespace = get_registry().ns_dict.get(collection, None)
        if (
            namespace
            and not namespace.namespaceEmbeddedInLui
            and term.lower().startswith(f"{collection}:")
        ):
            tokens = term.split(":")
            term = ":".join(tokens[1:])

        return term

    @staticmethod
    def from_tuple(t: tuple[BQB | BQM, str]) -> "RDFAnnotation":
        """Create an annotation from a `(qualifier, resource)` tuple."""
        qualifier, resource = t[0], t[1]
        return RDFAnnotation(qualifier=qualifier, resource=resource)

    @property
    def resource_normalized(self) -> str | None:
        """Normalize resource for given annotation.

        This is the correct usage. Resources are normalized to identifiers.org
        compact identifiers of the form
        `https://identifiers.org/<prefix>:<accession>`. If the namespace is
        embedded in the LUI the prefix is already part of the term, otherwise
        the prefix of the identifiers.org registry is prepended.
        """
        if not self.term:
            return None

        if (
            self.provider == ProviderType.IDENTIFIERS_ORG
            and self.collection is not None
        ):
            namespace = get_registry().ns_dict.get(self.collection, None)
            if namespace:
                if namespace.namespaceEmbeddedInLui:
                    return f"{IDENTIFIERS_ORG_PREFIX}/{self.term}"
                return f"{IDENTIFIERS_ORG_PREFIX}/{self.collection}:{self.term}"

        return self.term

    def __repr__(self) -> str:
        """Get representation string."""
        return f"RDFAnnotation({self.qualifier}|{self.collection}|{self.term}|{self.provider.value})"

    def to_dict(self) -> dict:
        """Convert the annotation to a dictionary."""
        return {
            "qualifier": self.qualifier.value,
            "collection": self.collection,
            "term": self.term,
        }

    def check_miriam_term(self) -> bool:
        """Check that term follows id pattern for collection.

        Uses the Identifiers collection information.
        """
        if self.provider != ProviderType.IDENTIFIERS_ORG:
            return False

        # find the miriam namespace
        if self.collection:
            namespace: Namespace | None = get_registry().ns_dict.get(
                self.collection, None
            )
            if not namespace:
                logger.error(
                    "MIRIAM namespace `%s` does not exist for `%s`",
                    self.collection,
                    self,
                )
                return False
        else:
            return False

        # check the pattern
        if self.term:
            p = re.compile(namespace.pattern)
            m = p.match(self.term)
            if not m:
                logger.error(
                    "Term `%s` did not match pattern `%s` for collection `%s`.",
                    self.term,
                    namespace.pattern,
                    self.collection,
                )
                return False
        else:
            return False

        return True

    @staticmethod
    def check_qualifier(qualifier: BQB | BQM) -> bool:
        """Check that the qualifier is a MIRIAM qualifier.

        Args:
            qualifier: qualifier to check

        Returns:
            True if the qualifier is a `BQB` or `BQM` term.
        """
        if not isinstance(qualifier, (BQB, BQM)):
            supported_qualifiers = [e.value for e in BQB] + [e.value for e in BQM]

            logger.error(
                "qualifier `%s` is not in supported qualifiers: '%s'.",
                qualifier,
                supported_qualifiers,
            )
            return False

        return True

    def validate(self) -> bool:
        """Validate qualifier and term of the annotation.

        Returns:
            True if the qualifier is a MIRIAM qualifier and the term matches the
            pattern of its collection.
        """
        valid_qualifier: bool = False
        if self.qualifier:
            valid_qualifier = self.check_qualifier(self.qualifier)
        valid_term: bool = True
        if self.collection and self.term:
            valid_term = self.check_miriam_term()

        return valid_qualifier and valid_term


class RDFAnnotationData(RDFAnnotation):
    """An annotation with the information behind the identifier resolved.

    Constructing the object resolves the cross references: for every provider
    the identifiers.org registry lists for the collection, the url pattern is
    filled in with the term. `query_ols` then adds label, description and
    synonyms from the Ontology Lookup Service, and replaces `xrefs` with the
    cross references reported by OLS.

    Attributes:
        url: url of the first provider of the collection
        label: name of the term
        description: definition of the term
        synonyms: synonyms of the term
        xrefs: cross references of the term
        warnings: problems which do not invalidate the annotation
        errors: problems which do

    Example:
        ```python
        data = RDFAnnotationData(RDFAnnotation(BQB.IS, "chebi/CHEBI:33699"))
        data.query_ols()
        print(data.label)
        ```

    Raises:
        ValueError: if the collection of the annotation is not in the registry
    """

    def __init__(self, annotation: RDFAnnotation):
        """Resolve the cross references of the annotation."""
        self.resource = annotation.resource
        self.qualifier = annotation.qualifier
        self.collection = annotation.collection
        self.term: str | None = annotation.term
        self.url: str | None = None
        self.description: str | None = None
        self.label: str | None = None
        self.synonyms: list = []
        self.xrefs: list = []
        self.warnings: list = []
        self.errors: list = []

        if self.collection:
            # register MIRIAM xrefs
            namespace = get_registry().ns_dict.get(self.collection, None)
            if not namespace:
                raise ValueError(
                    f"Namespace does not exist in dict for: `{self.collection}`"
                )

            namespace_embedded = namespace.namespaceEmbeddedInLui

            if not namespace.resources:
                namespace.resources = []

            for ns_resource in namespace.resources:
                # create url
                url = ns_resource.urlPattern

                if not self.term:
                    continue

                term = self.term

                # remove prefix
                if namespace_embedded and namespace.prefix:
                    term = term[len(namespace.prefix) + 1 :]

                # urlencode term
                term = urllib.parse.quote(term)

                # create url
                url = url.replace("{$Id}", term)
                url = url.replace("{$id}", term)
                if namespace.prefix:
                    url = url.replace(
                        f"{namespace.prefix.upper}:",
                        urllib.parse.quote(f"{namespace.prefix.upper}:"),
                    )

                if not self.url:
                    # set url to first resource url
                    self.url = url

                # print(url)
                _xref = CrossReference(
                    name=ns_resource.name, accession=self.term, url=url
                )
                valid = _xref.validate() and is_url(self.url)
                if valid:
                    self.xrefs.append(_xref)

        # query OLS information
        self.query_ols()

    def __repr__(self) -> str:
        """Get the string representation of the resolved annotation."""
        return f"RDFAnnotationData({self.collection}|{self.term}|{self.label}|{self.description}|{self.synonyms}|{self.xrefs})"

    def to_dict(self) -> dict[str, Any]:
        """Convert the annotation to a dictionary."""
        return {
            "resource": self.resource,
            "resource_normalized": self.resource_normalized,
            # "qualifier": self.qualifier.value,
            "collection": self.collection,
            "term": self.term,
            "label": self.label,
            "description": self.description,
            "url": self.url,
            "synonyms": self.synonyms,
            "xrefs": self.xrefs,
            "errors": self.errors,
            "warnings": self.warnings,
        }

    def query_ols(self) -> dict:
        """Resolve the term in the Ontology Lookup Service.

        Fills in `label`, `description` and `synonyms`, and replaces `xrefs`
        with the cross references reported by OLS. Requires network access;
        errors are collected in `errors` instead of raising.

        Returns:
            The processed OLS response.
        """
        try:
            d = get_ols_query().query_ols(ontology=self.collection, term=self.term)
        except requests.HTTPError as err:
            logger.error(err)
            d = {
                "errors": [err],
                "warnings": [],
            }

        info = get_ols_query().process_response(d)

        if self.label is None:
            self.label = info["label"]

        if self.description is None:
            self.description = info["description"]

        self.synonyms = info["synonyms"]
        self.xrefs = info["xrefs"]
        self.warnings.extend(info["warnings"])
        self.errors.extend(info["errors"])

        return info


if __name__ == "__main__":
    for annotation in [
        RDFAnnotation(
            qualifier=BQB.IS_VERSION_OF,
            resource="https://identifiers.org/DOI:10.1016/j.jtbi.2004.04.039",
        ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="hmdb/HMDB0000122",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="https://bioregistry.io/chebi:15996",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="NCIT:C75913",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="ncit:C75913",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="taxonomy/562",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="http://identifiers.org/taxonomy/9606",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="http://identifiers.org/biomodels.sbo/SBO:0000247",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF, resource="urn:miriam:obo.go:GO%3A0005623"
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF, resource="urn:miriam:chebi:CHEBI%3A33699"
        # ),
        # RDFAnnotation(qualifier=BQB.IS_VERSION_OF, resource="chebi/CHEBI:456215"),
        # RDFAnnotation(
        #     qualifier=BQB.IS, resource="https://en.wikipedia.org/wiki/Cytosol"
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF, resource="urn:miriam:uniprot:P03023"
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF,
        #     resource="http://identifiers.org/go/GO:0005829",
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF, resource="http://identifiers.org/go/GO:0005829"
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF, resource="http://identifiers.org/GO:0005829"
        # ),
        # RDFAnnotation(
        #     qualifier=BQB.IS_VERSION_OF, resource="http://identifiers.org/GO:0005829"
        # ),
        # RDFAnnotation(qualifier=BQB.IS_VERSION_OF, resource="bto/BTO:0000089"),
        # RDFAnnotation(qualifier=BQB.IS_VERSION_OF, resource="BTO:0000089"),
        # RDFAnnotation(qualifier=BQB.IS_VERSION_OF, resource="chebi/CHEBI:000012"),
    ]:
        print("-" * 80)
        data = RDFAnnotationData(annotation)
        print(data)
        pprint(data.to_dict())
