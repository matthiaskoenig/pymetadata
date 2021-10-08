"""
COMBINE Archive support.

This module provides an abstraction around the COMBINE archive. Common operations
such as archive creation, archive extraction, creating archives from entries or directories,
working with the `manifest.xml` are implemented.

When working with COMBINE archives these wrapper functions should be used.
The current version has no support for metadata manipulation.

TODO: metadata (creates, modifications, ...)
"""

import os
import shutil
import tempfile
import zipfile
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional

import libcombine
import xmltodict
from pydantic import BaseModel, PrivateAttr

from pymetadata import log
from pymetadata.console import console


logger = log.get_logger(__name__)


__all__ = ["EntryFormat", "ManifestEntry", "Manifest", "Omex"]


class EntryFormat(str, Enum):
    """Enum for common formats."""

    SBML = "http://identifiers.org/combine.specifications/sbml"
    SBML_L2V1 = "http://identifiers.org/combine.specifications/sbml.level-2.version-1"
    SBML_L2V2 = "http://identifiers.org/combine.specifications/sbml.level-2.version-2"
    SBML_L2V3 = "http://identifiers.org/combine.specifications/sbml.level-2.version-3"
    SBML_L2V4 = "http://identifiers.org/combine.specifications/sbml.level-2.version-4"
    SBML_L2V5 = "http://identifiers.org/combine.specifications/sbml.level-2.version-5"
    SBML_L3V1 = "http://identifiers.org/combine.specifications/sbml.level-3.version-1"
    SBML_L3V2 = "http://identifiers.org/combine.specifications/sbml.level-3.version-2"

    SEDML = "http://identifiers.org/combine.specifications/sed-ml"
    SEDML_L1V1 = (
        "http://identifiers.org/combine.specifications/sed-ml.level-1.version-1"
    )
    SEDML_L1V2 = (
        "http://identifiers.org/combine.specifications/sed-ml.level-1.version-2"
    )
    SEDML_L1V3 = (
        "http://identifiers.org/combine.specifications/sed-ml.level-1.version-3"
    )

    CELLML = "http://identifiers.org/combine.specifications/cellml"
    SBGN = "http://identifiers.org/combine.specifications/sbgn"
    SBGN_PD = "http://identifiers.org/combine.specifications/sbgn.pd"

    OMEX_METADATA = "http://identifiers.org/combine.specifications/omex-metadata"

    MARKDOWN = "http://purl.org/NET/mediatypes/text/x-markdown"
    PNG = "http://purl.org/NET/mediatypes/image/png"
    SVG = "http://purl.org/NET/mediatypes/image/svg+xml"
    PDF = "http://purl.org/NET/mediatypes/application/pdf"
    XML = "http://purl.org/NET/mediatypes/application/xml"
    PLAIN = "http://purl.org/NET/mediatypes/text/plain"


