"""Test omex."""

import gc
import zipfile
from pathlib import Path

import pytest
from pydantic import ValidationError

from pymetadata.omex import EntryFormat, Manifest, ManifestEntry, Omex


@pytest.fixture(scope="session")
def data_directory() -> Path:
    """Path to test data directory."""
    return Path(__file__).parent / "data"


SHOWCASE_OMEX = "CombineArchiveShowCase.omex"
COMPMODELS_OMEX = "CompModels.omex"
BIOMODELS_OMEX = "BIOMD0000000001.omex"
ICGB21FR_OMEX = "iCGB21FR.omex"
SHOWCASE_OMEX_MANIFEST = "CombineArchiveShowCase_manifest.xml"
COMPMODELS_OMEX_MANIFEST = "CompModels_manifest.xml"


def test_entry_from_dict() -> None:
    """Test entry creation from dictionary."""
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
    """Test manifest conversion to dictionary."""
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


def test_manifest_from_file(data_directory: Path) -> None:
    """Test that manifest can be created from file."""
    manifest_path = data_directory / "omex" / COMPMODELS_OMEX_MANIFEST
    manifest = Manifest.from_manifest(manifest_path)
    assert manifest
    assert len(manifest) == 6


@pytest.mark.parametrize(
    "manifest_filename",
    [
        COMPMODELS_OMEX_MANIFEST,
        SHOWCASE_OMEX_MANIFEST,
    ],
)
def test_manifest_to_file(
    manifest_filename: str, data_directory: Path, tmp_path: Path
) -> None:
    """Test that manifest can be writen to manifest.xml."""
    manifest = Manifest.from_manifest(data_directory / "omex" / manifest_filename)

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


def test_adding_removing_entry_manifest_no_dot() -> None:
    """Testing adding and removing entries from manifest without dots."""
    manifest = Manifest()
    assert "." in manifest
    assert "./manifest.xml" in manifest
    assert manifest
    assert len(manifest) == 2
    manifest.add_entry(
        ManifestEntry(location="models/model.xml", format="sbml", master=False)
    )
    assert "./models/model.xml" in manifest
    assert len(manifest) == 3

    entry = manifest.remove_entry_for_location(location="models/model.xml")
    assert entry
    assert entry.location == "./models/model.xml"
    assert len(manifest) == 2


@pytest.mark.parametrize(
    "omex_filename",
    [
        COMPMODELS_OMEX,
        SHOWCASE_OMEX,
        BIOMODELS_OMEX,
        ICGB21FR_OMEX,
    ],
)
def test_read_omex(omex_filename: str, data_directory: Path) -> None:
    """Test reading of omex files."""
    omex = Omex.from_omex(data_directory / "omex" / omex_filename)
    assert omex
    assert omex.manifest


def test_remove_entry_omex(data_directory: Path) -> None:
    """Test removing entry from omex file."""
    omex = Omex.from_omex(data_directory / "omex" / COMPMODELS_OMEX)
    omex_len = len(omex.manifest)
    omex.remove_entry_for_location("./README.md")
    assert len(omex.manifest) == omex_len - 1


def test_omex_to_directory(data_directory: Path, tmp_path: Path) -> None:
    """Test export to directory."""
    omex = Omex.from_omex(data_directory / "omex" / COMPMODELS_OMEX)
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


def test_omex_to_omex(data_directory: Path, tmp_path: Path) -> None:
    """Test export to directory."""
    omex = Omex.from_omex(data_directory / "omex" / COMPMODELS_OMEX)
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
    "omex_filename, omex_flag",
    [
        (COMPMODELS_OMEX, True),
        (SHOWCASE_OMEX, True),
        (BIOMODELS_OMEX, True),
        (COMPMODELS_OMEX_MANIFEST, False),
        (SHOWCASE_OMEX_MANIFEST, False),
    ],
)
def test_is_omex(omex_filename: str, omex_flag: bool, data_directory: Path) -> None:
    """Test if path is a COMBINE archive."""
    assert Omex.is_omex(data_directory / "omex" / omex_filename) == omex_flag


