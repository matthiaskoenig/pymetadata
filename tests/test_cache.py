"""Testing the cache and the fallback to outdated content."""

import json
import logging
import os
import stat
import sys
import time
from pathlib import Path
from typing import Any

import pytest

from pymetadata import cache
from pymetadata._files import regular_file_mode
from pymetadata.cache import (
    CACHE_DURATION_ONTOLOGY,
    CACHE_DURATION_REGISTRY,
    CACHE_IN_USE_ATTEMPTS,
    cache_age,
    cache_file,
    read_bytes_cache,
    read_json_cache,
    read_json_cache_fallback,
    write_bytes_cache,
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


def test_write_json_cache_overlapping_access(tmp_path: Path) -> None:
    """Readers and overlapping writers never see partially written JSON."""
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"old": True}, cache_path=cache_path)

    class OverlappingEncoder(json.JSONEncoder):
        def default(self, o: Any) -> Any:
            """Read and replace the cache while the outer write is in progress."""
            assert read_json_cache(cache_path) == {"old": True}
            write_json_cache(data={"other": "writer"}, cache_path=cache_path)
            assert read_json_cache(cache_path) == {"other": "writer"}
            return "encoded"

    write_json_cache(
        data={"new": object()},
        cache_path=cache_path,
        json_encoder=OverlappingEncoder,
    )

    assert read_json_cache(cache_path) == {"new": "encoded"}
    assert list(tmp_path.iterdir()) == [cache_path]


def test_write_json_cache_failure_preserves_cache(tmp_path: Path) -> None:
    """A serialization failure preserves the old cache and removes temporary files."""
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"old": True}, cache_path=cache_path)

    with pytest.raises(TypeError, match="not JSON serializable"):
        write_json_cache(data={"new": object()}, cache_path=cache_path)

    assert read_json_cache(cache_path) == {"old": True}
    assert list(tmp_path.iterdir()) == [cache_path]


@pytest.fixture
def in_use(monkeypatch: pytest.MonkeyPatch) -> list[Path]:
    """Make a cache file fail to be replaced, as on Windows while another process reads it.

    Returns:
        The targets of the attempted replaces.
    """
    monkeypatch.setattr(cache, "CACHE_IN_USE_DELAY", 0)
    attempts: list[Path] = []

    def replace(self: Path, target: Path) -> Path:
        attempts.append(target)
        raise PermissionError(13, "Access is denied", str(target))

    monkeypatch.setattr(Path, "replace", replace)
    return attempts


def test_write_json_cache_retries_while_in_use(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    """A cache file which another process uses for a moment is replaced once it is free."""
    monkeypatch.setattr(cache, "CACHE_IN_USE_DELAY", 0)
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"old": True}, cache_path=cache_path)
    attempts: list[Path] = []
    replace = Path.replace

    def replace_when_free(self: Path, target: Path) -> Path:
        attempts.append(target)
        if len(attempts) < 3:
            raise PermissionError(13, "Access is denied", str(target))
        return replace(self, target)

    monkeypatch.setattr(Path, "replace", replace_when_free)
    with caplog.at_level(logging.WARNING):
        write_json_cache(data={"new": True}, cache_path=cache_path)

    assert attempts == [cache_path] * 3
    assert read_json_cache(cache_path) == {"new": True}
    assert list(tmp_path.iterdir()) == [cache_path]
    assert not caplog.text


def test_write_json_cache_in_use_keeps_the_cache(
    tmp_path: Path, in_use: list[Path], caplog: pytest.LogCaptureFixture
) -> None:
    """A cache file which stays in use is kept with a warning, the write does not fail."""
    cache_path = tmp_path / "data.json"
    cache_path.write_text(json.dumps({"old": True}))

    with caplog.at_level(logging.WARNING):
        write_json_cache(data={"new": True}, cache_path=cache_path)

    assert in_use == [cache_path] * CACHE_IN_USE_ATTEMPTS
    assert read_json_cache(cache_path) == {"old": True}
    assert list(tmp_path.iterdir()) == [cache_path]
    assert len(caplog.records) == 1
    assert "could not be written" in caplog.text


def test_write_json_cache_to_unwritable_directory(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """A cache file which cannot be written is a warning and not an error."""
    blocker = tmp_path / "blocker"
    blocker.write_text("a file where the cache directory should be")

    with caplog.at_level(logging.WARNING):
        write_json_cache(data={"a": 1}, cache_path=blocker / "data.json")

    assert list(tmp_path.iterdir()) == [blocker]
    assert len(caplog.records) == 1
    assert "could not be written" in caplog.text


@pytest.mark.skipif(sys.platform == "win32", reason="POSIX permissions")
def test_write_cache_has_regular_permissions(tmp_path: Path) -> None:
    """A cache file has the permissions of a regular new file, not of a temporary one."""
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"a": 1}, cache_path=cache_path)

    assert stat.S_IMODE(cache_path.stat().st_mode) == regular_file_mode()


def test_write_bytes_cache(tmp_path: Path) -> None:
    """Binary content, e.g., an svg image, is cached like JSON."""
    cache_path = tmp_path / "a" / "image.svg"
    write_bytes_cache(b"<svg/>", cache_path)

    assert read_bytes_cache(cache_path) == b"<svg/>"
    assert list(cache_path.parent.iterdir()) == [cache_path]


def test_read_json_cache_retries_while_replaced(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A cache file which another process replaces at the moment is read once it is there."""
    monkeypatch.setattr(cache, "CACHE_IN_USE_DELAY", 0)
    cache_path = tmp_path / "data.json"
    write_json_cache(data={"a": 1}, cache_path=cache_path)
    attempts: list[Path] = []
    read_bytes = Path.read_bytes

    def read_when_replaced(self: Path) -> bytes:
        attempts.append(self)
        if len(attempts) < 2:
            raise PermissionError(13, "Access is denied", str(self))
        return read_bytes(self)

    monkeypatch.setattr(Path, "read_bytes", read_when_replaced)

    assert read_json_cache(cache_path) == {"a": 1}
    assert attempts == [cache_path] * 2


def test_cache_file_quotes_the_key(tmp_path: Path) -> None:
    """Test that the key is quoted into a single file name."""
    assert cache_file(tmp_path, "CHEBI:2668") == tmp_path / "CHEBI%3A2668.json"


def test_cache_file_stays_inside_the_directory(tmp_path: Path) -> None:
    """Test that a key with path separators cannot leave the directory."""
    path = cache_file(tmp_path, "../../evil")

    assert path.parent == tmp_path
    assert path.name == "..%2F..%2Fevil.json"


def test_cache_file_hashes_long_keys(tmp_path: Path) -> None:
    """Test that a key too long for a file name is hashed."""
    path = cache_file(tmp_path, "x" * 1000)
    other = cache_file(tmp_path, "x" * 999 + "y")

    assert path.parent == tmp_path
    assert len(path.name.encode()) <= 255
    assert path.suffix == ".json"
    assert path == cache_file(tmp_path, "x" * 1000)
    assert path != other


def test_cache_file_rejects_empty_key(tmp_path: Path) -> None:
    """Test that an empty key does not name a cache file."""
    with pytest.raises(ValueError, match="empty"):
        cache_file(tmp_path, "")


def test_read_json_cache_of_corrupt_cache(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that a corrupt cache file is a cache miss and is removed."""
    cache_path = tmp_path / "data.json"
    cache_path.write_text("{not json")

    with caplog.at_level(logging.WARNING), pytest.raises(OSError, match="corrupt"):
        read_json_cache(cache_path)

    assert not cache_path.exists()
    assert "corrupt" in caplog.text
