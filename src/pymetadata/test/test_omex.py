from pathlib import Path

import pytest
from pymetadata.omex import ManifestEntry, Manifest
from pymetadata import RESOURCES_DIR


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



