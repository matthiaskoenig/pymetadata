"""Ontology terms with the information of the ontology release.

An ontology is a class with one attribute per term, e.g., `SBO`, and a term is
an `OntologyTerm`, i.e., a `str` which is the identifier of the term and carries
what the ontology says about it:

```python
from pymetadata.ontologies import SBO

term = SBO.SIMPLE_CHEMICAL

term == "SBO_0000247"  # True, a term is the identifier
term.label             # 'simple chemical'
term.definition        # 'Simple, non-repetitive chemical entity.'
term.synonyms          # ()
term.curie             # 'SBO:0000247'
term.url               # 'https://identifiers.org/SBO:0000247'
```

Every term exists under its identifier (`SBO.SBO_0000247`) and under its name
(`SBO.SIMPLE_CHEMICAL`), both are the same object. The generated modules declare
the terms with their definition as docstring, so that an editor shows it when
the term is completed, and register the data with `_register`.

The ontology classes behave like the enums they replace: they are iterable, a
term can be looked up with `SBO["SBO_0000247"]` or `SBO("SBO:0000247")`, and
`validate` normalizes the notations of an identifier.
"""

from collections.abc import Iterator
from typing import Any, ClassVar

#: information of one term as it is registered by a generated module, i.e.
#: `(id, names, label, definition, synonyms, deprecated)`
TermData = tuple[str, tuple[str, ...], str, str | None, tuple[str, ...], bool]


def _lookup(
    ontology_id: str, terms: "dict[str, OntologyTerm]", term: "str | OntologyTerm"
) -> "OntologyTerm":
    """Resolve a term of an ontology.

    Args:
        ontology_id: name of the ontology, e.g., `SBO`
        terms: the terms of the ontology, keyed by identifier
        term: term or identifier, e.g., `SBO_0000247` or `SBO:0000247`

    Returns:
        The term of the ontology.

    Raises:
        ValueError: if the term does not belong to the ontology
        AttributeError: if the term does not exist in the ontology
    """
    if not isinstance(term, str):
        raise ValueError(f"Term is not a str or {ontology_id}: {term}")

    term_id = str(term).replace(":", "_", 1)
    if not term_id.startswith(ontology_id):
        raise ValueError(f"{term} is not a {ontology_id} id.")

    found = terms.get(term_id)
    if found is None:
        raise AttributeError(f"{ontology_id} has no term '{term}'.")
    return found


class OntologyMeta(type):
    """Metaclass which gives an ontology the lookups of an enum.

    The ontology is iterable, contains its terms and resolves an identifier with
    `SBO["SBO_0000247"]` and `SBO("SBO:0000247")`.
    """

    #: the terms of the ontology, keyed by identifier; set by `_register`
    _terms: "dict[str, OntologyTerm]"

    def __iter__(cls) -> Iterator["OntologyTerm"]:
        """Iterate over the terms of the ontology.

        Returns:
            The terms, in the order of the ontology.
        """
        return iter(cls._terms.values())

    def __len__(cls) -> int:
        """Count the terms of the ontology.

        Returns:
            The number of terms.
        """
        return len(cls._terms)

    def __contains__(cls, term: object) -> bool:
        """Check whether an identifier belongs to the ontology.

        Args:
            term: term or identifier, e.g., `SBO_0000247` or `SBO:0000247`

        Returns:
            True if the ontology has the term.
        """
        if not isinstance(term, str):
            return False
        return str(term).replace(":", "_", 1) in cls._terms

    def __getitem__(cls, term: str) -> "OntologyTerm":
        """Get a term by its identifier.

        Args:
            term: identifier, e.g., `SBO_0000247` or `SBO:0000247`

        Returns:
            The term of the ontology.

        Raises:
            KeyError: if the ontology has no such term
        """
        return cls._terms[term.replace(":", "_", 1)]

    def __call__(cls, term: "str | OntologyTerm") -> "OntologyTerm":
        """Resolve a term, i.e., `SBO("SBO:0000247")`.

        Args:
            term: term or identifier

        Returns:
            The term of the ontology.

        Raises:
            ValueError: if the term does not belong to the ontology
            AttributeError: if the term does not exist in the ontology
        """
        return _lookup(cls.__name__, cls._terms, term)