def test_entries_by_format(data_directory: Path) -> None:
    """Test that entries can be retrieved by format key."""
    omex = Omex.from_omex(data_directory / "omex" / SHOWCASE_OMEX)
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


def test_omex_from_url() -> None:
    """Read form url."""
    url = "https://github.com/matthiaskoenig/canagliflozin-model/releases/download/0.7.0/canagliflozin_model.omex"
    omex = Omex.from_url(url)
    assert omex


def test_omex_context_manager(data_directory: Path) -> None:
    """Test that the archive can be used as a context manager."""
    omex_path = data_directory / "omex" / SHOWCASE_OMEX
    with Omex.from_omex(omex_path) as omex:
        tmp_dir = omex._tmp_dir
        assert tmp_dir.exists()
        assert len(omex.manifest) > 0

    # the temporary directory is removed when the context is left
    assert not tmp_dir.exists()


SINGLE_ENTRY_MANIFEST = """<?xml version="1.0" encoding="UTF-8"?>
<omexManifest xmlns="http://identifiers.org/combine.specifications/omex-manifest">
  <content location="." format="http://identifiers.org/combine.specifications/omex"/>
</omexManifest>
"""

NO_NAMESPACE_MANIFEST = """<?xml version="1.0" encoding="UTF-8"?>
<omexManifest>
  <content location="." format="http://identifiers.org/combine.specifications/omex"/>
  <content
    location="./model.xml"
    format="http://identifiers.org/combine.specifications/sbml"
    master="true"/>
</omexManifest>
"""


def test_manifest_single_content_entry(tmp_path: Path) -> None:
    """Test manifest with a single content entry.

    An archive with a single file is valid OMEX.
    """
    manifest_path = tmp_path / "manifest.xml"
    manifest_path.write_text(SINGLE_ENTRY_MANIFEST)

    manifest = Manifest.from_manifest(manifest_path)
    assert len(manifest) == 1
    assert "." in manifest


def test_manifest_without_namespace(tmp_path: Path) -> None:
    """Test manifest which does not declare the omex namespace."""
    manifest_path = tmp_path / "manifest.xml"
    manifest_path.write_text(NO_NAMESPACE_MANIFEST)

    manifest = Manifest.from_manifest(manifest_path)
    assert len(manifest) == 2
    assert manifest["./model.xml"].master is True


# locations of a manifest in an order which is neither sorted nor the order in
# which the files are created, so that no file system returns it by chance
ORDERED_LOCATIONS = [
    f"./{directory}{name}.xml"
    for name in ["m", "b", "z", "a", "q", "c", "y", "d"]
    for directory in ["models/", "", "data/"]
]


def _ordered_directory(directory: Path, locations: list[str]) -> Path:
    """Write the files of all locations and a manifest which lists `locations`."""
    for location in sorted(ORDERED_LOCATIONS):
        path = directory / location
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("<sbml/>")

    manifest = Manifest()
    for location in locations:
        manifest.add_entry(ManifestEntry(location=location, format="sbml"))
    manifest.to_manifest(directory / "manifest.xml")
    return directory


def test_from_directory_keeps_manifest_order(tmp_path: Path) -> None:
    """The entries of a directory are in the order of its manifest.

    The order in which the file system returns the files differs between
    machines and must not be the order of the entries.
    """
    directory = _ordered_directory(tmp_path, ORDERED_LOCATIONS)
    omex = Omex.from_directory(directory)
    locations = [entry.location for entry in omex.manifest.entries]
    assert locations == [".", "./manifest.xml", *ORDERED_LOCATIONS]


