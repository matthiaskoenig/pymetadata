from dataclasses import dataclass, field


@dataclass
class Synonym:
    """Handling synonyms"""

    name: str
    type: str
    source: str
