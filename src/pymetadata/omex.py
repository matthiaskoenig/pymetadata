"""
COMBINE Archive support.

This module provides an abstraction around the COMBINE archive. Common operations
such as archive creation, archive extraction, creating archives from entries or
directories, working with the `manifest.xml` are implemented.

When working with COMBINE archives these wrapper functions should be used.
The current version has no support for metadata manipulation.

Encrypted archives can be opened, but no support for encrypting archives yet.
"""

import os
import pprint
import shutil
import tempfile
import zipfile
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional

import xmltodict
from pydantic import BaseModel, PrivateAttr

from pymetadata import log
from pymetadata.console import console


logger = log.get_logger(__name__)


__all__ = ["EntryFormat", "ManifestEntry", "Manifest", "Omex"]


IDENTIFIERS_PREFIX = "https://identifiers.org/combine.specifications:"
PURL_PREFIX = "https://purl.org/NET/mediatypes/"


class EntryFormat(str, Enum):
    """Enum for common formats."""

    OMEX = IDENTIFIERS_PREFIX + "omex"
    OMEX_MANIFEST = IDENTIFIERS_PREFIX + "omex-manifest"
    OMEX_METADATA = IDENTIFIERS_PREFIX + "omex-metadata"

    SBML = IDENTIFIERS_PREFIX + "sbml"
    SBML_L1V1 = (IDENTIFIERS_PREFIX + "sbml.level-1.version-1",)
    SBML_L1V2 = (IDENTIFIERS_PREFIX + "sbml.level-1.version-2",)
    SBML_L2V1 = IDENTIFIERS_PREFIX + "sbml.level-2.version-1"
    SBML_L2V2 = IDENTIFIERS_PREFIX + "sbml.level-2.version-2"
    SBML_L2V3 = IDENTIFIERS_PREFIX + "sbml.level-2.version-3"
    SBML_L2V4 = IDENTIFIERS_PREFIX + "sbml.level-2.version-4"
    SBML_L2V5 = IDENTIFIERS_PREFIX + "sbml.level-2.version-5"
    SBML_L3V1 = IDENTIFIERS_PREFIX + "sbml.level-3.version-1"
    SBML_L3V2 = IDENTIFIERS_PREFIX + "sbml.level-3.version-2"

    SEDML = IDENTIFIERS_PREFIX + "sed-ml"
    SEDML_L1V1 = IDENTIFIERS_PREFIX + "sed-ml.level-1.version-1"
    SEDML_L1V2 = IDENTIFIERS_PREFIX + "sed-ml.level-1.version-2"
    SEDML_L1V3 = IDENTIFIERS_PREFIX + "sed-ml.level-1.version-3"
    SEDML_L1V4 = IDENTIFIERS_PREFIX + "sed-ml.level-1.version-4"

    BIOPAX = IDENTIFIERS_PREFIX + "biopax"
    CELLML = IDENTIFIERS_PREFIX + "cellml"
    SBGN = IDENTIFIERS_PREFIX + "sbgn"
    SBGN_PD = IDENTIFIERS_PREFIX + "sbgn.pd"

    FROG_JSON_V1 = IDENTIFIERS_PREFIX + "frog-json-version-1"
    FROG_METADATA_V1 = IDENTIFIERS_PREFIX + "frog-metadata-version-1"
    FROG_OBJECTIVE_V1 = IDENTIFIERS_PREFIX + "frog-objective-version-1"
    FROG_FVA_V1 = IDENTIFIERS_PREFIX + "frog-fva-version-1"
    FROG_GENEDELETION_V1 = IDENTIFIERS_PREFIX + "frog-genedeletion-version-1"
    FROG_REACTIONDELETION_V1 = IDENTIFIERS_PREFIX + "frog-reactiondeletion-version-1"

    MARKDOWN = PURL_PREFIX + "text/x-markdown"
    PLAIN = PURL_PREFIX + "text/plain"
    XML = PURL_PREFIX + "application/xml"
    RDF = PURL_PREFIX + "application/xml"
    OWL = PURL_PREFIX + "application/xml"
    SCI = PURL_PREFIX + "application/x-scilab"
    XPP = PURL_PREFIX + "text/plain"

    COPASI = PURL_PREFIX + "application/x-copasi"
    SEDX = PURL_PREFIX + "application/x-sed-ml-archive"
    PNG = PURL_PREFIX + "image/png"
    CSV = PURL_PREFIX + "text/csv"
    H323 = PURL_PREFIX + "text/h323"
    ACX = PURL_PREFIX + "application/internet-property-stream"
    AI = PURL_PREFIX + "application/postscript"
    AIF = PURL_PREFIX + "audio/x-aiff"
    AIFC = PURL_PREFIX + "audio/x-aiff"
    AIFF = PURL_PREFIX + "audio/x-aiff"
    ASF = PURL_PREFIX + "video/x-ms-asf"
    ASR = PURL_PREFIX + "video/x-ms-asf"
    ASX = PURL_PREFIX + "video/x-ms-asf"
    AU = PURL_PREFIX + "audio/basic"
    AVI = PURL_PREFIX + "video/x-msvideo"
    AXS = PURL_PREFIX + "application/olescript"
    BAS = PURL_PREFIX + "text/plain"
    BCPIO = PURL_PREFIX + "application/x-bcpio"
    BIN = PURL_PREFIX + "application/octet-stream"
    BMP = PURL_PREFIX + "image/bmp"
    C = PURL_PREFIX + "text/plain"
    CAT = PURL_PREFIX + "application/vnd.ms-pkiseccat"
    CDF = PURL_PREFIX + "application/x-cdf"
    CER = PURL_PREFIX + "application/x-x509-ca-cert"
    CLP = PURL_PREFIX + "application/x-msclip"
    CMX = PURL_PREFIX + "image/x-cmx"
    COD = PURL_PREFIX + "image/cis-cod"
    CPIO = PURL_PREFIX + "application/x-cpio"
    CRD = PURL_PREFIX + "application/x-mscardfile"
    CRL = PURL_PREFIX + "application/pkix-crl"
    CRT = PURL_PREFIX + "application/x-x509-ca-cert"
    CSH = PURL_PREFIX + "application/x-csh"
    CSS = PURL_PREFIX + "text/css"
    DCR = PURL_PREFIX + "application/x-director"
    DER = PURL_PREFIX + "application/x-x509-ca-cert"
    DIR = PURL_PREFIX + "application/x-director"
    DLL = PURL_PREFIX + "application/x-msdownload"
    DMS = PURL_PREFIX + "application/octet-stream"
    DOC = PURL_PREFIX + "application/msword"
    DOT = PURL_PREFIX + "application/msword"
    DVI = PURL_PREFIX + "application/x-dvi"
    DXR = PURL_PREFIX + "application/x-director"
    EPS = PURL_PREFIX + "application/postscript"
    ETX = PURL_PREFIX + "text/x-setext"
    EVY = PURL_PREFIX + "application/envoy"
    EXE = PURL_PREFIX + "application/octet-stream"
    FIF = PURL_PREFIX + "application/fractals"
    FLR = PURL_PREFIX + "x-world/x-vrml"
    GIF = PURL_PREFIX + "image/gif"
    GTAR = PURL_PREFIX + "application/x-gtar"
    GZ = PURL_PREFIX + "application/x-gzip"
    H = PURL_PREFIX + "text/plain"
    HDF = PURL_PREFIX + "application/x-hdf"
    H5 = PURL_PREFIX + "application/x-hdf"
    HLP = PURL_PREFIX + "application/winhlp"
    HQT = PURL_PREFIX + "application/mac-binhex40"
    HTA = PURL_PREFIX + "application/hta"
    HTC = PURL_PREFIX + "text/x-component"
    HTM = PURL_PREFIX + "text/html"
    HTML = PURL_PREFIX + "text/html"
    HTT = PURL_PREFIX + "text/webviewhtml"
    ICO = PURL_PREFIX + "image/x-icon"
    IEF = PURL_PREFIX + "image/ief"
    III = PURL_PREFIX + "application/x-iphone"
    INS = PURL_PREFIX + "application/x-internet-signup"
    ISP = PURL_PREFIX + "application/x-internet-signup"
    JFIF = PURL_PREFIX + "image/pipeg"
    JPE = PURL_PREFIX + "image/jpeg"
    JPEG = PURL_PREFIX + "image/jpeg"
    JPG = PURL_PREFIX + "image/jpeg"
    JS = PURL_PREFIX + "application/x-javascript"
    LATEX = PURL_PREFIX + "application/x-latex"
    LHA = PURL_PREFIX + "application/octet-stream"
    LSF = PURL_PREFIX + "video/x-la-asf"
    LSX = PURL_PREFIX + "video/x-la-asf"
    LZH = PURL_PREFIX + "application/octet-stream"
    M = PURL_PREFIX + "application/x-matlab"
    MAT = PURL_PREFIX + "application/x-matlab-data"
    M13 = PURL_PREFIX + "application/x-msmediaview"
    M14 = PURL_PREFIX + "application/x-msmediaview"
    M3U = PURL_PREFIX + "audio/x-mpegurl"
    MAN = PURL_PREFIX + "application/x-troff-man"
    MDB = PURL_PREFIX + "application/x-msaccess"
    ME = PURL_PREFIX + "application/x-troff-me"
    MHT = PURL_PREFIX + "message/rfc822"
    MHTML = PURL_PREFIX + "message/rfc822"
    MID = PURL_PREFIX + "audio/mid"
    MNY = PURL_PREFIX + "application/x-msmoney"
    MOV = PURL_PREFIX + "video/quicktime"
    MOVIE = PURL_PREFIX + "video/x-sgi-movie"
    MP2 = PURL_PREFIX + "video/mpeg"
    MP3 = PURL_PREFIX + "audio/mpeg"
    MP4 = PURL_PREFIX + "video/mpeg"
    MPE = PURL_PREFIX + "video/mpeg"
    MPEG = PURL_PREFIX + "video/mpeg"
    MPG = PURL_PREFIX + "video/mpeg"
    MPP = PURL_PREFIX + "application/vnd.ms-project"
    MPV2 = PURL_PREFIX + "video/mpeg"
    MS = PURL_PREFIX + "application/x-troff-ms"
    MVB = PURL_PREFIX + "application/x-msmediaview"
    NWS = PURL_PREFIX + "message/rfc822"
    ODA = PURL_PREFIX + "application/oda"
    P10 = PURL_PREFIX + "application/pkcs10"
    P12 = PURL_PREFIX + "application/x-pkcs12"
    P7B = PURL_PREFIX + "application/x-pkcs7-certificates"
    P7C = PURL_PREFIX + "application/x-pkcs7-mime"
    P7M = PURL_PREFIX + "application/x-pkcs7-mime"
    P7R = PURL_PREFIX + "application/x-pkcs7-certreqresp"
    P7S = PURL_PREFIX + "application/x-pkcs7-signature"
    PBM = PURL_PREFIX + "image/x-portable-bitmap"
    PDF = PURL_PREFIX + "application/pdf"
    PFX = PURL_PREFIX + "application/x-pkcs12"
    PGM = PURL_PREFIX + "image/x-portable-graymap"
    PKO = PURL_PREFIX + "application/ynd.ms-pkipko"
    PMA = PURL_PREFIX + "application/x-perfmon"
    PMC = PURL_PREFIX + "application/x-perfmon"
    PML = PURL_PREFIX + "application/x-perfmon"
    PMR = PURL_PREFIX + "application/x-perfmon"
    PMW = PURL_PREFIX + "application/x-perfmon"
    PNW = PURL_PREFIX + "image/x-portable-anymap"
    POT = PURL_PREFIX + "application/vnd.ms-powerpoint"
    PPM = PURL_PREFIX + "image/x-portable-pixmap"
    PPS = PURL_PREFIX + "application/vnd.ms-powerpoint"
    PPT = PURL_PREFIX + "application/vnd.ms-powerpoint"
    PRF = PURL_PREFIX + "application/pics-rules"
    PS = PURL_PREFIX + "application/postscript"
    PUB = PURL_PREFIX + "application/x-mspublisher"
    QT = PURL_PREFIX + "video/quicktime"
    RA = PURL_PREFIX + "audio/x-pn-realaudio"
    RAM = PURL_PREFIX + "audio/x-pn-realaudio"
    RAS = PURL_PREFIX + "image/x-cmu-raster"
    RGB = PURL_PREFIX + "image/x-rgb"
    RMI = PURL_PREFIX + "audio/mid"
    ROFF = PURL_PREFIX + "application/x-troff"
    RTF = PURL_PREFIX + "application/rtf"
    RTX = PURL_PREFIX + "text/richtext"
    SCD = PURL_PREFIX + "application/x-msschedule"
    SCT = PURL_PREFIX + "text/scriptlet"
    SETPAY = PURL_PREFIX + "application/set-payment-initiation"
    SETREG = PURL_PREFIX + "application/set-registration-initiation"
    SH = PURL_PREFIX + "application/x-sh"
    SHAR = PURL_PREFIX + "application/x-shar"
    SIT = PURL_PREFIX + "application/x-stuffit"
    SND = PURL_PREFIX + "audio/basic"
    SPC = PURL_PREFIX + "application/x-pkcs7-certificates"
    SPL = PURL_PREFIX + "application/futuresplash"
    SRC = PURL_PREFIX + "application/x-wais-source"
    SST = PURL_PREFIX + "application/vnd.ms-pkicertstore"
    STL = PURL_PREFIX + "application/vnd.ms-pkistl"
    STM = PURL_PREFIX + "text/html"
    SVG = PURL_PREFIX + "image/svg+xml"
    SV4CPIO = PURL_PREFIX + "application/x-sv4cpio"
    SV4CRC = PURL_PREFIX + "application/x-sv4crc"
    SWF = PURL_PREFIX + "application/x-shockwave-flash"
    T = PURL_PREFIX + "application/x-troff"
    TAR = PURL_PREFIX + "application/x-tar"
    TCL = PURL_PREFIX + "application/x-tcl"
    TEX = PURL_PREFIX + "application/x-tex"
    TEXI = PURL_PREFIX + "application/x-texinfo"
    TEXINFO = PURL_PREFIX + "application/x-texinfo"
    TGZ = PURL_PREFIX + "application/x-compressed"
    TIF = PURL_PREFIX + "image/tiff"
    TIFF = PURL_PREFIX + "image/tiff"
    TR = PURL_PREFIX + "application/x-troff"
    TRM = PURL_PREFIX + "application/x-msterminal"
    TSV = PURL_PREFIX + "text/tab-separated-values"
    TXT = PURL_PREFIX + "text/plain"
    ULS = PURL_PREFIX + "text/iuls"
    USTAR = PURL_PREFIX + "application/x-ustar"
    VCF = PURL_PREFIX + "text/x-vcard"
    VRML = PURL_PREFIX + "x-world/x-vrml"
    WAV = PURL_PREFIX + "audio/x-wav"
    WCM = PURL_PREFIX + "application/vnd.ms-works"
    WDB = PURL_PREFIX + "application/vnd.ms-works"
    WKS = PURL_PREFIX + "application/vnd.ms-works"
    WMF = PURL_PREFIX + "application/x-msmetafile"
    WPS = PURL_PREFIX + "application/vnd.ms-works"
    WRI = PURL_PREFIX + "application/x-mswrite"
    WRL = PURL_PREFIX + "x-world/x-vrml"
    WRZ = PURL_PREFIX + "x-world/x-vrml"
    XAF = PURL_PREFIX + "x-world/x-vrml"
    XBM = PURL_PREFIX + "image/x-xbitmap"
    XLA = PURL_PREFIX + "application/vnd.ms-excel"
    XLC = PURL_PREFIX + "application/vnd.ms-excel"
    XLM = PURL_PREFIX + "application/vnd.ms-excel"
    XLS = PURL_PREFIX + "application/vnd.ms-excel"
    XLT = PURL_PREFIX + "application/vnd.ms-excel"
    XLW = PURL_PREFIX + "application/vnd.ms-excel"
    XOF = PURL_PREFIX + "x-world/x-vrml"
    XPM = PURL_PREFIX + "image/x-xpixmap"
    XWD = PURL_PREFIX + "image/x-xwindowdump"
    YAML = PURL_PREFIX + "text/yaml"
    Z = PURL_PREFIX + "application/x-compress"
    ZIP = PURL_PREFIX + "application/zip"


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

    class Config:
        """Pydantic configuration."""

        use_enum_values = True

    @staticmethod
    def is_format(format_key: str, format: str) -> bool:
        """Check if entry is of the given format_key."""
        # FIXME: use regular expressions
        if format_key == "sbml":
            return ("identifiers.org/combine.specifications/sbml" in format) or (
                "identifiers.org/combine.specifications:sbml" in format
            )
        if format_key == "sedml":
            return ("identifiers.org/combine.specifications/sed" in format) or (
                "identifiers.org/combine.specifications:sed" in format
            )
        if format_key == "sbgn":
            return ("identifiers.org/combine.specifications/sbgn" in format) or (
                "identifiers.org/combine.specifications:sbgn" in format
            )

        if hasattr(EntryFormat, format_key):
            format_reference = str(getattr(EntryFormat, format_key.upper()))
            return format_reference == format

        return False

    def is_sbml(self) -> bool:
        """Check if entry is SBML."""
        return ManifestEntry.is_format("sbml", self.format)

    def is_sedml(self) -> bool:
        """Check if entry is SED-ML."""
        return ManifestEntry.is_format("sedml", self.format)

    def is_sbgn(self) -> bool:
        """Check if entry is SBGN."""
        return ManifestEntry.is_format("sbgn", self.format)


