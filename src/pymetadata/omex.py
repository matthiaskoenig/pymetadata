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
import pprint
import shutil
import tempfile
import warnings
import zipfile
import xmltodict
import json
from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple, Dict
from pydantic import BaseModel

import libcombine

from pymetadata import log
from pymetadata.console import console

logger = log.get_logger(__name__)


# libcombine.KnownFormats.lookupFormat(formatKey=format_key)

class MetadataEntry(BaseModel):
    location: str


class ManifestEntry(BaseModel):
    """Entry of an OMEX file listed in the `manfiest.xml`.

    This corresponds to a single file in the archive which is tracked in the
    manifest.xml.
        location: location of the entry
        format: full format string
        master: master attribute
    """
    location: str
    format: str
    master: bool = False


class ManifestEntry(BaseModel):
    """Entry of an OMEX file listed in the `manfiest.xml`.

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
            location=".",
            format='http://identifiers.org/combine.specifications/omex'
        ),
        ManifestEntry(
            location="./manifest.xml",
            format='http://identifiers.org/combine.specifications/omex-manifest'
        ),
    ]

    @classmethod
    def from_manifest(cls, manifest_path: Path):
        with open(manifest_path, "r") as f_manifest:
            xml = f_manifest.read()
            d = xmltodict.parse(xml)

            # attributes have @ prefix
            entries = []
            for e in d['omexManifest']['content']:
                entries.append(
                    {k.replace('@', ''): v for (k, v) in e.items()}
                )

            return Manifest(**{'entries': entries})

    def __len__(self) -> int:
        """Get number of entries."""
        return len(self.entries)

    def to_manifest_xml(self) -> str:
        """Create xml of manifest."""
        def content_line(e: ManifestEntry):
            if e.master:
                master_token = ' master="true"'
            else:
                master_token = ''
            return f'  <content location="{e.location}" format="{e.location}"{master_token} />'


        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<omexManifest xmlns="http://identifiers.org/combine.specifications/omex-manifest">',
        ] + [content_line(e) for e in self.entries] + [
            '</omexManifest>'
        ]
        return "\n".join(lines)

    def to_manifest(self, manifest_path: Path) -> None:
        """Write manifest.xml."""
        with open(manifest_path, "w") as f_manifest:
            xml = self.to_manifest_xml()
            console.print(xml)
            f_manifest.write(xml)

class Omex:
    """Combine archive class."""

    def __init__(self):
        """Create COMBINE archive.

        :param omex_path: path to COMBINE archive file
        :param working_dir: working directory for archive, if left empty a temporary
                            directory is used.
        """
        self.entries: Dict[str, ManifestEntry] = {}

        # FIXME: ensure this is removed correctly under all circumstances
        self._tmp_dir = tempfile.mkdtemp()

    def __exit__(self, exc_type, exc_value, traceback):
        shutil.rmtree(self._tmp_dir)


    def __repr__(self) -> str:
        """Get representation string."""
        return f"Omex<{self.omex_path}, working_dir={self.working_dir}>"

    def __str__(self) -> str:
        """Get contents of archive string."""
        return pprint.pformat(self.list_contents())


    def to_omex(self, omex_path: Optional[Path] = None):
        """Write omex to path.

        :param omex_path:
        :return:
        """
        if isinstance(omex_path, str):
            logger.warning(f"'omex_path' should be 'Path': '{omex_path}'")
            omex_path = Path(omex_path)

        raise NotImplementedError

    @staticmethod
    def from_omex(omex_path: Path):
        """Read omex from given path.

        :param omex_path:
        :return:
        """
        omex = Omex()

        # extract archive to tmp file
        with tempfile.TemporaryDirectory as tmp_dir:
            zip_ref = zipfile.ZipFile(omex_path, "r")
            zip_ref.extractall(tmp_dir)
            zip_ref.close()

        # TODO: add all entries with manifest information

        # TODO: validate that entries correspond to manifest

        # TODO: read metadata

        raise NotImplementedError

    def entries_from_manifest(self, manifest_path: ManifestEntry):
        """Read entries from given manifest."""


        o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
        json.dumps(o)  # '{"e": {"a": ["text", "text"]}}'





    def manifest_xml(self):
        """Creates the manifest xml from the entries."""
        raise NotImplementedError

    def manifest_dict(self):
        """Creates manifest dict."""
        raise NotImplementedError

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

        # TODO: copy the tmp_dir

        # TODO: write the manifest file

        # TODO: write metadata

        raise NotImplementedError


    @classmethod
    def from_directory(
        cls,
        omex_path: Path,
        directory: Path,
    ) -> "Omex":
        """Create a COMBINE archive from a given folder.

        The file types are inferred,
        in case of existing manifest or metadata information this should be reused.

        For all SED-ML files in the directory the master attribute is set to True.

        :param directory: Directory to compress
        :param omex_path: Output path for omex directory
        :param creators: List of creators
        :return:
        """

        manifest_path: Path = directory / "manifest.xml"

        if manifest_path.exists():
            warnings.warn(
                f"Manifest file exists in directory, but not used in COMBINE "
                f"archive creation: {manifest_path}"
            )
            # FIXME: reuse existing manifest

        # add the base entry
        entries = [
            Entry(
                location=".",
                format="https://identifiers.org/combine.specifications/omex",
                master=False,
            )
        ]

        # iterate over all locations & guess format
        for root, _dirs, files in os.walk(str(directory)):
            for file in files:
                file_path = os.path.join(root, file)
                location = os.path.relpath(file_path, directory)
                # guess the format
                format = libcombine.KnownFormats.guessFormat(file_path)
                master = False
                if libcombine.KnownFormats.isFormat(formatKey="sed-ml", format=format):
                    master = True

                entries.append(
                    Entry(
                        location=location,
                        format=format,
                        master=master,
                    )
                )

        # create additional metadata if available

        # write all the entries
        print("-" * 80)
        print(omex_path)
        print("-" * 80)
        omex = cls.from_entries(
            omex_path=omex_path, entries=entries, working_dir=directory
        )
        print("-" * 80)

        return omex

    def add_entry(self, entry_path: Path, entry: ManifestEntry):
        """Add a path to the combine archive."""

        # copies the entry_path to tmp_dir and adds the entry
        raise NotImplementedError

    def remove_entry(self, entry: ManifestEntry):

        raise NotImplementedError

    def remove_location(self, location: str):
        raise NotImplementedError


    # def _from_entries(self, entries: Iterable[Entry], add_entries: bool) -> None:
    #     """Create archive from given entries.
    #
    #     :param entries: entries which should be in the archive.
    #     :param add_entries: boolean flag to add entries or create new archive
    #     :return:
    #     """
    #
    #     # timestamp
    #     time_now = libcombine.OmexDescription.getCurrentDateAndTime()
    #
    #     for entry in entries:
    #         print(entry)
    #         location = entry.location
    #         path = os.path.join(str(self.working_dir), location)
    #         if not os.path.exists(path):
    #             raise IOError(f"File does not exist at given location: {path}")
    #
    #         archive.addFile(path, location, entry.format, entry.master)
    #
    #     archive.writeToFile(str(self.omex_path))
    #     archive.cleanUp()





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


    # def list_contents(self, method: str = "omex") -> List["Content"]:
    #     """Return list of contents of the combine archive.
    #
    #     :param omexPath:
    #     :param method: method to extract content, only 'omex' supported
    #     :return: list of contents
    #     """
    #     if method not in ["omex"]:
    #         raise ValueError("Method is not supported: {method}")
    #
    #     contents = []
    #     omex = self._omex_init()
    #
    #     for i in range(omex.getNumEntries()):
    #         entry = omex.getEntry(i)
    #         location = entry.getLocation()
    #         format = entry.getFormat()
    #         master = entry.getMaster()
    #         info = None
    #         for formatKey in ["sed-ml", "sbml", "sbgn", "cellml"]:
    #             if libcombine.KnownFormats_isFormat(formatKey, format):
    #                 info = omex.extractEntryToString(location)
    #
    #         content = Content(
    #             location=location,
    #             format=format,
    #             master=master,
    #             info=info,
    #         )
    #
    #         contents.append(content)
    #
    #     omex.cleanUp()
    #
    #     return contents



