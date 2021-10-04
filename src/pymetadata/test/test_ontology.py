import pytest

from pymetadata.metadata import SBO, SBOType
from pymetadata.ontologies import ontology


@pytest.mark.parametrize(
    "ontology_id",
    [
        "SBO",
        "KISAO",
        "ECO",
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
