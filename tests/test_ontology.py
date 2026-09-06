"""Test ontology."""

import pytest

from pymetadata.metadata import PBPKO, SBO, PBPKOType, SBOType
from pymetadata.ontologies import ontology


@pytest.mark.parametrize(
    "ontology_id",
    [
        "SBO",
        "KISAO",
        "ECO",
        "PBPKO",
    ],
)
def test_import_ontology(ontology_id: str) -> None:
    """Test import of ontology enum."""
    ontology.try_ontology_import(ontology_id)


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