class Manifest(BaseModel):
    """COMBINE archive manifest.

    A manifest is a list of ManifestEntries.
    """

    _entries_dict: Dict[str, ManifestEntry] = PrivateAttr()
    entries: List[ManifestEntry] = [
        ManifestEntry(location=".", format=EntryFormat.OMEX),
        ManifestEntry(
            location="./manifest.xml",
            format=EntryFormat.OMEX_MANIFEST,
        ),
    ]

    def __init__(self, **data) -> None:  # type: ignore
        """Initialize Manifest."""
        super().__init__(**data)
        for e in self.entries:
            if not e.location.startswith("."):
                logger.warning(
                    f"Relative location paths must start with './', but '{e.location}'."
                )
                e.location = f"./{e.location}"
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
                master_token = ' master="false"'
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
        entry.location = self._check_and_normalize_location(entry.location)
        self.entries.append(entry)
        self._entries_dict[entry.location] = entry

    def remove_entry_for_location(self, location: str) -> Optional[ManifestEntry]:
        """Remove entry for given location."""
        location = self._check_and_normalize_location(location)

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

    @staticmethod
    def _check_and_normalize_location(location: str) -> str:
        """Add relative prefix and check location."""

        if location.startswith("/"):
            raise ValueError(
                f"Locations must be relative paths in COMBINE archive, but location is "
                f"'{location}'."
            )

        # add prefix
        if not location.startswith("./") and location != ".":
            location = f"./{location}"
        return location


