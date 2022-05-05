"""Synonym information."""
from dataclasses import dataclass


@dataclass
class Synonym:
    """Synonyms."""

    name: str
    type: str
    source: str