def test_from_directory_appends_unlisted_files(tmp_path: Path) -> None:
    """Files which the manifest does not list follow the listed ones, sorted."""
    listed = ORDERED_LOCATIONS[:5]
    directory = _ordered_directory(tmp_path, listed)
    omex = Omex.from_directory(directory)
    locations = [entry.location for entry in omex.manifest.entries]
    unlisted = sorted(set(ORDERED_LOCATIONS) - set(listed))
    assert locations == [".", "./manifest.xml", *listed, *unlisted]


def test_from_directory_without_manifest_is_sorted(tmp_path: Path) -> None:
    """Without a manifest the entries are sorted by their location."""
    directory = _ordered_directory(tmp_path, [])
    (directory / "manifest.xml").unlink()
    omex = Omex.from_directory(directory)
    locations = [entry.location for entry in omex.manifest.entries]
    assert locations == [".", "./manifest.xml", *sorted(ORDERED_LOCATIONS)]


def test_omex_roundtrip_keeps_manifest_order(tmp_path: Path) -> None:
    """The order of the entries survives writing and reading an archive."""
    omex = Omex.from_directory(_ordered_directory(tmp_path / "in", ORDERED_LOCATIONS))
    omex_path = tmp_path / "ordered.omex"
    omex.to_omex(omex_path)
    locations = [entry.location for entry in Omex.from_omex(omex_path).manifest.entries]
    assert locations == [".", "./manifest.xml", *ORDERED_LOCATIONS]


@pytest.mark.parametrize(
    "location",
    ["../escaped.txt", "./a/../../escaped.txt", "/abs/file.txt", "C:/file.txt", ""],
)
def test_location_outside_archive_is_rejected(location: str) -> None:
    """Locations must stay inside the archive."""
    with pytest.raises(ValidationError):
        ManifestEntry(location=location, format=EntryFormat.TXT)


@pytest.mark.parametrize(
    "location, normalized",
    [
        (".", "."),
        ("./", "."),
        ("model.xml", "./model.xml"),
        (".hidden", "./.hidden"),
        ("./a//b/./model.xml", "./a/b/model.xml"),
        ("a\\b.xml", "./a/b.xml"),
    ],
)
def test_location_is_normalized(location: str, normalized: str) -> None:
    """Locations are normalized to relative paths starting with `./`."""
    entry = ManifestEntry(location=location, format=EntryFormat.TXT)
    assert entry.location == normalized


def test_add_entry_does_not_escape_archive(tmp_path: Path) -> None:
    """A location changed after creation is validated as well."""
    entry = ManifestEntry(location="./model.txt", format=EntryFormat.TXT)
    with pytest.raises(ValidationError):
        entry.location = "../escaped.txt"


def test_manifest_special_characters_roundtrip(tmp_path: Path) -> None:
    """Locations with XML special characters survive writing and reading."""
    # `"`, `<` and `>` are not allowed in file names on Windows
    name = "a&b 'c'.txt"
    source = tmp_path / "source.txt"
    source.write_text("content", encoding="utf-8")
    omex = Omex()
    omex.add_entry(source, ManifestEntry(location=name, format=EntryFormat.TXT))
    omex_path = tmp_path / "special.omex"
    omex.to_omex(omex_path)

    with Omex.from_omex(omex_path) as omex2:
        assert f"./{name}" in omex2.manifest
        assert omex2.get_path(name).read_text(encoding="utf-8") == "content"


def test_add_entry_unnormalized_location_twice(tmp_path: Path) -> None:
    """Adding the same unnormalized location twice replaces the entry."""
    source = tmp_path / "m.txt"
    source.write_text("content", encoding="utf-8")
    with Omex() as omex:
        for _ in range(2):
            omex.add_entry(source, ManifestEntry(location="m.txt", format="txt"))
        locations = [e.location for e in omex.manifest.entries]
        assert locations == [".", "./manifest.xml", "./m.txt"]
        assert omex.get_path("m.txt").exists()


