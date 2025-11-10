"""Annotation.

Core data structure to store annotations.
"""

import re
import urllib
from enum import Enum
from pprint import pprint
from typing import Any, Dict, Final, List, Optional, Tuple, Union

import requests

from pymetadata import log
from pymetadata.core.xref import CrossReference, is_url
from pymetadata.identifiers.miriam import BQB, BQM
from pymetadata.identifiers.registry import REGISTRY, Namespace
from pymetadata.ontologies.ols import ONTOLOGIES, OLSQuery


OLS_QUERY = OLSQuery(ontologies=ONTOLOGIES)

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
    """Provider type."""

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

    replaced_collections: Dict[str, str] = {
        "obo.go": "go",
        "biomodels.sbo": "sbo",
    }

    def __init__(
        self, qualifier: Union[BQB, BQM], resource: str, validate: bool = True
    ):
        """Initialize RDFAnnotation."""
        self.qualifier: Union[BQB, BQM] = qualifier
        self.collection: Optional[str] = None
        self.term: Optional[str] = None
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
                        f"{resource} does not conform to "
                        f"http(s)://identifiers.org/collection/id or http(s)://identifiers.org/id or "
                        f"https://bioregistry.io/id .",
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
                    f"Deprecated urn pattern `{resource}` updated: "
                    f"{self.resource_normalized}"
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
                    f"Resource `{resource}` could not be split in collection and term. "
                    f"A given resource must be of the form "
                    f"`collection/term` or an url starting with "
                    f"`http(s)://`)"
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
        namespace = REGISTRY.ns_dict.get(collection, None)
        if namespace and not namespace.namespaceEmbeddedInLui:
            # shorter term
            if term.lower().startswith(f"{collection}:"):
                tokens = term.split(":")
                term = ":".join(tokens[1:])

        return term

    @staticmethod
    def from_tuple(t: Tuple[Union[BQB, BQM], str]) -> "RDFAnnotation":
        """Construct from tuple."""
        qualifier, resource = t[0], t[1]
        return RDFAnnotation(qualifier=qualifier, resource=resource)

    @property
    def resource_normalized(self) -> Optional[str]:
        """Normalize resource for given annotation.

        This is the correct usage.
        """
        if not self.term:
            return None

        if self.provider == ProviderType.IDENTIFIERS_ORG:
            if self.collection is not None:
                namespace = REGISTRY.ns_dict.get(self.collection, None)
                if namespace:
                    if namespace.namespaceEmbeddedInLui:
                        return f"{IDENTIFIERS_ORG_PREFIX}/{self.term}"
                    else:
                        return f"{IDENTIFIERS_ORG_PREFIX}/{self.collection}/{self.term}"

        return self.term

    def __repr__(self) -> str:
        """Get representation string."""
        return f"RDFAnnotation({self.qualifier}|{self.collection}|{self.term}|{self.provider.value})"

    def to_dict(self) -> Dict:
        """Convert to dict."""
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
            namespace: Optional[Namespace] = REGISTRY.ns_dict.get(self.collection, None)
            if not namespace:
                logger.error(
                    f"MIRIAM namespace `{self.collection}` does not exist for `{self}`"
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
                    f"Term `{self.term}` did not match pattern `{namespace.pattern}` for collection `{self.collection}`."
                )
                return False
        else:
            return False

        return True

    @staticmethod
    def check_qualifier(qualifier: Union[BQB, BQM]) -> bool:
        """Check that the qualifier is an allowed qualifier.

        :param qualifier:
        :return:
        """
        if not isinstance(qualifier, (BQB, BQM)):
            supported_qualifiers = [e.value for e in BQB] + [e.value for e in BQM]

            logger.error(
                f"qualifier `{qualifier}` is not in supported qualifiers: '{supported_qualifiers}'."
            )
            return False

        return True

    def validate(self) -> bool:
        """Validate annotation."""
        valid_qualifier: bool = False
        if self.qualifier:
            valid_qualifier = self.check_qualifier(self.qualifier)
        valid_term: bool = True
        if self.collection and self.term:
            valid_term = self.check_miriam_term()

        return valid_qualifier and valid_term


class RDFAnnotationData(RDFAnnotation):
    """Annotation with resolved information.

    queries for the resource should happen here;
    this resolves additional information.
    """

    def __init__(self, annotation: RDFAnnotation):
        """Initialize RDFAnnotationData."""
        self.resource = annotation.resource
        self.qualifier = annotation.qualifier
        self.collection = annotation.collection
        self.term: Optional[str] = annotation.term
        self.url: Optional[str] = None
        self.description: Optional[str] = None
        self.label: Optional[str] = None
        self.synonyms: List = []
        self.xrefs: List = []
        self.warnings: List = []
        self.errors: List = []

        if self.collection:
            # register MIRIAM xrefs
            namespace = REGISTRY.ns_dict.get(self.collection, None)
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
                valid = _xref.validate() and is_url(self.url)  # type: ignore
                if valid:
                    self.xrefs.append(_xref)

        # query OLS information
        self.query_ols()

    def __repr__(self) -> str:
        """Get representation string."""
        return f"RDFAnnotationData({self.collection}|{self.term}|{self.label}|{self.description}|{self.synonyms}|{self.xrefs})"

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dict."""

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

    def query_ols(self) -> Dict:
        """Query ontology lookup service."""
        try:
            d = OLS_QUERY.query_ols(ontology=self.collection, term=self.term)
        except requests.HTTPError as err:
            logger.error(err)
            d = {
                "errors": [err],
                "warnings": [],
            }

        info = OLS_QUERY.process_response(d)

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
