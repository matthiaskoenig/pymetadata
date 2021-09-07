from typing import Union

import pytest

from pymetadata.core.annotation import RDFAnnotation
from pymetadata.identifiers.miriam import BQB, BQM


rdf_annotation_data = [
    (
        BQB.IS,
        "ncit/C75913",
        "RDFAnnotation(BQB.IS|ncit|C75913)",
    ),
    (
        BQB.IS,
        "taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606)",
    ),
    (
        BQB.IS,
        "taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/taxonomy/9606",
        "RDFAnnotation(BQB.IS|taxonomy|9606)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/biomodels.sbo/SBO:0000247",
        "RDFAnnotation(BQB.IS|sbo|SBO:0000247)",
    ),
    (
        BQB.IS,
        "urn:miriam:obo.go:GO%3A0005623",
        "RDFAnnotation(BQB.IS|go|GO:0005623)",
    ),
    (
        BQB.IS,
        "urn:miriam:chebi:CHEBI%3A33699",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:33699)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
    (
        BQB.IS,
        "bto/BTO:0000089",
        "RDFAnnotation(BQB.IS|bto|BTO:0000089)",
    ),
    (
        BQB.IS,
        "BTO:0000089",
        "RDFAnnotation(BQB.IS|bto|BTO:0000089)",
    ),
    (
        BQB.IS,
        "CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012)",
    ),
    (
        BQB.IS,
        "chebi/CHEBI:000012",
        "RDFAnnotation(BQB.IS|chebi|CHEBI:000012)",
    ),
    (
        BQB.IS,
        "https://en.wikipedia.org/wiki/Cytosol",
        "RDFAnnotation(BQB.IS|None|https://en.wikipedia.org/wiki/Cytosol)",
    ),
    (
        BQB.IS_VERSION_OF,
        "urn:miriam:uniprot:P03023",
        "RDFAnnotation(BQB.IS_VERSION_OF|uniprot|P03023)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/go/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
    (
        BQB.IS,
        "https://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
    (
        BQB.IS,
        "http://identifiers.org/GO:0005829",
        "RDFAnnotation(BQB.IS|go|GO:0005829)",
    ),
]


@pytest.mark.parametrize("qualifier,resource,expected", rdf_annotation_data)
def test_rdf_annotation(
    qualifier: Union[BQB, BQM], resource: str, expected: str
) -> None:
    """Test various RDF annotation patterns"""
    a = RDFAnnotation(qualifier=qualifier, resource=resource)
    assert a
    assert str(a) == expected


def test_check_term_pass() -> None:
    assert RDFAnnotation.check_term("chebi", "CHEBI:000012") is True


@pytest.mark.xfail(raises=ValueError)
def test_check_collection_fail() -> None:
    assert RDFAnnotation.check_term("234234sdf", "CHEBI:000012") is True


@pytest.mark.xfail(raises=ValueError)
def test_check_term_fail() -> None:
    assert RDFAnnotation.check_term("chebi", "CHEB:000012") is False
