"""
COMBINE Archive helper functions and classes based on libCOMBINE.

Here common operations with COMBINE archives are implemented, like
extracting archives, creating archives from entries or directories,
adding metadata, listing content of archives.

When working with COMBINE archives these wrapper functions should be used.

TODO: core
- [ ] correct handling files
- [ ] correct handling manifest.xml
- [ ] print tree
- [ ] Enum for (common) data types
- [ ] Operate with temporary working dir
- Printing/plotting of manifest (Tree views with types)
- Support for metadata
- Validation of content against manifest; fix manifest options
- Examples

TODO: metadata
- [ ] handle metadata

            if entry.description or entry.creators:
                omex_description: libcombine.OmexDescription = (
                    libcombine.OmexDescription()
                )
                omex_description.setAbout(location)
                omex_description.setCreated(time_now)

                if entry.description:
                    omex_description.setDescription(entry.description)

                if entry.creators:
                    for c in entry.creators:
                        creator: libcombine.VCard = libcombine.VCard()
                        creator.setFamilyName(c.familyName)
                        creator.setGivenName(c.givenName)
                        creator.setEmail(c.email)
                        creator.setOrganization(c.organization)

                        omex_description.addCreator(creator)

                archive.addMetadata(location, omex_description)

"""

import os
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Dict, List, Optional

import libcombine
import xmltodict
from pydantic import BaseModel, PrivateAttr

from pymetadata import log
from pymetadata.console import console


logger = log.get_logger(__name__)


class ManifestEntry(BaseModel):
    """Entry of an OMEX file listed in the `manifest.xml`.

    This corresponds to a single file in the archive which is tracked in the
    manifest.xml.
        location: location of the entry
        format: full format string
        master: master attribute
    """

    location: str
    format: str
    master: bool = False


class Manifest(BaseModel):
    """COMBINE archive manifest.

    A manifest is a list of ManifestEntries.
    """

    entries: List[ManifestEntry] = [
        ManifestEntry(
            location=".", format="http://identifiers.org/combine.specifications/omex"
        ),
        ManifestEntry(
            location="./manifest.xml",
            format="http://identifiers.org/combine.specifications/omex-manifest",
        ),
    ]
    _entries_dict: Dict[str, ManifestEntry] = PrivateAttr()

    def __init__(self, **data) -> None:  # type: ignore
        super().__init__(**data)
        self._entries_dict = {e.location: e for e in self.entries}

    def __contains__(self, location: str) -> bool:
        """Check if location is in manifest."""
        return location in self._entries_dict

    def __getitem__(self, location: str) -> ManifestEntry:
        """Get entry by location."""
        return self._entries_dict[location]

    def __len__(self) -> int:
        """Get number of entries."""
        return len(self.entries)

    @classmethod
    def from_manifest(cls, manifest_path: Path) -> "Manifest":
        """Create manifest from existing manifest.xml file."""
        with open(manifest_path, "r") as f_manifest:
            xml = f_manifest.read()
            d = xmltodict.parse(xml)

            # attributes have @ prefix
            entries = []
            for e in d["omexManifest"]["content"]:
                entries.append({k.replace("@", ""): v for (k, v) in e.items()})

            return Manifest(**{"entries": entries})

    def to_manifest_xml(self) -> str:
        """Create xml of manifest."""

        def content_line(e: ManifestEntry) -> str:
            if e.master:
                master_token = ' master="true"'
            else:
                master_token = ""
            return f'  <content location="{e.location}" format="{e.format}"{master_token} />'

        lines = (
            [
                '<?xml version="1.0" encoding="UTF-8"?>',
                '<omexManifest xmlns="http://identifiers.org/combine.specifications/omex-manifest">',
            ]
            + [content_line(e) for e in self.entries]
            + ["</omexManifest>"]
        )
        return "\n".join(lines)

    def to_manifest(self, manifest_path: Path) -> None:
        """Write manifest.xml."""
        with open(manifest_path, "w") as f_manifest:
            xml = self.to_manifest_xml()
            f_manifest.write(xml)

    def add_entry(self, entry: ManifestEntry) -> None:
        """Add entry to manifest.

        Does not check for duplication.
        """
        if not entry.location.startswith("./"):
            raise ValueError(
                f"Locations must be relative paths in COMBINE archive, but location is "
                f"'{entry.location}'."
            )

        self.entries.append(entry)
        self._entries_dict[entry.location] = entry

    def remove_entry_for_location(self, location: str) -> Optional[ManifestEntry]:
        """Remove entry for given location."""
        if location in [".", "./manifest.xml"]:
            logger.error(
                f"Core location cannot be removed from manifest: '{location}'."
            )
            return None
        if location not in self:
            logger.error(f"The location '{location}' does not exist in manifest.")
            return None
        else:
            entry = self._entries_dict.pop(location)
            self.entries = [e for e in self.entries if e.location != location]
            return entry


