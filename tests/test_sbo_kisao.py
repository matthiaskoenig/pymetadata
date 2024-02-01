"""Test KISAO and SBO ontologies."""

import pytest

from pymetadata.metadata.kisao import KISAO
from pymetadata.metadata.sbo import SBO


@pytest.mark.parametrize(
    "term",
    [
        "SIMPLE_CHEMICAL",
        "BIOCHEMICAL_REACTION",
        "TRANSPORT_REACTION",
    ],
)
def test_sbo_term_exists(term: str) -> None:
    """Test that term exists in SBO."""
    assert getattr(SBO, term)


@pytest.mark.parametrize(
    "term",
    [
        "UPPER_BOUND",
        "LOWER_BOUND",
    ],
)
def test_kisao_term_exists(term: str) -> None:
    """Test that term exists in KISAO."""
    assert getattr(KISAO, term)