class OntologyTerm(str, metaclass=OntologyMeta):
    """A term of an ontology.

    The term is the identifier of the ontology term, i.e., it can be used
    wherever the identifier is expected: `SBO.SIMPLE_CHEMICAL == "SBO_0000247"`
    is True and serializing a term gives the identifier. The information of the
    ontology release is available as attributes.

    Attributes:
        label: name of the term in the ontology, e.g., `simple chemical`
        definition: definition of the term, `None` if the ontology has none
        synonyms: alternative names of the term
        deprecated: the term is obsolete and should not be used for annotation
    """

    #: the terms of the ontology, keyed by identifier; set by `_register`
    _terms: ClassVar[dict[str, "OntologyTerm"]] = {}

    label: str
    definition: str | None
    synonyms: tuple[str, ...]
    deprecated: bool

    @classmethod
    def _register(cls, terms: list[TermData]) -> None:
        """Create the terms of an ontology and set them on the class.

        This is called by the generated modules, which declare the terms in the
        class body and provide their information here.

        Args:
            terms: information of every term of the ontology
        """
        cls._terms = {}
        for term_id, names, label, definition, synonyms, deprecated in terms:
            term = str.__new__(cls, term_id)
            term.label = label
            term.definition = definition
            term.synonyms = synonyms
            term.deprecated = deprecated

            cls._terms[term_id] = term
            for name in names:
                setattr(cls, name, term)

    @property
    def id(self) -> str:
        """Identifier of the term.

        Returns:
            The identifier with an underscore, e.g., `SBO_0000247`.
        """
        return str(self)

    @property
    def name(self) -> str:
        """Identifier of the term, the name in the ontology is `label`.

        Returns:
            The identifier with an underscore, e.g., `SBO_0000247`.
        """
        return str(self)

    @property
    def value(self) -> str:
        """Identifier of the term.

        Returns:
            The identifier with an underscore, e.g., `SBO_0000247`.
        """
        return str(self)

    @property
    def curie(self) -> str:
        """Compact identifier of the term.

        Returns:
            The identifier with a colon, e.g., `SBO:0000247`.
        """
        return str(self).replace("_", ":", 1)

    @property
    def url(self) -> str:
        """Identifiers.org URL of the term.

        Returns:
            The resolvable url, e.g., `https://identifiers.org/SBO:0000247`.
        """
        return f"https://identifiers.org/{self.curie}"

    def __repr__(self) -> str:
        """Represent the term with its ontology, identifier and label.

        Returns:
            The representation, e.g., `<SBO.SBO_0000247: 'simple chemical'>`.
        """
        return f"<{type(self).__name__}.{self!s}: '{self.label}'>"

    def __reduce__(self) -> tuple[Any, ...]:
        """Pickle the term as the lookup of its identifier.

        Returns:
            The callable and the arguments which restore the term.
        """
        return (type(self).validate, (str(self),))

    @classmethod
    def get_name(cls, term: "str | OntologyTerm") -> str | None:
        """Get the name of a term.

        Args:
            term: term or identifier, e.g., `SBO_0000247` or `SBO:0000247`

        Returns:
            The name, or None if the term does not exist in the ontology.
        """
        found = cls._terms.get(str(term).replace(":", "_", 1))
        return found.label if found else None

    @classmethod
    def get_term(cls, term: "str | OntologyTerm") -> "OntologyTerm":
        """Get a term of the ontology.

        Args:
            term: term or identifier, e.g., `SBO_0000247` or `SBO:0000247`

        Returns:
            The term with label, definition, synonyms and deprecation.

        Raises:
            ValueError: if the term does not belong to the ontology
            AttributeError: if the term does not exist in the ontology
        """
        return cls.validate(term)

    @classmethod
    def validate(cls, term: "str | OntologyTerm") -> "OntologyTerm":
        """Validate and normalize a term of the ontology.

        Accepts a term, `SBO_0000247` and `SBO:0000247`.

        Args:
            term: term or identifier of a term

        Returns:
            The term of the ontology.

        Raises:
            ValueError: if the term does not belong to the ontology
            AttributeError: if the term does not exist in the ontology
        """
        return _lookup(cls.__name__, cls._terms, term)