class Omex:
    """Combine archive class."""

    def __init__(self) -> None:
        """Create COMBINE archive.

        :param omex_path: path to COMBINE archive file
        :param working_dir: working directory for archive, if left empty a temporary
                            directory is used.
        """
        self.manifest: Manifest = Manifest()
        self._tmp_dir: Path = Path(tempfile.mkdtemp())

    def __exit__(self, exc_type, exc_value, traceback):  # type: ignore
        """Cleanup on exit."""
        shutil.rmtree(self._tmp_dir)

    def __str__(self) -> str:
        """Get contents of archive string."""
        return str(self.manifest.dict())

    @staticmethod
    def from_omex(omex_path: Path) -> "Omex":
        """Read omex from given path.

        :param omex_path:
        :return: Omex object
        """
        if isinstance(omex_path, str):
            logger.warning(f"'omex_path' should be 'Path': '{omex_path}'")
            omex_path = Path(omex_path)

        if not omex_path.exists:
            raise ValueError(f"'omex_path' does not exist: '{omex_path}'.")
        if not omex_path.is_file():
            raise ValueError(f"'omex_path' is not a file: '{omex_path}'.")

        # extract archive to tmp directory
        with tempfile.TemporaryDirectory() as tmp_dir:
            zip_ref = zipfile.ZipFile(omex_path, "r")
            zip_ref.extractall(tmp_dir)
            zip_ref.close()

            return Omex.from_directory(Path(tmp_dir))

    @classmethod
    def from_directory(cls, directory: Path) -> "Omex":
        """Create a COMBINE archive from a given directory.

        The file types are inferred,
        in case of existing manifest or metadata information this should be reused.

        For all SED-ML files in the directory the master attribute is set to True.
        """
        if isinstance(directory, str):
            logger.warning(f"'directory' should be 'Path': '{directory}'")
            directory = Path(directory)

        if not directory.exists:
            msg = f"'directory' does not exist: '{directory}'."
            logger.error(msg)
            raise ValueError(msg)

        if not directory.is_dir():
            msg = f"'directory' is not a directory: '{directory}'."
            logger.error(msg)
            raise ValueError(msg)

        manifest_path: Path = directory / "manifest.xml"
        manifest: Optional[Manifest] = None
        if manifest_path.exists():
            manifest = Manifest.from_manifest(manifest_path)
        else:
            logger.warning(f"No 'manifest.xml' in directory: '{directory}'.")

        # new archive
        omex = Omex()

        # iterate over all locations and add entry
        for root, _dirs, files in os.walk(str(directory)):
            for file in files:
                file_path = os.path.join(root, file)
                location = f"./{os.path.relpath(file_path, directory)}"
                if location == "./manifest.xml":
                    # manifest is created from the internal manifest entries
                    continue

                logger.debug(f"'{file_path}' -> '{location}'")
                entry: ManifestEntry
                if manifest and location in manifest:
                    # use entry from existing manifest
                    entry = manifest[location]
                else:
                    if manifest and location not in manifest:
                        logger.warning(
                            f"Location missing from existing manifest.xml: '{location}'"
                        )

                    format = libcombine.KnownFormats.guessFormat(file_path)
                    master = False
                    if libcombine.KnownFormats.isFormat(
                        formatKey="sed-ml", format=format
                    ):
                        master = True
                    entry = ManifestEntry(
                        location=location,
                        format=format,
                        master=master,
                    )

                omex.add_entry(entry_path=Path(file_path), entry=entry)

        return omex

    def add_entry(self, entry_path: Path, entry: ManifestEntry) -> None:
        """Add a path to the combine archive.

        The corresponding ManifestEntry information is required.
        """
        if isinstance(entry_path, str):
            logger.warning(f"'entry_path' should be 'Path': '{entry_path}'")
            entry_path = Path(entry_path)

        if not entry_path.exists:
            msg = f"'entry_path' does not exist: '{entry_path}'."
            logger.error(msg)
            raise ValueError(msg)

        if not entry_path.is_file():
            raise ValueError(f"'entry_path' is not a file: '{entry_path}'.")

        if entry.location in self.manifest:
            logger.warning(
                f"Location already exists and is overwritten: '{entry.location}'."
            )
            self.manifest.remove_entry_for_location(entry.location)

        # copy path
        destination = self._tmp_dir / entry.location
        if not destination.parent.exists():
            destination.parent.mkdir(parents=True)
        shutil.copy2(src=str(entry_path), dst=str(destination))

        # add entry
        self.manifest.add_entry(entry)

    def remove_entry_for_location(self, location: str) -> Optional[ManifestEntry]:
        """Remove entry and corresponding entry_path."""
        entry = self.manifest.remove_entry_for_location(location)
        if entry:
            destination = self._tmp_dir / entry.location
            os.remove(destination)
        return entry

    def to_omex(self, omex_path: Path) -> None:
        """Write omex to path.

        :param omex_path:
        :return:
        """
        if isinstance(omex_path, str):
            logger.warning(f"'omex_path' should be 'Path': '{omex_path}'")
            omex_path = Path(omex_path)

        if omex_path.exists():
            logger.warning(f"Existing omex is overwritten: '{omex_path}'")

        # write tmp dir
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.to_directory(output_dir=Path(tmp_dir))

            # compress directory as zip
            with zipfile.ZipFile(omex_path, mode="w") as zf:
                for e in self.manifest.entries:
                    if e.location != ".":
                        f = Path(tmp_dir) / e.location
                        zf.write(filename=str(f), arcname=e.location)

                # zf.printdir()

    def to_directory(self, output_dir: Path) -> None:
        """Extract combine archive to output directory.

        :param output_dir: output directory
        :return:
        """

        if isinstance(output_dir, str):
            logger.warning(f"'output_dir' should be 'Path': '{output_dir}'")
            output_dir = Path(output_dir)

        if output_dir and not output_dir.exists():
            logger.warning(f"Creating working directory: {output_dir}")
            output_dir.mkdir(parents=True, exist_ok=True)

        # iterate over all locations and copy to destination
        for entry in self.manifest.entries:
            if entry.location in [".", "./manifest.xml"]:
                continue
            src = self._tmp_dir / entry.location
            destination = output_dir / entry.location
            destination.parent.mkdir(parents=True, exist_ok=True)
            logger.debug(f"'{src}' -> '{destination}")
            shutil.copy2(src=str(src), dst=str(destination))

        # write manifest.xml
        self.manifest.to_manifest(manifest_path=output_dir / "manifest.xml")

    # def locations_by_format(
    #     self, format_key: str = None, method: str = "omex"
    # ) -> List[Tuple[str, bool]]:
    #     """Get locations to files with given format in the archive.
    #
    #     Uses the libcombine KnownFormats for formatKey, e.g., 'sed-ml' or 'sbml'.
    #     Files which have a master=True have higher priority and are listed first.
    #
    #     :param omex_path:
    #     :param format_key:
    #     :param method:
    #     :return: List of files with master flags
    #     """
    #     if not format_key:
    #         raise ValueError("Format must be specified.")
    #
    #     locations: List[Tuple[str, bool]] = []
    #
    #     if method == "omex":
    #         archive: libcombine.CombineArchive = self._omex_init()
    #
    #         for i in range(archive.getNumEntries()):
    #             entry: libcombine.CaContent = archive.getEntry(i)
    #             format: str = entry.getFormat()
    #             master: bool = entry.getMaster()
    #             if libcombine.KnownFormats.isFormat(format_key, format):
    #                 loc: str = entry.getLocation()
    #                 if (master is None) or (master is False):
    #                     locations.append((loc, False))
    #                 else:
    #                     locations.append((loc, True))
    #         archive.cleanUp()
    #
    #     elif method == "zip":
    #         logger.warning("Master flag cannot be resolved, use method 'omex' instead.")
    #         # extract to tmpfile and guess format
    #         tmp_dir = tempfile.mkdtemp()
    #
    #         try:
    #             self.extract(output_dir=Path(tmp_dir), method="zip")
    #
    #             # iterate over all locations & guess format
    #             for root, _dirs, files in os.walk(tmp_dir):
    #                 for file in files:
    #                     file_path = os.path.join(root, file)
    #                     location = os.path.relpath(file_path, tmp_dir)
    #                     # guess the format
    #                     format = libcombine.KnownFormats.guessFormat(file_path)
    #                     if libcombine.KnownFormats.isFormat(
    #                         formatKey=format_key, format=format
    #                     ):
    #                         locations.append((location, False))
    #
    #         finally:
    #             shutil.rmtree(tmp_dir)
    #
    #     else:
    #         raise ValueError(f"Method is not supported '{method}'")
    #
    #     return locations
