"""Ontology terms with the information of the ontology release.

The generated enums of `pymetadata.ontologies` are `OntologyEnum` subclasses:
the members are the terms of the ontology, and every member carries the
information the ontology provides for it.

```python
from pymetadata.ontologies import SBO

term = SBO.SIMPLE_CHEMICAL

term.value       # 'SBO_0000247', the enum is a `str` subclass
term.label       # 'simple chemical'
term.definition  # 'Simple, non-repetitive chemical entity.'
term.synonyms    # ()
term.curie       # 'SBO:0000247'
term.url         # 'https://identifiers.org/SBO:0000247'
term.term        # the complete `OntologyTerm`
```

The member name is the id of the term (`term.name` is `'SBO_0000247'`), the
readable name of the ontology is `label`. The information is stored per enum
class as plain tuples, which keeps the import of the large generated modules
cheap, and is turned into an `OntologyTerm` when it is accessed.
"""

from dataclasses import dataclass
from enum import Enum
from typing import ClassVar

#: information of one term as it is stored in a generated module, i.e.
#: `(label, definition, synonyms, deprecated)`
TermData = tuple[str, str | None, tuple[str, ...], bool]


@dataclass(frozen=True, slots=True)
class OntologyTerm:
    """A term of an ontology.

    Attributes:
        id: id of the term with an underscore, e.g., `SBO_0000247`
        label: name of the term in the ontology, e.g., `simple chemical`
        definition: definition of the term, `None` if the ontology has none
        synonyms: alternative names of the term
        deprecated: the term is obsolete and should not be used for annotation
    """

    id: str
    label: str
    definition: str | None = None
    synonyms: tuple[str, ...] = ()
    deprecated: bool = False

    @property
    def curie(self) -> str:
        """Compact identifier of the term.

        Returns:
            The id with a colon, e.g., `SBO:0000247`.
        """
        return self.id.replace("_", ":", 1)

    @property
    def url(self) -> str:
        """Identifiers.org URL of the term.

        Returns:
            The resolvable url, e.g., `https://identifiers.org/SBO:0000247`.
        """
        return f"https://identifiers.org/{self.curie}"


class OntologyEnum(str, Enum):
    """Base class of the generated ontology enums.

    The members are the terms of an ontology, with the id as value, so that a
    member can be used wherever the id is expected. Every term exists twice,
    under its id (`SBO.SBO_0000247`) and under its name (`SBO.SIMPLE_CHEMICAL`),
    the second being an alias of the first.

    The generated subclasses provide the members and assign `_terms`, the
    information of the ontology release for every term.
    """

    #: term information keyed by id, assigned by the generated modules
    _terms: ClassVar[dict[str, TermData]]

    @property
    def term(self) -> OntologyTerm:
        """Information the ontology provides for the term.

        Returns:
            The term with label, definition, synonyms and deprecation.
        """
        label, definition, synonyms, deprecated = type(self)._terms[self.value]
        return OntologyTerm(
            id=self.value,
            label=label,
            definition=definition,
            synonyms=synonyms,
            deprecated=deprecated,
        )

    @property
    def label(self) -> str:
        """Name of the term in the ontology.

        Returns:
            The label, e.g., `simple chemical`.
        """
        return type(self)._terms[self.value][0]

    @property
    def definition(self) -> str | None:
        """Definition of the term in the ontology.

        Returns:
            The definition, `None` if the ontology has none.
        """
        return type(self)._terms[self.value][1]

    @property
    def synonyms(self) -> tuple[str, ...]:
        """Alternative names of the term.

        Returns:
            The synonyms, empty if the ontology has none.
        """
        return type(self)._terms[self.value][2]

    @property
    def deprecated(self) -> bool:
        """Whether the term is obsolete.

        Returns:
            True for a term which should no longer be used for annotation.
        """
        return type(self)._terms[self.value][3]

    @property
    def curie(self) -> str:
        """Compact identifier of the term.

        Returns:
            The id with a colon, e.g., `SBO:0000247`.
        """
        return self.value.replace("_", ":", 1)

    @property
    def url(self) -> str:
        """Identifiers.org URL of the term.

        Returns:
            The resolvable url, e.g., `https://identifiers.org/SBO:0000247`.
        """
        return f"https://identifiers.org/{self.curie}"

    def __repr__(self) -> str:
        """Represent the term with its id and label.

        Returns:
            The representation, e.g., `<SBO.SBO_0000247: 'simple chemical'>`.
        """
        return f"<{type(self).__name__}.{self.value}: '{self.label}'>"

    @classmethod
    def get_name(cls, term: "OntologyEnum") -> str | None:
        """Get the name of a term.

        Args:
            term: member of the enum

        Returns:
            The name, or None if the term does not exist in the ontology.
        """
        data = cls._terms.get(term.value)
        return data[0] if data else None

    @classmethod
    def get_term(cls, term: "str | OntologyEnum") -> OntologyTerm:
        """Get the information of a term.

        Args:
            term: member of the enum, `SBO_0000247` or `SBO:0000247`

        Returns:
            The term with label, definition, synonyms and deprecation.

        Raises:
            ValueError: if the term does not belong to the ontology
            AttributeError: if the term does not exist in the ontology
        """
        return cls.validate(term).term

    @classmethod
    def validate(cls, term: "str | OntologyEnum") -> "OntologyEnum":
        """Validate and normalize a term of the ontology.

        Accepts an enum member, `SBO_0000247` and `SBO:0000247`.

        Args:
            term: member of the enum or the id of a term

        Returns:
            The corresponding enum member.

        Raises:
            ValueError: if the term does not belong to the ontology
            AttributeError: if the term does not exist in the ontology
        """
        if isinstance(term, cls):
            return term
        if isinstance(term, str):
            prefix = cls.__name__
            if not term.startswith(prefix):
                raise ValueError(f"{term} is not a {prefix} id.")
            member: OntologyEnum = getattr(cls, term.replace(":", "_", 1))
            return member

        raise ValueError(f"Term is neither a str nor a {cls.__name__}: {term}")
