"""Module for crossreferences (xref)."""
import logging
import re
from dataclasses import dataclass, field
from typing import Dict
from urllib.parse import urlparse


logger = logging.getLogger(__name__)

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
    """Check if string is valid url."""
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
    """Handling database cross references."""

    name: str
    accession: str
    url: str

    def __post_init__(self):
        """Validate."""
        self.validate()

    def to_dict(self) -> Dict:
        """Convert to dict."""
        return self.__dict__

    def validate(self, warnings=True) -> bool:
        """Validate the cross reference.

        :return:
        """
        if not is_url(self.url):
            if warnings:
                logger.warning(
                    f"{self.__class__.__name__} <{self.name}|{self.accession}> has invalid url: '{self.url}'"
                )
            return False
        return True