class Omex:
    """Combine archive class."""

    def __init__(self) -> None:
        """Create COMBINE Archive Version 1."""
        self.manifest: Manifest = Manifest()
        self._tmp_dir: Path = Path(tempfile.mkdtemp())

    def __exit__(self, exc_type, exc_value, traceback):  # type: ignore
        """Cleanup on exit."""
        shutil.rmtree(self._tmp_dir)

    def __str__(self) -> str:
        """Get contents of archive string."""
        return pprint.pformat(self.manifest.entries, indent=4, compact=True)

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

        if not omex_path.exists():
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
    def from_omex(omex_path: Path, password: Optional[bytes] = None) -> "Omex":
        """Read omex from given path.

        :param omex_path: path to omex archive
        :param password: password for encryption
        :return: Omex object
        """
        omex_path = Omex._check_omex_path(omex_path)

        # extract archive to tmp directory
        with tempfile.TemporaryDirectory() as tmp_dir:
            with zipfile.ZipFile(omex_path, "r") as zf:
                # Figure out algorithm:
                for info in zf.infolist():
                    if info.compress_type not in {
                        zipfile.ZIP_DEFLATED,
                        zipfile.ZIP_STORED,
                    }:
                        logger.warning(f"Unsupported compression for: '{info}'")
                # extract all files
                zf.extractall(tmp_dir, pwd=password)

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

        if not directory.exists():
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
            logger.error(
                f"No 'manifest.xml' in directory: '{directory}'. Trying "
                f"to create manifest.xml."
            )

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
                            f"Entry with location missing in manifest.xml: '{location}'"
                        )

                    format = Omex.guess_format(Path(file_path))
                    master = False
                    if format and ManifestEntry.is_format(
                        format_key="sedml", format=format
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
        The entry is copied when getting added, i.e., changes to the location
        after adding an entry will not have any effect on the content in the
        archive!
        """
        if isinstance(entry_path, str):
            logger.warning(f"'entry_path' should be 'Path': '{entry_path}'")
            entry_path = Path(entry_path)

        if not entry_path.exists():
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

    def to_omex(
        self,
        omex_path: Path,
        password: Optional[str] = None,
        compression: int = zipfile.ZIP_DEFLATED,
        compresslevel: int = 9,
    ) -> None:
        """Write omex to path.

        By definition OMEX files should be zip deflated.

        The `compresslevel` parameter controls the compression level to use when
        writing files to the archive. When using `ZIP_STORED` or `ZIP_LZMA` it has no
        effect. When using `ZIP_DEFLATED` integers 0 through 9 are accepted
        (see zlib for more information). When using ZIP_BZIP2 integers 1 through 9
        are accepted (see bz2 for more information). The larger the value the better
        te compression

        :param omex_path:
        :param compression: compression algorithm
        :param compresslevel: level of compression
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
            with zipfile.ZipFile(
                omex_path,
                mode="w",
                compression=compression,
                compresslevel=compresslevel,
            ) as zf:
                for e in self.manifest.entries:
                    if e.location != ".":
                        f = Path(tmp_dir) / e.location
                        zf.write(filename=str(f), arcname=e.location)

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

    def entries_by_format(self, format_key: str) -> List[ManifestEntry]:
        """Get entries with given format in the archive."""

        entries: List[ManifestEntry] = []
        for entry in self.manifest.entries:
            if ManifestEntry.is_format(format_key, entry.format):
                entries.append(entry)

        return entries

    @staticmethod
    def lookup_format(format_key: str) -> str:
        """Lookup format by format_key."""
        if hasattr(EntryFormat, format_key.upper()):
            return str(getattr(EntryFormat, format_key.upper()).value)

        logger.error(f"Unknown format_key: {format_key}")
        return PURL_PREFIX + "application/x.unknown"

    @staticmethod
    def guess_format(path: Path) -> str:
        """Guess format string for given file.

        If string cannot be resolved '' is returned.
        """

        extension = path.suffix[1:] if path.suffix else ""
        if extension == "xml":
            with open(path, "r") as f_in:
                try:
                    text = f_in.read(256)
                    if "<sbml" in text:
                        return Omex.lookup_format("sbml")
                    if "<sedML" in text:
                        return Omex.lookup_format("sedml")
                    if "<cell" in text:
                        return Omex.lookup_format("cellml")
                    if "<COPASI" in text:
                        return Omex.lookup_format("copasi")
                except UnicodeDecodeError as err:
                    # handle incorrect encodings
                    logger.error(
                        f"UnicodeDecodeError in '{path}', "
                        f"incorrect file encoding: '{err}'"
                    )

        return Omex.lookup_format(extension)
