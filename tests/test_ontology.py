"""Test ontology."""

import json
import pickle

import pytest

from pymetadata.ontologies import (
    KISAO,
    PBPKO,
    SBO,
    OntologyTerm,
    PBPKOType,
    SBOType,
    _ontology_builder,
)


@pytest.mark.parametrize(
    "ontology_id",
    [
        "SBO",
        "KISAO",
        "PBPKO",
    ],
)
def test_import_ontology(ontology_id: str) -> None:
    """Test import of ontology enum."""
    _ontology_builder.try_ontology_import(ontology_id)


@pytest.mark.parametrize(
    "sbo, name",
    [
        (SBO.PHENOTYPE, "phenotype"),
        (SBO.SIMPLE_CHEMICAL, "simple chemical"),
    ],
)
def test_sbo_name(sbo: SBO, name: str) -> None:
    """Test import of ontology enum."""
    assert SBO.get_name(sbo) == name


@pytest.mark.parametrize(
    "sbo, term",
    [
        (SBO.PHENOTYPE, SBO.PHENOTYPE),
        ("SBO_0000358", SBO.PHENOTYPE),
        ("SBO:0000358", SBO.PHENOTYPE),
        (SBO.SIMPLE_CHEMICAL, SBO.SIMPLE_CHEMICAL),
        ("SBO_0000247", SBO.SIMPLE_CHEMICAL),
        ("SBO:0000247", SBO.SIMPLE_CHEMICAL),
    ],
)
def test_sbo_validate(sbo: SBOType, term: SBO) -> None:
    """Test import of ontology enum."""
    assert SBO.validate(sbo) == term


@pytest.mark.parametrize(
    "pbpko, name",
    [
        (
            PBPKO.PHYSIOLOGICALLY_BASED_PHARMACOKINETIC_MODEL,
            "physiologically based pharmacokinetic model",
        ),
        (PBPKO.BODYWEIGHT, "bodyweight"),
    ],
)
def test_pbpko_name(pbpko: PBPKO, name: str) -> None:
    """Test names of the PBPKO enum."""
    assert PBPKO.get_name(pbpko) == name


@pytest.mark.parametrize(
    "pbpko, term",
    [
        (PBPKO.BODYWEIGHT, PBPKO.BODYWEIGHT),
        ("PBPKO_00008", PBPKO.BODYWEIGHT),
        ("PBPKO:00008", PBPKO.BODYWEIGHT),
    ],
)
def test_pbpko_validate(pbpko: PBPKOType, term: PBPKO) -> None:
    """Test validation of PBPKO terms."""
    assert PBPKO.validate(pbpko) == term


def test_term_information() -> None:
    """Test that a term carries the information of the ontology."""
    term = SBO.SIMPLE_CHEMICAL

    assert term.label == "simple chemical"
    assert term.definition is not None
    assert term.curie == "SBO:0000247"
    assert term.url == "https://identifiers.org/SBO:0000247"
    assert term.deprecated is False


def test_term_synonyms() -> None:
    """Test that the synonyms of a term are available."""
    term = KISAO.CVODE

    assert "VODE" in term.synonyms
    assert term.label not in term.synonyms


def test_get_term() -> None:
    """Test the complete term record, also for a term given as a string."""
    term = PBPKO.get_term("PBPKO:00008")

    assert isinstance(term, OntologyTerm)
    assert isinstance(term, PBPKO)
    assert term.id == "PBPKO_00008"
    assert term.label == "bodyweight"
    assert term.definition is not None
    assert term.curie == "PBPKO:00008"


def test_term_repr() -> None:
    """Test that the representation shows id and label."""
    assert repr(SBO.SIMPLE_CHEMICAL) == "<SBO.SBO_0000247: 'simple chemical'>"


def test_term_is_str() -> None:
    """Test that a term still behaves like its id."""
    assert SBO.SIMPLE_CHEMICAL == "SBO_0000247"
    assert json.dumps({"sbo": SBO.SIMPLE_CHEMICAL}) == '{"sbo": "SBO_0000247"}'


def test_term_lookup() -> None:
    """Test that an ontology can be looked up like the enum it replaces."""
    assert SBO["SBO_0000247"] is SBO.SIMPLE_CHEMICAL
    assert SBO["SBO:0000247"] is SBO.SIMPLE_CHEMICAL
    assert SBO("SBO:0000247") is SBO.SIMPLE_CHEMICAL
    assert "SBO_0000247" in SBO
    assert "SBO_9999999" not in SBO


def test_term_iteration() -> None:
    """Test that the terms of an ontology can be iterated and counted."""
    terms = list(KISAO)

    assert len(terms) == len(KISAO)
    assert KISAO.CVODE in terms


def test_term_identity() -> None:
    """Test that the id and the name give the same term."""
    assert SBO.SIMPLE_CHEMICAL is SBO.SBO_0000247
    assert isinstance(SBO.SIMPLE_CHEMICAL, SBO)
    assert isinstance(SBO.SIMPLE_CHEMICAL, str)


def test_term_pickle() -> None:
    """Test that a term survives a roundtrip through pickle."""
    assert pickle.loads(pickle.dumps(SBO.SIMPLE_CHEMICAL)) is SBO.SIMPLE_CHEMICAL


def test_term_unknown() -> None:
    """Test the errors for terms which do not exist."""
    with pytest.raises(AttributeError):
        SBO.validate("SBO_9999999")

    with pytest.raises(ValueError, match="not a SBO id"):
        SBO.validate("KISAO_0000019")
