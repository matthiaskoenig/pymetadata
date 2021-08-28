import pytest

from pymetadata.pkdb_data.annotation import BQB, Annotation


def test_url_annotation():
    a = Annotation(BQB.IS, "https://mypage/myid")
    assert a


def test_chebi_annotation():
    a = Annotation(BQB.IS_VERSION_OF, "chebi/CHEBI:00012")
    assert a


def test_check_term_pass():
    assert Annotation.check_term("chebi", "CHEBI:000012") is True


@pytest.mark.xfail(raises=ValueError)
def test_check_collection_fail():
    assert Annotation.check_term("234234sdf", "CHEBI:000012") is True


@pytest.mark.xfail(raises=ValueError)
def test_check_term_fail():
    assert Annotation.check_term("chebi", "CHEB:000012") is False
