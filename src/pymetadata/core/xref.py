"""Cross references to database entries.

A cross reference points at one database entry for a term, e.g., the ChEBI web
page for `CHEBI:33699`. `RDFAnnotationData` creates one cross reference per
provider registered for a collection in the identifiers.org registry.
"""

import re
from dataclasses import dataclass
from typing import Dict
from urllib.parse import urlparse

from pymetadata import log


logger = log.get_logger(__name__)

url_regex = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def is_url(url: str) -> bool:
    """Check if a string is a valid http(s) or ftp url.

    Args:
        url: string to check

    Returns:
        True if the string is a valid url.
    """
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            return False
        if re.match(url_regex, url) is None:
            return False
    except ValueError:
        return False

    return True


@dataclass()
class CrossReference:
    """A database cross reference.

    Attributes:
        name: name of the resource, e.g., `ChEBI`
        accession: term in the resource, e.g., `CHEBI:33699`
        url: url of the entry in the resource
    """

    name: str
    accession: str
    url: str

    def __post_init__(self) -> None:
        """Validate the cross reference after construction."""
        self.validate()

    def to_dict(self) -> Dict:
        """Convert the cross reference to a dictionary."""
        return self.__dict__

    def validate(self, warnings: bool = True) -> bool:
        """Check that the cross reference has a valid url.

        Args:
            warnings: log a warning for an invalid url

        Returns:
            True if the url is valid.
        """
        if not is_url(self.url):
            if warnings:
                logger.warning(
                    f"{self.__class__.__name__} <{self.name}|{self.accession}> "
                    f"has invalid url: '{self.url}'"
                )
            return False
        return True