# FIXME: info from https://github.com/sbmlteam/libCombine/blob/master/src/combine/knownformats.cpp
# "sbml",{
#       "http://identifiers.org/combine.specifications/sbml",
#       "http://identifiers.org/combine.specifications/sbml.level-1.version-1",
#       "http://identifiers.org/combine.specifications/sbml.level-1.version-2",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version-1",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version-2",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version-3",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version-4",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version-5",
#       "http://identifiers.org/combine.specifications/sbml.level-3.version-1",
#       "http://identifiers.org/combine.specifications/sbml.level-3.version-2",
#       "http://identifiers.org/combine.specifications/sbml.level-1.version.1",
#       "http://identifiers.org/combine.specifications/sbml.level-1.version.2",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version.1",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version.2",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version.3",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version.4",
#       "http://identifiers.org/combine.specifications/sbml.level-2.version.5",
#       "http://identifiers.org/combine.specifications/sbml.level-3.version.1",
#       "http://identifiers.org/combine.specifications/sbml.level-3.version.2",
#     } },
#     { "sedml",
#     {
#       "http://identifiers.org/combine.specifications/sed-ml",
#       "http://identifiers.org/combine.specifications/sedml",
#       "http://identifiers.org/combine.specifications/sed-ml.level-1.version-1",
#       "http://identifiers.org/combine.specifications/sed-ml.level-1.version-2",
#       "http://identifiers.org/combine.specifications/sed-ml.level-1.version-3"
#     } },
#     { "cellml",{ "http://identifiers.org/combine.specifications/cellml" } },
#     { "sed-ml",
#     {
#       "http://identifiers.org/combine.specifications/sed-ml",
#       "http://identifiers.org/combine.specifications/sedml",
#       "http://identifiers.org/combine.specifications/sed-ml.level-1.version-1",
#       "http://identifiers.org/combine.specifications/sed-ml.level-1.version-2",
#       "http://identifiers.org/combine.specifications/sed-ml.level-1.version-3"
#     } },
#     { "sbgn",{ "http://identifiers.org/combine.specifications/sbgn" } },
#     { "omex",{ "http://identifiers.org/combine.specifications/omex-metadata" } },
#     { "manifest",{
#       "http://identifiers.org/combine.specifications/omex",
#       "http://identifiers.org/combine.specifications/omex-manifest",
#       "http://identifiers.org/combine.specifications/omex.version-1",
#     } },
#     { "copasi",{ "application/x-copasi" } },
#     { "sedx",{ "application/x-sed-ml-archive" } },
#     { "png",{ "image/png" } },
#     { "csv",{ "text/csv" } },
#     { "323",{ "text/h323" } },
#     { "acx",{ "application/internet-property-stream" } },
#     { "ai",{ "application/postscript" } },
#     { "aif",{ "audio/x-aiff" } },
#     { "aifc",{ "audio/x-aiff" } },
#     { "aiff",{ "audio/x-aiff" } },
#     { "asf",{ "video/x-ms-asf" } },
#     { "asr",{ "video/x-ms-asf" } },
#     { "asx",{ "video/x-ms-asf" } },
#     { "au",{ "audio/basic" } },
#     { "avi",{ "video/x-msvideo" } },
#     { "axs",{ "application/olescript" } },
#     { "bas",{ "text/plain" } },
#     { "bcpio",{ "application/x-bcpio" } },
#     { "bin",{ "application/octet-stream" } },
#     { "bmp",{ "image/bmp" } },
#     { "c",{ "text/plain" } },
#     { "cat",{ "application/vnd.ms-pkiseccat" } },
#     { "cdf",{ "application/x-cdf" } },
#     { "cer",{ "application/x-x509-ca-cert" } },
#     { "class",{ "application/octet-stream" } },
#     { "clp",{ "application/x-msclip" } },
#     { "cmx",{ "image/x-cmx" } },
#     { "cod",{ "image/cis-cod" } },
#     { "cpio",{ "application/x-cpio" } },
#     { "crd",{ "application/x-mscardfile" } },
#     { "crl",{ "application/pkix-crl" } },
#     { "crt",{ "application/x-x509-ca-cert" } },
#     { "csh",{ "application/x-csh" } },
#     { "css",{ "text/css" } },
#     { "dcr",{ "application/x-director" } },
#     { "der",{ "application/x-x509-ca-cert" } },
#     { "dir",{ "application/x-director" } },
#     { "dll",{ "application/x-msdownload" } },
#     { "dms",{ "application/octet-stream" } },
#     { "doc",{ "application/msword" } },
#     { "dot",{ "application/msword" } },
#     { "dvi",{ "application/x-dvi" } },
#     { "dxr",{ "application/x-director" } },
#     { "eps",{ "application/postscript" } },
#     { "etx",{ "text/x-setext" } },
#     { "evy",{ "application/envoy" } },
#     { "exe",{ "application/octet-stream" } },
#     { "fif",{ "application/fractals" } },
#     { "flr",{ "x-world/x-vrml" } },
#     { "gif",{ "image/gif" } },
#     { "gtar",{ "application/x-gtar" } },
#     { "gz",{ "application/x-gzip" } },
#     { "h",{ "text/plain" } },
#     { "hdf",{ "application/x-hdf" } },
#     { "hlp",{ "application/winhlp" } },
#     { "hqx",{ "application/mac-binhex40" } },
#     { "hta",{ "application/hta" } },
#     { "htc",{ "text/x-component" } },
#     { "htm",{ "text/html" } },
#     { "html",{ "text/html" } },
#     { "htt",{ "text/webviewhtml" } },
#     { "ico",{ "image/x-icon" } },
#     { "ief",{ "image/ief" } },
#     { "iii",{ "application/x-iphone" } },
#     { "ins",{ "application/x-internet-signup" } },
#     { "isp",{ "application/x-internet-signup" } },
#     { "jfif",{ "image/pipeg" } },
#     { "jpe",{ "image/jpeg" } },
#     { "jpeg",{ "image/jpeg" } },
#     { "jpg",{ "image/jpeg" } },
#     { "js",{ "application/x-javascript" } },
#     { "latex",{ "application/x-latex" } },
#     { "lha",{ "application/octet-stream" } },
#     { "lsf",{ "video/x-la-asf" } },
#     { "lsx",{ "video/x-la-asf" } },
#     { "lzh",{ "application/octet-stream" } },
#     { "m",{ "application/x-matlab" } },
#     { "mat",{ "application/x-matlab-data" } },
#     { "m13",{ "application/x-msmediaview" } },
#     { "m14",{ "application/x-msmediaview" } },
#     { "m3u",{ "audio/x-mpegurl" } },
#     { "man",{ "application/x-troff-man" } },
#     { "mdb",{ "application/x-msaccess" } },
#     { "me",{ "application/x-troff-me" } },
#     { "mht",{ "message/rfc822" } },
#     { "mhtml",{ "message/rfc822" } },
#     { "mid",{ "audio/mid" } },
#     { "mny",{ "application/x-msmoney" } },
#     { "mov",{ "video/quicktime" } },
#     { "movie",{ "video/x-sgi-movie" } },
#     { "mp2",{ "video/mpeg" } },
#     { "mp3",{ "audio/mpeg" } },
#     { "mpa",{ "video/mpeg" } },
#     { "mpe",{ "video/mpeg" } },
#     { "mpeg",{ "video/mpeg" } },
#     { "mpg",{ "video/mpeg" } },
#     { "mpp",{ "application/vnd.ms-project" } },
#     { "mpv2",{ "video/mpeg" } },
#     { "ms",{ "application/x-troff-ms" } },
#     { "mvb",{ "application/x-msmediaview" } },
#     { "nws",{ "message/rfc822" } },
#     { "oda",{ "application/oda" } },
#     { "p10",{ "application/pkcs10" } },
#     { "p12",{ "application/x-pkcs12" } },
#     { "p7b",{ "application/x-pkcs7-certificates" } },
#     { "p7c",{ "application/x-pkcs7-mime" } },
#     { "p7m",{ "application/x-pkcs7-mime" } },
#     { "p7r",{ "application/x-pkcs7-certreqresp" } },
#     { "p7s",{ "application/x-pkcs7-signature" } },
#     { "pbm",{ "image/x-portable-bitmap" } },
#     { "pdf",{ "application/pdf" } },
#     { "pfx",{ "application/x-pkcs12" } },
#     { "pgm",{ "image/x-portable-graymap" } },
#     { "pko",{ "application/ynd.ms-pkipko" } },
#     { "pma",{ "application/x-perfmon" } },
#     { "pmc",{ "application/x-perfmon" } },
#     { "pml",{ "application/x-perfmon" } },
#     { "pmr",{ "application/x-perfmon" } },
#     { "pmw",{ "application/x-perfmon" } },
#     { "pnm",{ "image/x-portable-anymap" } },
#     { "pot,",{ "application/vnd.ms-powerpoint" } },
#     { "ppm",{ "image/x-portable-pixmap" } },
#     { "pps",{ "application/vnd.ms-powerpoint" } },
#     { "ppt",{ "application/vnd.ms-powerpoint" } },
#     { "prf",{ "application/pics-rules" } },
#     { "ps",{ "application/postscript" } },
#     { "pub",{ "application/x-mspublisher" } },
#     { "qt",{ "video/quicktime" } },
#     { "ra",{ "audio/x-pn-realaudio" } },
#     { "ram",{ "audio/x-pn-realaudio" } },
#     { "ras",{ "image/x-cmu-raster" } },
#     { "rgb",{ "image/x-rgb" } },
#     { "rmi",{ "audio/mid" } },
#     { "roff",{ "application/x-troff" } },
#     { "rtf",{ "application/rtf" } },
#     { "rtx",{ "text/richtext" } },
#     { "scd",{ "application/x-msschedule" } },
#     { "sct",{ "text/scriptlet" } },
#     { "setpay",{ "application/set-payment-initiation" } },
#     { "setreg",{ "application/set-registration-initiation" } },
#     { "sh",{ "application/x-sh" } },
#     { "shar",{ "application/x-shar" } },
#     { "sit",{ "application/x-stuffit" } },
#     { "snd",{ "audio/basic" } },
#     { "spc",{ "application/x-pkcs7-certificates" } },
#     { "spl",{ "application/futuresplash" } },
#     { "src",{ "application/x-wais-source" } },
#     { "sst",{ "application/vnd.ms-pkicertstore" } },
#     { "stl",{ "application/vnd.ms-pkistl" } },
#     { "stm",{ "text/html" } },
#     { "svg",{ "image/svg+xml" } },
#     { "sv4cpio",{ "application/x-sv4cpio" } },
#     { "sv4crc",{ "application/x-sv4crc" } },
#     { "swf",{ "application/x-shockwave-flash" } },
#     { "t",{ "application/x-troff" } },
#     { "tar",{ "application/x-tar" } },
#     { "tcl",{ "application/x-tcl" } },
#     { "tex",{ "application/x-tex" } },
#     { "texi",{ "application/x-texinfo" } },
#     { "texinfo",{ "application/x-texinfo" } },
#     { "tgz",{ "application/x-compressed" } },
#     { "tif",{ "image/tiff" } },
#     { "tiff",{ "image/tiff" } },
#     { "tr",{ "application/x-troff" } },
#     { "trm",{ "application/x-msterminal" } },
#     { "tsv",{ "text/tab-separated-values" } },
#     { "txt",{ "text/plain" } },
#     { "uls",{ "text/iuls" } },
#     { "ustar",{ "application/x-ustar" } },
#     { "vcf",{ "text/x-vcard" } },
#     { "vrml",{ "x-world/x-vrml" } },
#     { "wav",{ "audio/x-wav" } },
#     { "wcm",{ "application/vnd.ms-works" } },
#     { "wdb",{ "application/vnd.ms-works" } },
#     { "wks",{ "application/vnd.ms-works" } },
#     { "wmf",{ "application/x-msmetafile" } },
#     { "wps",{ "application/vnd.ms-works" } },
#     { "wri",{ "application/x-mswrite" } },
#     { "wrl",{ "x-world/x-vrml" } },
#     { "wrz",{ "x-world/x-vrml" } },
#     { "xaf",{ "x-world/x-vrml" } },
#     { "xbm",{ "image/x-xbitmap" } },
#     { "xla",{ "application/vnd.ms-excel" } },
#     { "xlc",{ "application/vnd.ms-excel" } },
#     { "xlm",{ "application/vnd.ms-excel" } },
#     { "xls",{ "application/vnd.ms-excel" } },
#     { "xlt",{ "application/vnd.ms-excel" } },
#     { "xlw",{ "application/vnd.ms-excel" } },
#     { "xof",{ "x-world/x-vrml" } },
#     { "xpm",{ "image/x-xpixmap" } },
#     { "xwd",{ "image/x-xwindowdump" } },
#     { "xml",{ "application/xml" } },
#     { "z",{ "application/x-compress" } },
#     { "zip",{ "application/zip" } },


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

    def _is_format(self, format_key: str) -> bool:
        """Check if entry is of the given format_key."""
        return bool(libcombine.KnownFormats.isFormat(format_key, self.format))

    def is_sbml(self) -> bool:
        """Check if entry is SBML."""
        return self._is_format("sbml")

    def is_sedml(self) -> bool:
        """Check if entry is SED-ML."""
        return self._is_format("sedml")

    def is_sbgn(self) -> bool:
        """Check if entry is SBGN."""
        return self._is_format("sbgn")


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

    def get_path(self, location: str) -> Path:
        """Get path for given location."""
        # check that entry exists (raises KeyError)
        _ = self.manifest[location]
        return self._tmp_dir / location

    @staticmethod
    def _check_omex_path(omex_path: Path) -> Path:
        """Check if omex path exist, is a file and a COMBINE archive."""
        if isinstance(omex_path, str):
            logger.warning(f"'omex_path' should be 'Path': '{omex_path}'")
            omex_path = Path(omex_path)

        if not omex_path.exists:
            raise ValueError(f"'omex_path' does not exist: '{omex_path}'.")
        if not omex_path.is_file():
            raise ValueError(f"'omex_path' is not a file: '{omex_path}'.")

        return omex_path

    @staticmethod
    def is_omex(omex_path: Path) -> bool:
        """Check if path is an omex archive.

        File must be a zip archive and contain a manifest.xml.
        """
        omex_path = Omex._check_omex_path(omex_path)

        if not zipfile.is_zipfile(str(omex_path)):
            logger.warning(f"Omex path '{omex_path}' is not a zip archive.")
            return False

        with zipfile.ZipFile(omex_path, mode="r") as zf:
            try:
                zf.getinfo("manifest.xml")
                return True
            except KeyError:
                # manifest does not exist in archive
                logger.warning(f"No 'manifest.xml' in '{omex_path}'.")
                return False

    @staticmethod
    def from_omex(omex_path: Path) -> "Omex":
        """Read omex from given path.

        :param omex_path:
        :return: Omex object
        """
        omex_path = Omex._check_omex_path(omex_path)

        # extract archive to tmp directory
        with tempfile.TemporaryDirectory() as tmp_dir:
            with zipfile.ZipFile(omex_path, "r") as zf:
                zf.extractall(tmp_dir)

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
