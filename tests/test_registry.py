"""Test identifiers.org registry."""

from pymetadata.identifiers.registry import Registry


def test_registry() -> None:
    """Test registry."""
    registry = Registry(cache=False)
    assert registry
    registry = Registry(cache=True)
    assert registry
