"""Annotation of SBML models.

Handle the XML annotations and notes in SBML.
Annotate models from information in annotation csv files.
Thereby a model can be fully annotated from information
stored in a separate annotation store.

Annotation is performed via searching for ontology terms which describe the model and
model components.
A standard workflow is looking up the components for instance in things like OLS
ontology lookup service.
"""
import logging
import os
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple, Union

import pandas as pd

from .miriam import (
    BQB,
    BQM,
    IDENTIFIERS_ORG_PATTERN,
    IDENTIFIERS_ORG_PREFIX,
    MIRIAM_COLLECTION,
)


logger = logging.getLogger(__name__)


class Annotation:
    """Annotation class.

    Basic storage of annotation information. This consists of the relation
    and the the resource.
    The annotations can be attached to other objects thereby forming
    triples which can be converted to RDF.

    Resource can be either:
        - `http(s)://identifiers.org/collection/term`, i.e., a identifiers.org URI
        - `collection/term`, i.e., the combination of collection and term
        - `http(s)://arbitrary.url`, an arbitrary URL

    TODO: load the xrefs, synonyms and definitions from OLS
    """

    def __init__(self, qualifier: Union[BQB, BQM], resource: str):
        """Initialize annotation.

        :param qualifier: BQM or BQB term
        :param resource:
        """
        if not qualifier:
            raise ValueError(
                "MIRIAM qualifiers are required for annotation, but no "
                "qualifier for resource '{resource}' was provided."
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

        self.qualifier: Union[BQB, BQM] = qualifier
        self.collection: Optional[str] = None
        self.term: Optional[str] = None

        # handle urls
        if resource.startswith("http"):
            match = IDENTIFIERS_ORG_PATTERN.match(resource)
            if match:
                # handle identifiers.org pattern
                self.collection, self.term = match.group(1), match.group(2)
            else:
                # other urls are directly stored as resources without collection
                self.collection = None
                self.term = resource
                logger.warning(
                    "%s does not conform to " "http(s)://identifiers.org/collection/id",
                    resource,
                )
        else:
            # get term and collection
            tokens = resource.split("/")
            if len(tokens) < 2:
                logger.error(
                    "Resource `{}` could not be split in collection and term. "
                    "A given resource must be of the form "
                    "`collection/term` or an url starting with "
                    "`http(s)://`)".format(resource)
                )
                self.collection = None
                self.term = resource
            else:
                self.collection = tokens[0]
                self.term = "/".join(tokens[1:])

        self.validate()

    @staticmethod
    def from_tuple(t: Tuple[Union[BQB, BQM], str]) -> "Annotation":
        """Construct from tuple."""
        qualifier, resource = t[0], t[1]
        return Annotation(qualifier=qualifier, resource=resource)

    @property
    def resource(self) -> Optional[str]:
        """Resource for annotations."""
        if self.collection:
            return f"{IDENTIFIERS_ORG_PREFIX}/{self.collection}/{self.term}"
        else:
            return self.term

    def to_dict(self) -> Dict[str, Optional[str]]:
        """Convert to dictionary."""
        return {
            "qualifier": self.qualifier.value,
            "collection": self.collection,
            "term": self.term,
            "resource": self.resource,
        }

    @staticmethod
    def check_term(collection: str, term: str) -> bool:
        """Check that term follows id pattern for collection.

        Uses the Identifiers collection information.
        """
        entry: Optional[str] = MIRIAM_COLLECTION.get(collection, None)
        if entry is None:
            logging.error(
                f"The given MIRIAM collection '{collection}' in annotation"
                f"`{collection}/{term}` does not exist."
            )
            return False

        pattern: str = entry["pattern"]  # type: ignore
        p = re.compile(pattern)
        m = p.match(term)
        if not m:
            logging.error(
                f"Term '{term}' did not match pattern "
                f"'{pattern} for collection `{collection}`."
            )
            return False

        return True

    @staticmethod
    def check_qualifier(qualifier: Union[BQB, BQM]) -> None:
        """Check that the qualifier is an allowed qualifier.

        :param qualifier:
        :return:
        """
        if not isinstance(qualifier, (BQB, BQM)):
            supported_qualifiers = [e.value for e in BQB] + [e.value for e in BQM]

            raise ValueError(
                f"qualifier '{qualifier}' is not in supported qualifiers: "
                f"{supported_qualifiers}"
            )

    def validate(self) -> None:
        """Validate annotation."""
        self.check_qualifier(self.qualifier)
        if self.collection:
            self.check_term(collection=self.collection, term=self.term)  # type: ignore