def test_add_entry_does_not_modify_entry(tmp_path: Path) -> None:
    """The entry passed to `add_entry` is not changed by the archive."""
    source = tmp_path / "m.txt"
    source.write_text("content", encoding="utf-8")
    entry = ManifestEntry(location="./m.txt", format=EntryFormat.TXT)
    with Omex() as omex:
        omex.add_entry(source, entry)
        assert omex.manifest["./m.txt"] is not entry


@pytest.mark.parametrize(
    "format_key, count",
    [("csv", 1), ("CSV", 1), ("SBML_L3V1", 1), ("sbml", 1), ("png", 0)],
)
def test_entries_by_format_name(tmp_path: Path, format_key: str, count: int) -> None:
    """Formats are matched by the name of an `EntryFormat`."""
    source = tmp_path / "m.txt"
    source.write_text("content", encoding="utf-8")
    with Omex() as omex:
        omex.add_entry(
            source, ManifestEntry(location="data.csv", format=EntryFormat.CSV)
        )
        omex.add_entry(
            source,
            ManifestEntry(location="model.xml", format=EntryFormat.SBML_L3V1),
        )
        assert len(omex.entries_by_format(format_key)) == count


def test_temporary_directory_removed_without_context_manager() -> None:
    """The temporary directory is removed when the archive is collected."""
    omex = Omex()
    tmp_dir = omex._tmp_dir
    assert tmp_dir.exists()
    del omex
    gc.collect()
    assert not tmp_dir.exists()


def test_close_removes_temporary_directory() -> None:
    """`close` removes the temporary directory and can be called twice."""
    omex = Omex()
    tmp_dir = omex._tmp_dir
    omex.close()
    omex.close()
    assert not tmp_dir.exists()


def test_guess_format_uppercase_xml(tmp_path: Path) -> None:
    """The content of `.XML` files is inspected like that of `.xml` files."""
    path = tmp_path / "model.XML"
    path.write_text('<?xml version="1.0"?>\n<sbml level="3">', encoding="utf-8")
    assert Omex.guess_format(path) == EntryFormat.SBML.value


def test_guess_format_non_utf8_xml(tmp_path: Path) -> None:
    """The format of an XML file which is not UTF-8 can be guessed."""
    path = tmp_path / "model.xml"
    path.write_bytes('<?xml version="1.0"?>\n<sbml name="é">'.encode("latin-1"))
    assert Omex.guess_format(path) == EntryFormat.SBML.value


@pytest.mark.parametrize("url", ["file:///etc/passwd", "ftp://example.org/a.omex"])
def test_from_url_rejects_scheme(url: str) -> None:
    """Only http and https urls can be read."""
    with pytest.raises(ValueError, match="scheme"):
        Omex.from_url(url)


def test_from_omex_without_manifest_fails(tmp_path: Path) -> None:
    """A zip without `manifest.xml` is not a COMBINE archive."""
    zip_path = tmp_path / "plain.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("model.xml", "<sbml/>")
    with pytest.raises(ValueError, match="manifest"):
        Omex.from_omex(zip_path)


def test_to_omex_keeps_existing_file_on_error(tmp_path: Path) -> None:
    """A failing write does not destroy an existing archive."""
    omex_path = tmp_path / "archive.omex"
    omex_path.write_bytes(b"existing")
    omex = Omex()
    omex.manifest.entries.append(
        ManifestEntry(location="./missing.txt", format=EntryFormat.TXT)
    )
    with pytest.raises(FileNotFoundError):
        omex.to_omex(omex_path)
    assert omex_path.read_bytes() == b"existing"
    assert list(tmp_path.iterdir()) == [omex_path]


def test_manifest_xml_escapes_attributes(tmp_path: Path) -> None:
    """All XML special characters in the attributes are escaped."""
    location = "./a&b \"c\" <d> 'e'.txt"
    manifest = Manifest()
    manifest.add_entry(ManifestEntry(location=location, format=EntryFormat.TXT))
    manifest_path = tmp_path / "manifest.xml"
    manifest.to_manifest(manifest_path)
    assert location in Manifest.from_manifest(manifest_path)
