"""Synonym information."""
from dataclasses import dataclass, field


@dataclass
class Synonym:
    """Synonyms."""

    name: str
    type: str
    source: str
