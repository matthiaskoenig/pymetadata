"""Testing the cache and the fallback to outdated content."""

import json
import logging
import os
import time
from pathlib import Path

import pytest

from pymetadata.cache import (
    CACHE_DURATION_ONTOLOGY,
    CACHE_DURATION_REGISTRY,
    cache_age,
    read_json_cache,
    read_json_cache_fallback,
    write_json_cache,
)


def age_cache(cache_path: Path, hours: float) -> None:
    """Backdate a cache file by the given number of hours."""
    old = time.time() - hours * 3600
    os.utime(cache_path, (old, old))


def test_ontology_is_cached_much_longer_than_the_registry() -> None:
    """Test the cache durations, the ontologies change with a release."""
    assert CACHE_DURATION_REGISTRY == 24
    assert CACHE_DURATION_ONTOLOGY == 30 * 24
    assert CACHE_DURATION_ONTOLOGY > CACHE_DURATION_REGISTRY


def test_cache_age_of_missing_file(tmp_path: Path) -> None:
    """Test that a missing cache file has no age."""
    assert cache_age(tmp_path / "missing.json") is None


def test_cache_age(tmp_path: Path) -> None:
    """Test that the age of a cache file is measured in hours."""
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"a": 1}, cache_path=cache_path)
    assert cache_age(cache_path) == pytest.approx(0, abs=0.01)

    age_cache(cache_path, hours=48)
    assert cache_age(cache_path) == pytest.approx(48, abs=0.01)


def test_read_json_cache_missing(tmp_path: Path) -> None:
    """Test that reading a missing cache file raises."""
    with pytest.raises(OSError, match="does not exist"):
        read_json_cache(tmp_path / "missing.json")


def test_read_json_cache_within_max_age(tmp_path: Path) -> None:
    """Test that content younger than the maximum age is returned."""
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"a": 1}, cache_path=cache_path)

    age_cache(cache_path, hours=10)
    assert read_json_cache(cache_path, max_age=24) == {"a": 1}


def test_read_json_cache_outdated(tmp_path: Path) -> None:
    """Test that content older than the maximum age is treated as missing."""
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"a": 1}, cache_path=cache_path)

    age_cache(cache_path, hours=25)
    with pytest.raises(OSError, match="older than"):
        read_json_cache(cache_path, max_age=24)

    # without a maximum age the content is returned however old it is
    assert read_json_cache(cache_path) == {"a": 1}


def test_read_json_cache_fallback_warns(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that outdated content is returned with a warning."""
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"a": 1}, cache_path=cache_path)
    age_cache(cache_path, hours=2000)

    with caplog.at_level(logging.WARNING):
        data = read_json_cache_fallback(cache_path, reason="service is not reachable")

    assert data == {"a": 1}
    assert "could not be refreshed" in caplog.text
    assert "service is not reachable" in caplog.text


def test_read_json_cache_fallback_without_cache(tmp_path: Path) -> None:
    """Test that the fallback is None if nothing is cached."""
    assert read_json_cache_fallback(tmp_path / "missing.json", reason="offline") is None


def test_read_json_cache_fallback_of_broken_cache(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that a corrupted cache file does not raise in the fallback."""
    cache_path = tmp_path / "data.json"
    cache_path.write_text("{not json")

    with caplog.at_level(logging.WARNING):
        assert read_json_cache_fallback(cache_path, reason="offline") is None

    assert "could not be read" in caplog.text


def test_write_json_cache_creates_parents(tmp_path: Path) -> None:
    """Test that the directories of a cache file are created."""
    cache_path = tmp_path / "a" / "b" / "data.json"
    write_json_cache(data={"a": 1}, cache_path=cache_path)

    assert json.loads(cache_path.read_text()) == {"a": 1}
