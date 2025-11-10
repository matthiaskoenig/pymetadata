"""Test annotations."""

from typing import Union

import pytest

from pymetadata.core.annotation import RDFAnnotation
from pymetadata.identifiers.miriam import BQB, BQM


rdf_annotation_data = [
    (
        BQB.IS,
        "https://identifiers.org/DOI:10.1016/j.jtbi.2004.04.039",
        "RDFAnnotation(BQB.IS|doi|10.1016/j.jtbi.2004.04.039|identifiers.org)",
    ),
    (
        BQB.IS,
        "NCIT:C75913",
        "RDFAnnotation(BQB.IS|ncit|C75913|identifiers.org)",
    ),
    (
        BQB.IS,
        "ncit:C75913",
        "RDFAnnotation(BQB.IS|ncit|C75913|identifiers.org)",
    ),
    (
        BQB.IS,
        "ncit/C75913",
        "RDFAnnotation(BQB.IS|ncit|C75913|identifiers.org)",
    ),
    (
        BQB.IS,
        "taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606|identifiers.org)",
    ),
    (
        BQB.IS,
        "taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/biomodels.sbo/SBO:0000247",
        "RDFAnnotation(BQB.IS|sbo|SBO:0000247|identifiers.org)",
    ),
    (
        BQB.IS,
        "urn:miriam:obo.go:GO%3A0005623",
        "RDFAnnotation(BQB.IS|go|GO:0005623|identifiers.org)",
    ),
    (
        BQB.IS,
        "urn:miriam:chebi:CHEBI%3A33699",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:33699|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "bto/BTO:0000089",
        "RDFAnnotation(BQB.IS|bto|BTO:0000089|identifiers.org)",
    ),
    (
        BQB.IS,
        "BTO:0000089",
        "RDFAnnotation(BQB.IS|bto|BTO:0000089|identifiers.org)",
    ),
    (
        BQB.IS,
        "CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012|identifiers.org)",
    ),
    (
        BQB.IS,
        "chebi/CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://en.wikipedia.org/wiki/Cytosol",
        "RDFAnnotation(BQB.IS|None|https://en.wikipedia.org/wiki/Cytosol|none)",
    ),
    (
        BQB.IS_VERSION_OF,
        "urn:miriam:uniprot:P03023",
        "RDFAnnotation(BQB.IS_VERSION_OF|uniprot|P03023|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829|identifiers.org)",
    ),
    (
        BQB.IS,
        "CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012|identifiers.org)",
    ),
    (
        BQB.IS,
        "doi/10.3389/fphar.2025.1686415",
        "RDFAnnotation(BQB.IS|doi|10.3389/fphar.2025.1686415|identifiers.org)",
    ),
    (
        BQB.IS,
        "https://bioregistry.io/chebi:15996",
        "RDFAnnotation(BQB.IS|None|https://bioregistry.io/chebi:15996|bioregistry.io)",
    ),
    (
        BQB.IS,
        "hmdb/HMDB0000122",
        "RDFAnnotation(BQB.IS|hmdb|HMDB0000122|identifiers.org)",
    ),
    (
        BQB.IS,
        "hmdb:HMDB0000122",
        "RDFAnnotation(BQB.IS|hmdb|HMDB0000122|identifiers.org)",
    ),
]


@pytest.mark.parametrize("qualifier,resource,expected", rdf_annotation_data)
def test_rdf_annotation(
    qualifier: Union[BQB, BQM], resource: str, expected: str
) -> None:
    """Test various RDF annotation patterns."""
    a = RDFAnnotation(qualifier=qualifier, resource=resource)
    assert a
    assert str(a) == expected


def test_check_term_pass() -> None:
    """Test that check term passes."""
    rdf_annotation = RDFAnnotation(qualifier=BQB.IS, resource="CHEBI:000012")
    assert rdf_annotation.check_miriam_term()


def test_check_bioregistry() -> None:
    """Test that check collection fails."""
    rdf_annotation = RDFAnnotation(
        qualifier=BQB.IS, resource="https://bioregistry.io/CHEBI:000012"
    )
    assert not rdf_annotation.check_miriam_term()
