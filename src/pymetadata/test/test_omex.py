from pathlib import Path

import pytest

from pymetadata import RESOURCES_DIR
from pymetadata.omex import Manifest, ManifestEntry, Omex


SHOWCASE_OMEX = RESOURCES_DIR / "testdata" / "omex" / "CombineArchiveShowCase.omex"
COMPMODELS_OMEX = RESOURCES_DIR / "testdata" / "omex" / "CompModels.omex"
BIOMODELS_OMEX = RESOURCES_DIR / "testdata" / "omex" / "BIOMD0000000001.omex"

SHOWCASE_OMEX_MANIFEST = (
    RESOURCES_DIR / "testdata" / "omex" / "CombineArchiveShowCase_manifest.xml"
)
COMPMODELS_OMEX_MANIFEST = (
    RESOURCES_DIR / "testdata" / "omex" / "CompModels_manifest.xml"
)


def test_entry_from_dict() -> None:
    entry_data = {
        "location": "./model/model1.xml",
        "format": "sbml",
        "master": "false",
    }
    entry = ManifestEntry(**entry_data)
    assert entry
    assert entry.location == "./model/model1.xml"
    assert entry.master is False


def test_manifest_from_dict() -> None:
    manifest_data = {
        "entries": [
            {
                "location": "./model/model1.xml",
                "format": "sbml",
                "master": "true",
            },
            {
                "location": ".",
                "format": "omex",
            },
        ]
    }
    manifest = Manifest(**manifest_data)
    assert manifest


def test_manifest_from_file() -> None:
    """Test that manifest can be created from file."""
    manifest_path = RESOURCES_DIR / "testdata" / "omex" / "CompModels_manifest.xml"
    manifest = Manifest.from_manifest(manifest_path)
    assert manifest
    assert len(manifest) == 6


@pytest.mark.parametrize(
    "manifest_path",
    [
        COMPMODELS_OMEX_MANIFEST,
        SHOWCASE_OMEX_MANIFEST,
    ],
)
def test_manifest_to_file(manifest_path: Path, tmp_path: Path) -> None:
    """Test that manifest can be writen to manifest.xml."""
    manifest = Manifest.from_manifest(manifest_path)

    manifest2_path = tmp_path / "manifest.xml"
    manifest.to_manifest(manifest2_path)
    manifest2 = Manifest.from_manifest(manifest2_path)
    assert manifest2
    assert len(manifest) == len(manifest2)

    for k, e in enumerate(manifest.entries):
        e2 = manifest2.entries[k]
        assert e.location == e2.location
        assert e.format == e2.format
        assert e.master == e2.master


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


@pytest.mark.parametrize(
    "omex_path",
    [
        COMPMODELS_OMEX,
        SHOWCASE_OMEX,
        BIOMODELS_OMEX,
    ],
)
def test_read_omex(omex_path: Path) -> None:
    """Test reading of omex files."""
    omex = Omex.from_omex(omex_path)
    assert omex
    assert omex.manifest


def test_remove_entry_omex() -> None:
    """Test removing entry from omex file."""
    omex = Omex.from_omex(COMPMODELS_OMEX)
    omex_len = len(omex.manifest)
    omex.remove_entry_for_location("./README.md")
    assert len(omex.manifest) == omex_len - 1


def test_omex_to_directory(tmp_path: Path) -> None:
    """Test export to directory."""
    omex = Omex.from_omex(COMPMODELS_OMEX)
    omex.to_directory(tmp_path)
    for e in omex.manifest.entries:
        if e.location != ".":
            assert (tmp_path / e.location).exists()

    omex2 = Omex.from_directory(tmp_path)
    for k, e in enumerate(omex.manifest.entries):
        e2 = omex2.manifest.entries[k]
        assert e.location == e2.location
        assert e.format == e2.format
        assert e.master == e2.master


def test_omex_to_omex(tmp_path: Path) -> None:
    """Test export to directory."""
    omex = Omex.from_omex(COMPMODELS_OMEX)
    omex_path = tmp_path / "example.omex"
    omex.to_omex(omex_path)

    assert omex_path.exists()

    omex2 = Omex.from_omex(omex_path)

    for k, e in enumerate(omex.manifest.entries):
        e2 = omex2.manifest.entries[k]
        assert e.location == e2.location
        assert e.format == e2.format
        assert e.master == e2.master


@pytest.mark.parametrize(
    "omex_path, omex_flag",
    [
        (COMPMODELS_OMEX, True),
        (SHOWCASE_OMEX, True),
        (BIOMODELS_OMEX, True),
        (COMPMODELS_OMEX_MANIFEST, False),
        (SHOWCASE_OMEX_MANIFEST, False),
    ],
)
def test_is_omex(omex_path: Path, omex_flag: bool) -> None:
    """Test if path is a COMBINE archive."""
    assert Omex.is_omex(omex_path) == omex_flag


def test_entries_by_format() -> None:
    """Test that entries can be retrieved by format key."""
    omex = Omex.from_omex(SHOWCASE_OMEX)
    sbml_entries = omex.entries_by_format("sbml")
    assert sbml_entries
    assert len(sbml_entries) == 1
    assert sbml_entries[0].format.startswith(
        "http://identifiers.org/combine.specifications/sbml"
    )

    sedml_entries = omex.entries_by_format("sedml")
    assert sedml_entries
    assert len(sedml_entries) == 2
    assert sedml_entries[0].format.startswith(
        "http://identifiers.org/combine.specifications/sed-ml"
    )
