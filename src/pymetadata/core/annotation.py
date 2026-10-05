"""MIRIAM annotations.

An annotation combines a qualifier (`BQB`, `BQM`) with a resource pointing at a
database entry, forming the statement *this element **is** CHEBI:17234*.

`RDFAnnotation` parses the notations found in the wild, normalizes them to
identifiers.org compact identifiers and validates them against the
identifiers.org registry. `RDFAnnotationData` resolves what an identifier refers
to via the Ontology Lookup Service.

```python
from pymetadata.core.annotation import RDFAnnotation
from pymetadata.core.miriam import BQB

annotation = RDFAnnotation(qualifier=BQB.IS, resource="chebi/CHEBI:33699")
print(annotation.resource_normalized)  # https://identifiers.org/CHEBI:33699
print(annotation.validate())
```
"""

import logging
import re
import urllib.parse
from dataclasses import asdict, dataclass
from enum import Enum
from functools import lru_cache
from pprint import pprint
from typing import Any, ClassVar, Final

from pymetadata.core.miriam import BQB, BQM
from pymetadata.core.xref import CrossReference, is_url
from pymetadata.webservices.ols import ONTOLOGIES, OLSQuery
from pymetadata.webservices.registry import Namespace, Resource, get_registry

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
# prefixes of the registry consist of letters, digits, `.`, `_` and `-`,
# e.g., `ec-code` or `go_ref`; query string, fragment and a trailing `/` are
# not part of the term
_TERM_PATTERN: Final = r"([^?#]+?)/?(?:[?#].*)?$"
IDENTIFIERS_ORG_PATTERN_COMPACT: Final = re.compile(
    rf"^https?://identifiers\.org/([a-zA-Z0-9._-]+):{_TERM_PATTERN}", re.IGNORECASE
)
IDENTIFIERS_ORG_PATTERN_CLASSIC: Final = re.compile(
    rf"^https?://identifiers\.org/([a-zA-Z0-9._-]+)/{_TERM_PATTERN}", re.IGNORECASE
)

BIOREGISTRY_PREFIX: Final = "https://bioregistry.io"
BIOREGISTRY_PATTERN: Final = re.compile(
    rf"^https?://bioregistry\.io/([a-zA-Z0-9._-]+):{_TERM_PATTERN}", re.IGNORECASE
)

MIRIAM_URN_PATTERN: Final = re.compile(r"^urn:miriam:(.+)")

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1024)
def _compile_pattern(pattern: str) -> re.Pattern[str]:
    """Compile a pattern of the identifiers.org registry.

    Args:
        pattern: regular expression of a registry namespace

    Returns:
        The compiled regular expression.
    """
    return re.compile(pattern)


# characters of a term which would start the query string or the fragment of
# an url, they are percent-encoded when the term is part of an url
_URL_TERM_ESCAPES: Final = {"?": "%3F", "#": "%23"}


def _encode_url_term(term: str) -> str:
    """Percent-encode the characters of a term which end the path of an url.

    Args:
        term: term to write into an url

    Returns:
        The term with `?` and `#` percent-encoded.
    """
    for char, escaped in _URL_TERM_ESCAPES.items():
        term = term.replace(char, escaped)
    return term


def _decode_url_term(term: str) -> str:
    """Decode the characters which `_encode_url_term` percent-encodes.

    Only `?` and `#` are decoded, since other percent-encodings can be part
    of a term, e.g., `--%3E` of `datanator.reaction`.

    Args:
        term: term read from an url

    Returns:
        The term with `?` and `#` decoded.
    """
    for char, escaped in _URL_TERM_ESCAPES.items():
        term = re.sub(re.escape(escaped), char, term, flags=re.IGNORECASE)
    return term


