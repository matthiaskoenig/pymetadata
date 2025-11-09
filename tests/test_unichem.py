"""Testing unichem."""

from pathlib import Path
from typing import Optional

from pymetadata.unichem import UnichemQuery, UnichemSource


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
    source: Optional[UnichemSource] = query.sources.get(1, None)
    assert source
    assert isinstance(source, UnichemSource)


def test_get_source_missing() -> None:
    """Test missing source."""
    query = UnichemQuery(cache=False)
    source: Optional[UnichemSource] = query.sources.get(-1, None)
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
