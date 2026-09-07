"""Testing unichem."""

from pathlib import Path
from typing import Any

import requests

from pymetadata.webservices.unichem import UnichemQuery, UnichemSource


def test_get_sources(tmp_path: Path) -> None:
    """Test retrieving sources."""
    cache_path: Path = tmp_path
    sources = UnichemQuery(cache=True, cache_path=cache_path).get_sources()
    assert sources
    assert (cache_path / "unichem_sources.json").exists()

    sources = UnichemQuery(cache=True, cache_path=cache_path).get_sources()
    assert sources


def test_get_source_exists() -> None:
    """Test existing source."""
    query = UnichemQuery(cache=False)
    source: UnichemSource | None = query.sources.get(1, None)
    assert source
    assert isinstance(source, UnichemSource)


def test_get_source_missing() -> None:
    """Test missing source."""
    query = UnichemQuery(cache=False)
    source: UnichemSource | None = query.sources.get(-1, None)
    assert source is None


def test_query_xref_for_inchikey_no_cache(tmp_path: Path) -> None:
    """Test retrieving xrefs without cache."""
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    xrefs = UnichemQuery(cache=False, cache_path=tmp_path).query_xrefs_for_inchikey(
        inchikey=inchikey
    )
    assert xrefs


def test_query_xref_for_inchikey_cache(tmp_path: Path) -> None:
    """Test retrieving xrefs with cache."""
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    xrefs1 = UnichemQuery(cache=False, cache_path=tmp_path).query_xrefs_for_inchikey(
        inchikey=inchikey
    )
    xrefs2 = UnichemQuery(
        cache=True,
        cache_path=tmp_path,
    ).query_xrefs_for_inchikey(inchikey=inchikey)
    assert xrefs1
    assert xrefs2
    assert len(xrefs1) == len(xrefs2)


def test_query_xrefs_server_error(tmp_path: Path, monkeypatch: Any) -> None:
    """Test that a server error does not surface as a JSONDecodeError.

    The UniChem service intermittently answers with a HTML error page, see #73.
    """
    html_error = "<!doctype html><html lang='en'>500 Internal Server Error</html>"

    class FakeResponse:
        status_code = 500
        text = html_error
        content = html_error.encode()

        def json(self) -> Any:
            raise requests.exceptions.JSONDecodeError("Expecting value", html_error, 0)

    # the queries go through `get_json`, which uses the session of `webservice`
    monkeypatch.setattr(
        "pymetadata.webservices.webservice.get_session",
        lambda: type("S", (), {"get": lambda self, url, **kw: FakeResponse()})(),
    )

    xrefs = UnichemQuery(cache=False, cache_path=tmp_path).query_xrefs_for_inchikey(
        inchikey="NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    )
    assert xrefs == []