def _is_http_url(resource: str) -> bool:
    """Check if a resource is an http(s) url.

    Args:
        resource: resource to check

    Returns:
        True if the scheme of the resource is `http` or `https`.
    """
    try:
        scheme = urllib.parse.urlparse(resource).scheme
    except ValueError:
        return False
    return scheme.lower() in {"http", "https"}


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

        if not isinstance(qualifier, BQB | BQM):
            raise ValueError(
                f"MIRIAM qualifiers are required for rdf annotation, but "
                f"'{qualifier}' was provided for resource '{resource}'."
            )
        if not resource:
            raise ValueError(
                f"resource is required for annotation, but resource is empty "
                f"'{qualifier} {resource}'."
            )
        if not isinstance(resource, str):
            raise ValueError(
                f"resource must be string, but found '{resource} {type(resource)}'."
            )

        # handle urls
        if _is_http_url(resource):
            # tests new compact patterns
            match_compact = IDENTIFIERS_ORG_PATTERN_COMPACT.match(resource)
            if match_compact:
                self.collection = match_compact.group(1).lower()
                self.term = _decode_url_term(
                    f"{match_compact.group(1)}:{match_compact.group(2)}"
                )
                self.provider = ProviderType.IDENTIFIERS_ORG

            if not self.collection:
                match_classic = IDENTIFIERS_ORG_PATTERN_CLASSIC.match(resource)
                if match_classic:
                    self.collection = match_classic.group(1).lower()
                    self.term = _decode_url_term(match_classic.group(2))
                    self.provider = ProviderType.IDENTIFIERS_ORG

            if not self.collection:
                # other urls are directly stored as resources without collection
                self.collection = None
                self.term = resource
                match_bioregistry = BIOREGISTRY_PATTERN.match(resource)
                if match_bioregistry:
                    self.collection = match_bioregistry.group(1).lower()
                    self.term = (
                        f"{match_bioregistry.group(1)}:{match_bioregistry.group(2)}"
                    )
                    self.provider = ProviderType.BIOREGISTRY_IO
                else:
                    self.provider = ProviderType.NONE
                    logger.debug(
                        "%s does not conform to http(s)://identifiers.org/collection/id or http(s)://identifiers.org/id or https://bioregistry.io/id .",
                        resource,
                    )

        # other urls, e.g., ftp, are kept as they are
        elif "://" in resource:
            self.term = resource
            self.provider = ProviderType.NONE

        # handle urns
        elif resource.startswith("urn:miriam:"):
            match3 = MIRIAM_URN_PATTERN.match(resource)
            if match3:
                tokens = match3.group(1).split(":")
                self.collection = tokens[0].lower()
                self.term = urllib.parse.unquote(":".join(tokens[1:]))
                self.provider = ProviderType.IDENTIFIERS_ORG

        else:
            # handle short notation, a `:` before the first `/` marks a compact
            # identifier such as `doi:10.1016/j.jtbi.2004.04.039`
            head, sep, tail = resource.partition("/")
            if ":" in head:
                self.collection = head.split(":")[0].lower()
                self.term = resource
                self.provider = ProviderType.IDENTIFIERS_ORG
            elif sep:
                self.collection = head.lower()
                self.term = tail
                self.provider = ProviderType.IDENTIFIERS_ORG

            # validation
            if not self.collection:
                logger.error(
                    "Resource `%s` could not be split in collection and term. A given resource must be of the form `collection/term` or an url starting with `http(s)://`)",
                    resource,
                )
                self.collection = None
                self.term = resource
                self.provider = ProviderType.NONE

        # clean legacy collections
        if self.collection in self.replaced_collections:
            self.collection = self.replaced_collections[self.collection]

        # shorten compact terms
        if (
            self.term
            and self.collection
            and self.provider == ProviderType.IDENTIFIERS_ORG
        ):
            self.term = self.shorten_compact_term(
                term=self.term, collection=self.collection
            )

        if resource.startswith("urn:miriam:"):
            logger.warning(
                "Deprecated urn pattern `%s` updated: %s",
                resource,
                self.resource_normalized,
            )

        if validate:
            self.validate()

    @staticmethod
    def shorten_compact_term(term: str, collection: str) -> str:
        """Shorten a compact term to the accession.

        If the namespace is not embedded in the LUI, the prefix of the
        collection is removed from the term, e.g., `ncit:C75913` becomes
        `C75913`.

        Args:
            term: term, possibly with the prefix of its collection
            collection: collection of the term

        Returns:
            The term without the prefix if the namespace is not embedded in the
            LUI, otherwise the unchanged term.
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
        """Create an annotation from a `(qualifier, resource)` tuple.

        Args:
            t: qualifier and resource of the annotation

        Returns:
            The annotation.
        """
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

        The normalization never changes what the resource says: the result is
        an url, and parsing it again yields the same `collection` and `term`.
        A `?` or `#` of the term is percent-encoded, since it would otherwise
        start the query string or the fragment of the url.
        A collection which is not in the registry, or a term which does not
        carry the prefix of its collection, can not be written as a compact
        identifier and is returned as
        `https://identifiers.org/<collection>/<term>`. Whether the term is
        valid does not matter here, this is the task of `validate`.

        Bioregistry URLs retain their original resource while exposing their
        collection and compact term for OLS resolution. Arbitrary URLs are also
        returned unchanged.
        """
        if not self.term:
            return None

        if self.provider == ProviderType.BIOREGISTRY_IO:
            return self.resource
        if self.provider != ProviderType.IDENTIFIERS_ORG or self.collection is None:
            return self.term

        term = _encode_url_term(self.term)
        namespace = get_registry().ns_dict.get(self.collection, None)
        if namespace and not namespace.namespaceEmbeddedInLui:
            return f"{IDENTIFIERS_ORG_PREFIX}/{self.collection}:{term}"

        # the term is only a compact identifier if its prefix is the collection
        if self.term.lower().startswith(f"{self.collection}:"):
            return f"{IDENTIFIERS_ORG_PREFIX}/{term}"

        return f"{IDENTIFIERS_ORG_PREFIX}/{self.collection}/{term}"

    def __repr__(self) -> str:
        """Get representation string."""
        return f"RDFAnnotation({self.qualifier}|{self.collection}|{self.term}|{self.provider.value})"

    def to_dict(self) -> dict[str, Any]:
        """Convert the annotation to a dictionary.

        Returns:
            Qualifier, collection and term of the annotation.
        """
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
            if not _compile_pattern(namespace.pattern).fullmatch(self.term):
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
            True if the qualifier is a MIRIAM qualifier and an identifiers.org
            term matches its collection pattern. Bioregistry.io resources do not
            use identifiers.org term validation, other resources must be urls.
        """
        valid_qualifier: bool = self.check_qualifier(self.qualifier)
        valid_term: bool = True
        if self.provider == ProviderType.IDENTIFIERS_ORG:
            valid_term = self.check_miriam_term()
        elif self.provider == ProviderType.NONE:
            valid_term = bool(self.term) and is_url(self.term or "")
            if not valid_term:
                logger.error(
                    "Resource `%s` is neither an identifier nor an url.",
                    self.resource,
                )

        return valid_qualifier and valid_term


@dataclass
class Provider:
    """A provider which resolves the term of an annotation.

    Attributes:
        name: name of the provider, e.g., `UniProt`
        url: url of the term at the provider
        official: whether the registry names it the official provider
    """

    name: str
    url: str
    official: bool


def primary_resource(resources: list[Resource]) -> Resource | None:
    """Get the provider a term links to: the official non deprecated one.

    Falls back to the first non deprecated provider, and to the first provider
    when all are deprecated.
    """
    active = [resource for resource in resources if not resource.deprecated]
    for resource in active:
        if resource.official:
            return resource
    if active:
        return active[0]
    return resources[0] if resources else None


def pattern_matches(pattern: str | None, term: str | None) -> bool | None:
    """Check a term against the pattern of its collection, None if it cannot be checked."""
    if not pattern or not term:
        return None
    try:
        return re.match(pattern, term) is not None
    except re.error:
        return None


class RDFAnnotationData(RDFAnnotation):
    """An annotation with the information behind the identifier resolved.

    Constructing the object resolves the cross references: for every provider
    the identifiers.org registry lists for the collection, the url pattern is
    filled in with the term. `query_ols` then adds label, description and
    synonyms from the Ontology Lookup Service, and replaces `xrefs` with the
    cross references reported by OLS.

    Attributes:
        url: url of the primary provider of the collection
        providers: non deprecated providers, the primary one first
        collection_name: name of the collection, e.g., `UniProt Knowledgebase`
        collection_homepage: homepage of the primary provider
        pattern_match: whether the term matches the pattern of the collection,
            None if it cannot be checked
        label: name of the term
        ontology: ontology id of the term in OLS, e.g., `go`
        iri: IRI of the term
        ols_url: page of the term in OLS
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
        self.provider = annotation.provider
        self.url: str | None = None
        self.providers: list[Provider] = []
        self.collection_name: str | None = None
        self.collection_homepage: str | None = None
        self.pattern_match: bool | None = None
        self.description: str | None = None
        self.label: str | None = None
        self.ontology: str | None = None
        self.iri: str | None = None
        self.ols_url: str | None = None
        self.synonyms: list[Any] = []
        self.xrefs: list[Any] = []
        self.warnings: list[Any] = []
        self.errors: list[Any] = []

        if self.collection and self.provider == ProviderType.IDENTIFIERS_ORG:
            # register MIRIAM xrefs
            namespace = get_registry().ns_dict.get(self.collection, None)
            if not namespace:
                raise ValueError(
                    f"Namespace does not exist in dict for: `{self.collection}`"
                )

            namespace_embedded = namespace.namespaceEmbeddedInLui

            if not namespace.resources:
                namespace.resources = []

            urls: dict[int, str] = {}
            for ns_resource in namespace.resources:
                # create url
                url = ns_resource.urlPattern

                if not self.term:
                    continue

                term = self.term

                # remove the embedded prefix, the url pattern contains it
                if (
                    namespace_embedded
                    and namespace.prefix
                    and term.lower().startswith(f"{namespace.prefix.lower()}:")
                ):
                    term = term[len(namespace.prefix) + 1 :]

                # urlencode term
                term = urllib.parse.quote(term)

                # create url
                url = url.replace("{$Id}", term)
                url = url.replace("{$id}", term)

                urls[id(ns_resource)] = url

                # print(url)
                _xref = CrossReference(
                    name=ns_resource.name, accession=self.term, url=url
                )
                valid = _xref.validate() and is_url(url)
                if valid:
                    self.xrefs.append(_xref)

            primary = primary_resource(namespace.resources)
            self.collection_name = namespace.name
            self.pattern_match = pattern_matches(namespace.pattern, self.term)
            if primary is not None:
                self.collection_homepage = primary.resourceHomeUrl
                self.url = urls.get(id(primary))
            active = [
                r for r in namespace.resources if not r.deprecated and id(r) in urls
            ]
            active.sort(key=lambda r: r is not primary)
            self.providers = [
                Provider(name=r.name, url=urls[id(r)], official=bool(r.official))
                for r in active
            ]

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
            "ontology": self.ontology,
            "iri": self.iri,
            "ols_url": self.ols_url,
            "description": self.description,
            "url": self.url,
            "providers": [asdict(p) for p in self.providers],
            "collection_name": self.collection_name,
            "collection_homepage": self.collection_homepage,
            "pattern_match": self.pattern_match,
            "synonyms": self.synonyms,
            "xrefs": self.xrefs,
            "errors": self.errors,
            "warnings": self.warnings,
        }

    def query_ols(self) -> dict[str, Any]:
        """Resolve the term in the Ontology Lookup Service.

        Fills in `label`, `description` and `synonyms`, and replaces `xrefs`
        with the cross references reported by OLS. Requires network access;
        errors are collected in `errors` instead of raising.

        Returns:
            The processed OLS response.
        """
        d = get_ols_query().query_ols(ontology=self.collection, term=self.term)
        info = get_ols_query().process_response(d)

        if self.label is None:
            self.label = info["label"]

        if self.description is None:
            self.description = info["description"]

        self.ontology = info.get("ontology")
        self.iri = info.get("iri")
        self.ols_url = info.get("ols_url")
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
