from pathlib import Path

import pytest
from pymetadata.omex import ManifestEntry, Manifest, Omex
from pymetadata import RESOURCES_DIR


SHOWCASE_OMEX = RESOURCES_DIR / "testdata" / "omex" / "CombineArchiveShowCase.omex"
COMPMODELS_OMEX = RESOURCES_DIR / "testdata" / "omex" / "CompModels.omex"


def test_entry_from_dict():
    entry_data = {
        'location': "./model/model1.xml",
        'format': "sbml",
        'master': "false",
    }
    entry = ManifestEntry(**entry_data)
    assert entry
    assert entry.location == "./model/model1.xml"
    assert entry.master is False


def test_manifest_from_dict():
    manifest_data = {
        'entries': [
            {
                'location': "./model/model1.xml",
                'format': "sbml",
                'master': "true",
            },
            {
                'location': ".",
                'format': "omex",
            },
        ]
    }
    manifest = Manifest(**manifest_data)
    assert manifest


def test_manifest_from_file():
    """Test that manifest can be created from file."""
    manifest_path = RESOURCES_DIR / "testdata" / "omex" / "CompModels_manifest.xml"
    manifest = Manifest.from_manifest(manifest_path)
    assert manifest
    assert len(manifest) == 6


@pytest.mark.parametrize("manifest_path", [
    RESOURCES_DIR / "testdata" / "omex" / "CompModels_manifest.xml",
    RESOURCES_DIR / "testdata" / "omex" / "CombineArchiveShowcase_manifest.xml",
])
def test_manifest_to_file(manifest_path, tmp_path: Path) -> None:
    """Test that manifest can be writen to manifest.xml."""
    manifest = Manifest.from_manifest(manifest_path)

    manifest2_path = tmp_path / "manifest.xml"
    manifest.to_manifest(manifest2_path)
    manifest2 = Manifest.from_manifest(manifest2_path)
    assert manifest2
    assert len(manifest) == len(manifest2)


def test_adding_removing_entry_manifest() -> None:
    """Testing adding and removing entries from manifest."""
    manifest = Manifest()
    assert "." in manifest
    assert "./manifest.xml" in manifest
    assert manifest
    assert len(manifest) == 2
    manifest.add_entry(
        ManifestEntry(location="./models/model.xml", format="sbml", master=False)
    )
    assert "./models/model.xml" in manifest
    assert len(manifest) == 3

    entry = manifest.remove_entry_for_location(location="./models/model.xml")
    assert entry
    assert entry.location == "./models/model.xml"
    assert len(manifest) == 2


@pytest.mark.parametrize("omex_path", [
    COMPMODELS_OMEX,
    SHOWCASE_OMEX,
])
def test_read_omex(omex_path: Path) -> None:
    """Test reading of omex files."""
    omex = Omex.from_omex(omex_path)
    assert omex
    assert omex.manifest


def test_remove_entry_omex() -> None:
    omex = Omex.from_omex(COMPMODELS_OMEX)
    omex_len = len(omex.manifest)
    omex.remove_entry_for_location("./README.md")
    assert len(omex.manifest) == omex_len - 1
