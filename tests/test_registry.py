"""Test identifiers.org registry."""

import json
import logging
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import pytest

import pymetadata
from pymetadata import cache
from pymetadata.cache import read_json_cache
from pymetadata.webservices import registry as registry_module
from pymetadata.webservices.registry import Registry

#: the registry response of identifiers.org, reduced to three collections
RESPONSE_PATH = (
    Path(__file__).parent / "data" / "registry" / "identifiers_registry_response.json"
)

#: the collections of the reduced registry response
PREFIXES = ["chebi", "go", "taxonomy"]


def test_registry() -> None:
    """Test registry."""
    registry = Registry(cache=False)
    assert registry
    registry = Registry(cache=True)
    assert registry


@pytest.fixture
def downloads(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> list[str]:
    """Answer the registry downloads with the reduced response, cached in `tmp_path`.

    Returns:
        The urls of the downloads.
    """
    monkeypatch.setattr(pymetadata, "CACHE_PATH", tmp_path)
    response = json.loads(RESPONSE_PATH.read_text(encoding="utf-8"))
    urls: list[str] = []

    def get_json(url: str, **kwargs: Any) -> Any:
        urls.append(url)
        return response

    monkeypatch.setattr(registry_module, "get_json", get_json)
    return urls


def test_registry_is_downloaded_once_and_cached(
    tmp_path: Path, downloads: list[str]
) -> None:
    """The registry is downloaded into an empty cache and then read from it."""
    registry = Registry()

    assert sorted(registry.ns_dict) == PREFIXES
    assert downloads == [Registry.URL]
    assert Registry().ns_dict == registry.ns_dict
    assert downloads == [Registry.URL]
    assert list(tmp_path.iterdir()) == [tmp_path / "identifiers_registry.json"]


def test_registry_without_cache_write(
    tmp_path: Path,
    downloads: list[str],
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """A registry which cannot be cached is used as downloaded, and downloaded once."""
    monkeypatch.setattr(cache, "CACHE_IN_USE_DELAY", 0)

    def replace(self: Path, target: Path) -> Path:
        # Windows, while another process reads the cached registry
        raise PermissionError(13, "Access is denied", str(target))

    monkeypatch.setattr(Path, "replace", replace)

    with caplog.at_level(logging.WARNING):
        registry = Registry()

    assert sorted(registry.ns_dict) == PREFIXES
    assert downloads == [Registry.URL]
    assert list(tmp_path.iterdir()) == []
    assert "could not be written" in caplog.text


def test_corrupt_registry_cache_is_downloaded_again(
    tmp_path: Path, downloads: list[str]
) -> None:
    """A corrupt cached registry is replaced by a download instead of failing."""
    registry_path = tmp_path / "identifiers_registry.json"
    registry_path.write_text('{"chebi": {"prefix": "che')

    registry = Registry()

    assert sorted(registry.ns_dict) == PREFIXES
    assert downloads == [Registry.URL]
    assert sorted(read_json_cache(registry_path)) == PREFIXES


def test_downloaded_registry_equals_cached_registry(
    tmp_path: Path, downloads: list[str]
) -> None:
    """The downloaded namespaces are the ones the cached registry gives."""
    registry_path = tmp_path / "identifiers_registry.json"
    downloaded = Registry.update_registry(registry_path=registry_path)

    assert Registry.load_registry(registry_path) == downloaded
    assert len(downloads) == 1


#: a process which loads the registry as a pytest-xdist worker does with its
#: first annotation, on the same empty cache as the other processes and at the
#: same time. Arguments: cache directory, registry response, start file, and
#: whether a cache file in use cannot be replaced (Windows)
WORKER = """
import json
import os
import random
import sys
import time
from pathlib import Path

import pymetadata
from pymetadata import cache
from pymetadata.webservices import registry

cache_dir, response_path, start = (Path(arg) for arg in sys.argv[1:4])
in_use = sys.argv[4] == "1"

pymetadata.CACHE_PATH = cache_dir
cache.CACHE_IN_USE_DELAY = 0.001
response = json.loads(response_path.read_text(encoding="utf-8"))
downloads = 0


def get_json(url, **kwargs):
    global downloads
    downloads += 1
    # the downloads end at different times, as over the network
    time.sleep(random.uniform(0, 0.2))
    return response


registry.get_json = get_json

if in_use:
    # on Windows a file which another process has open cannot be replaced;
    # here the cached registry is always in use once it exists
    replace = os.replace

    def replace_unless_in_use(src, dst, **kwargs):
        if os.path.exists(dst):
            raise PermissionError(13, "Access is denied", str(dst))
        return replace(src, dst, **kwargs)

    os.replace = replace_unless_in_use

(start.parent / f"ready-{os.getpid()}").touch()
while not start.exists():
    time.sleep(0.001)

namespaces = registry.Registry().ns_dict

# read the cached registry while the other processes write it
end = time.monotonic() + 0.3
while time.monotonic() < end:
    data = cache.read_json_cache(cache_dir / "identifiers_registry.json")
    assert sorted(data) == sorted(namespaces)

print(json.dumps({"downloads": downloads, "namespaces": sorted(namespaces)}))
"""


@pytest.mark.parametrize("in_use", [False, True], ids=["platform", "in-use"])
def test_registry_loaded_by_concurrent_processes(tmp_path: Path, in_use: bool) -> None:
    """Several processes load the registry into the same empty cache at once (#102).

    Every process downloads the registry at most once and has it complete, no
    process fails, the cached registry is complete and no temporary file is
    left. `platform` runs with the file semantics of the platform, `in-use`
    with those of Windows while another process reads the cached registry.
    """
    n_processes = 6
    cache_dir = tmp_path / "cache"
    sync_dir = tmp_path / "sync"
    sync_dir.mkdir()
    start = sync_dir / "start"
    processes = [
        subprocess.Popen(
            [
                sys.executable,
                "-c",
                WORKER,
                str(cache_dir),
                str(RESPONSE_PATH),
                str(start),
                "1" if in_use else "0",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(n_processes)
    ]
    # start all processes at once, after their imports
    deadline = time.monotonic() + 120
    while len(list(sync_dir.glob("ready-*"))) < n_processes:
        if time.monotonic() > deadline or any(p.poll() is not None for p in processes):
            break
        time.sleep(0.01)
    start.touch()

    results = []
    for process in processes:
        stdout, stderr = process.communicate(timeout=120)
        assert process.returncode == 0, stderr
        results.append(json.loads(stdout.splitlines()[-1]))

    assert all(result["namespaces"] == PREFIXES for result in results)
    downloads = [result["downloads"] for result in results]
    assert all(n <= 1 for n in downloads), downloads
    assert sum(downloads) >= 1
    registry_path = cache_dir / "identifiers_registry.json"
    assert sorted(read_json_cache(registry_path)) == PREFIXES
    assert list(cache_dir.iterdir()) == [registry_path]
