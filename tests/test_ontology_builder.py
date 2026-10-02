"""Testing the download of the ontologies."""

import gzip
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest

from pymetadata.ontologies import _ontology_builder
from pymetadata.ontologies._ontology_builder import (
    ontology_files,
    update_ontology_file,
    update_ontology_files,
)


class FakeResponse:
    """Streamed response which can break off in the middle of the download."""

    def __init__(self, chunks: list[bytes], fail: bool) -> None:
        """Store the chunks and whether the download breaks off after them."""
        self.chunks = chunks
        self.fail = fail

    def __enter__(self) -> "FakeResponse":
        """Enter the context of the response."""
        return self

    def __exit__(self, *args: object) -> None:
        """Leave the context of the response."""

    def raise_for_status(self) -> None:
        """Accept the response."""

    def iter_content(self, chunk_size: int) -> Iterator[bytes]:
        """Yield the chunks, then break off if requested."""
        yield from self.chunks
        if self.fail:
            raise ConnectionError("connection reset")


class FakeSession:
    """Stand-in for the shared session of the web services."""

    def __init__(self, response: FakeResponse) -> None:
        """Store the response for every request."""
        self.response = response
        self.requests: list[tuple[str, dict[str, Any]]] = []

    def get(self, url: str, **kwargs: Any) -> FakeResponse:
        """Record the request and answer with the response."""
        self.requests.append((url, kwargs))
        return self.response


@pytest.fixture
def resources(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Store the downloaded ontologies in a temporary directory."""
    monkeypatch.setattr(_ontology_builder, "RESOURCES_DIR", tmp_path)
    (tmp_path / "ontologies").mkdir()
    return tmp_path


def test_update_ontology_file(resources: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that the download is streamed through the shared session."""
    session = FakeSession(FakeResponse([b"<owl>", b"</owl>"], fail=False))
    monkeypatch.setattr(_ontology_builder, "get_session", lambda: session)

    update_ontology_file(ontology_files["SBO"])

    gzip_path = resources / "ontologies" / "sbo.owl.gz"
    assert gzip.decompress(gzip_path.read_bytes()) == b"<owl></owl>"
    assert session.requests[0][1]["stream"] is True
    assert list((resources / "ontologies").iterdir()) == [gzip_path]


def test_interrupted_download_keeps_ontology(
    resources: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that a broken off download does not truncate the stored ontology."""
    gzip_path = resources / "ontologies" / "sbo.owl.gz"
    gzip_path.write_bytes(gzip.compress(b"<old/>"))
    session = FakeSession(FakeResponse([b"<new>"], fail=True))
    monkeypatch.setattr(_ontology_builder, "get_session", lambda: session)

    with pytest.raises(ConnectionError):
        update_ontology_file(ontology_files["SBO"])

    assert gzip.decompress(gzip_path.read_bytes()) == b"<old/>"
    assert list((resources / "ontologies").iterdir()) == [gzip_path]


def test_update_ontology_files_raises_failures(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test that a failed download is not silently discarded."""

    def fail(ofile: Any) -> None:
        raise RuntimeError(f"download failed: {ofile.id}")

    monkeypatch.setattr(_ontology_builder, "update_ontology_file", fail)

    with pytest.raises(RuntimeError, match="download failed: SBO"):
        update_ontology_files(["SBO"])
