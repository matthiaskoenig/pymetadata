from pymetadata.pkdb_data.registry import Registry


def test_registry():
    registry = Registry(cache=False)
    assert registry
    registry = Registry(cache=True)
    assert registry
