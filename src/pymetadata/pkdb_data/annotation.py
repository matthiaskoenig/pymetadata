"""Annotation helpers."""
import logging
import re
import urllib
from dataclasses import dataclass
from enum import Enum

from pymetadata.pkdb_data.ols import ONTOLOGIES, OLSQuery
from pymetadata.pkdb_data.registry import Registry
from pymetadata.pkdb_data.xref import CrossReference, is_url


logger = logging.getLogger(__name__)

REGISTRY = Registry()
OLS_QUERY = OLSQuery(ontologies=ONTOLOGIES)


class BQB(Enum):
    """Biological qualifier."""

    IS = "BQB_IS"
    HAS_PART = "BQB_HAS_PART"
    IS_PART_OF = "BQB_IS_PART_OF"
    IS_VERSION_OF = "BQB_IS_VERSION_OF"
    HAS_VERSION = "BQB_HAS_VERSION"
    IS_HOMOLOG_TO = "BQB_IS_HOMOLOG_TO"
    IS_DESCRIBED_BY = "BQB_IS_DESCRIBED_BY"
    IS_ENCODED_BY = "BQB_IS_ENCODED_BY"
    ENCODES = "BQB_ENCODES"
    OCCURS_IN = "BQB_OCCURS_IN"
    HAS_PROPERTY = "BQB_HAS_PROPERTY"
    IS_PROPERTY_OF = "BQB_IS_PROPERTY_OF"
    HAS_TAXON = "BQB_HAS_TAXON"
    UNKNOWN = "BQB_UNKNOWN"


class Annotation(object):
    """Annotation."""

    def __init__(self, relation, resource, url=None, description=None, label=None):
        self.relation = relation
        self.description = description
        self.label = label
        self.url = None
        self.synonyms = []
        self.xrefs = []

        # get the collection/term part from identifiers.org urls
        for prefix in ["http://identifiers.org/", "https://identifiers.org/"]:
            if resource.startswith(prefix):
                resource = resource.replace(prefix, "")

        # other urls are directly stored as resources
        if resource.startswith("http"):
            self.collection = None
            self.term = resource
        else:
            # get term and collection
            tokens = resource.split("/")
            if len(tokens) < 2:
                raise ValueError(
                    f"resource `{resource}` must be of the form "
                    f"`collection/term` or an url starting with `http`)"
                )
            self.collection = tokens[0]
            self.term = "/".join(tokens[1:])

        self.validate()

        if self.collection:

            # register MIRIAM xrefs
            namespace = REGISTRY.ns_dict.get(self.collection)
            namespace_embedded = namespace.namespaceEmbeddedInLui
            # print("-" * 80)
            # print(namespace.prefix, "embedded=", namespace_embedded)

            for resource in namespace.resources:  # Resource

                # create url
                url = resource.urlPattern
                term = self.term

                # remove prefix
                if namespace_embedded:
                    term = term[len(namespace.prefix) + 1 :]

                # urlencode term
                term = urllib.parse.quote(term)

                # create url
                url = url.replace("{$Id}", term)
                url = url.replace("{$id}", term)
                url = url.replace(
                    f"{prefix.upper}:", urllib.parse.quote(f"{prefix.upper}:")
                )

                if not self.url:
                    # set url to first resource url
                    self.url = url

                # print(url)
                _xref = CrossReference(name=resource.name, accession=self.term, url=url)
                valid = _xref.validate() and is_url(self.url)
                if valid:
                    self.xrefs.append(_xref)

    def query_ols(self):
        """Query ontology lookup service."""
        d = OLS_QUERY.query_ols(ontology=self.collection, term=self.term)
        info = OLS_QUERY.process_response(d)
        if info is not None:
            if self.label is None:
                self.label = info.get("label")

            if self.description is None:
                self.description = info.get("description")

            # TODO: process synonmys and xrefs
            self.synonyms = info["synonyms"]
            self.xrefs = info["xrefs"]

        return info

    def __repr__(self):
        """Get representation string."""
        return f"Annotation({self.collection}|{self.term}|{self.description}|{self.synonyms}|{self.xrefs})"

    def to_dict(self):
        """Convert to dict."""
        return {
            "term": self.term,
            "relation": self.relation.value,
            "collection": self.collection,
            "description": self.description,
            "label": self.label,
            "url": self.url,
            # synonyms and xrefs are not serialized
        }

    @staticmethod
    def check_term(collection, term):
        """Check that a given term follows id pattern for existing collection."""
        namespace = REGISTRY.ns_dict.get(collection, None)
        if not namespace:
            raise ValueError(
                f"MIRIAM collection `{collection}` does not exist for term `{term}`"
            )

        p = re.compile(namespace.pattern)
        m = p.match(term)
        if not m:
            raise ValueError(
                f"Term `{term}` did not match pattern "
                f"`{namespace.pattern}` for collection `{collection}`."
            )
            return False

        return True

    @staticmethod
    def check_qualifier(qualifier) -> None:
        """Check that the qualifier is an allowed qualifier."""
        if not isinstance(qualifier, BQB):
            raise ValueError(
                f"relation `{qualifier}``> is not in allowed qualifiers: "
                f"{[e.value for e in BQB]}"
            )

    def validate(self) -> None:
        """Validate."""
        self.check_qualifier(self.relation)
        if self.collection:
            self.check_term(collection=self.collection, term=self.term)
