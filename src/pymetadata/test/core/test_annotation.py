from typing import Union

import pytest
from pymetadata.core.annotation import RDFAnnotation
from pymetadata.identifiers.miriam import BQB, BQM

rdf_annotation_data = [
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
def test_rdf_annotation(qualifier: Union[BQB, BQM], resource: str, expected: str) -> None:
    """Test various RDF annotation patterns"""
    a = RDFAnnotation(qualifier=qualifier, resource=resource)
    assert a
    assert str(a) == expected


def test_check_term_pass():
    assert RDFAnnotation.check_term("chebi", "CHEBI:000012") is True


@pytest.mark.xfail(raises=ValueError)
def test_check_collection_fail():
    assert RDFAnnotation.check_term("234234sdf", "CHEBI:000012") is True


@pytest.mark.xfail(raises=ValueError)
def test_check_term_fail():
    assert RDFAnnotation.check_term("chebi", "CHEB:000012") is False
