"""COMBINE archive (OMEX) support.

A COMBINE archive is a single file which bundles everything belonging to a
modeling project: models (SBML, CellML), simulation experiments (SED-ML), data,
figures and documentation. It is a ZIP container with a `manifest.xml` at its
root listing every file together with its format, given as an identifiers.org
URI rather than guessed from the file suffix.

This module provides three classes:

- `Omex`: the archive; reading, writing and access to its files
- `Manifest`: the entries of the archive, i.e., the `manifest.xml`
- `ManifestEntry`: a single file with `location`, `format` and `master`

Example:
    Read an existing archive and list the SBML models it contains:

    ```python
    from pathlib import Path
    from pymetadata.omex import Omex

    omex = Omex.from_omex(Path("archive.omex"))
    for entry in omex.entries_by_format("sbml"):
        print(entry.location, omex.get_path(entry.location))
    ```

    Create an archive from single files:

    ```python
    from pymetadata.omex import EntryFormat, ManifestEntry, Omex

    omex = Omex()
    omex.add_entry(
        entry_path=Path("model.xml"),
        entry=ManifestEntry(
            location="./model.xml", format=EntryFormat.SBML_L3V2, master=True
        ),
    )
    omex.to_omex(Path("archive.omex"))
    ```

Encrypted archives can be read by passing a password; writing encrypted archives
is not supported. Manipulation of OMEX metadata is not supported.

References:
    Bergmann FT, Adams R, Moodie S, Cooper J, Glont M, Golebiewski M, Hucka M,
    Laibe C, Miller AK, Nickerson DP, Olivier BG, Rodriguez N, Sauro HM,
    Scharm M, Soiland-Reyes S, Waltemath D, Yvon F, Le Novere N.
    COMBINE archive and OMEX format: one file to share all information to
    reproduce a modeling project. BMC Bioinformatics. 2014;15(1):369.
    https://doi.org/10.1186/s12859-014-0369-z

    Bergmann FT, Rodriguez N, Le Novere N. COMBINE Archive Specification
    Version 1. J Integr Bioinform. 2015;12(2):261.
    https://doi.org/10.2390/biecoll-jib-2015-261
"""

import logging
import os
import pprint
import shutil
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from enum import Enum
from pathlib import Path
from types import TracebackType
from typing import Any

import requests
from pydantic import BaseModel, PrivateAttr

logger = logging.getLogger(__name__)


__all__ = ["EntryFormat", "Manifest", "ManifestEntry", "Omex"]


IDENTIFIERS_PREFIX = "http://identifiers.org/combine.specifications/"
PURL_PREFIX = "https://purl.org/NET/mediatypes/"


class EntryFormat(str, Enum):
    """Format URIs used in the `manifest.xml`.

    COMBINE specifications (SBML, SED-ML, CellML, SBGN, BioPAX, OMEX metadata,
    FROG results) are identified by `http://identifiers.org/combine.specifications/*`
    URIs, all other files by their media type via `https://purl.org/NET/mediatypes/*`.
    Where a specification is versioned, both the generic and the level and
    version specific term exist, e.g., `SBML` and `SBML_L3V2`.
    """

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
    SEDX = PURL_PREFIX + "application/x-sed-ml-archive"

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
    COPASI = PURL_PREFIX + "application/x-copasi"
    CPIO = PURL_PREFIX + "application/x-cpio"
    CPS = PURL_PREFIX + "application/x-copasi"
    CRD = PURL_PREFIX + "application/x-mscardfile"
    CRL = PURL_PREFIX + "application/pkix-crl"
    CRT = PURL_PREFIX + "application/x-x509-ca-cert"
    CSH = PURL_PREFIX + "application/x-csh"
    CSS = PURL_PREFIX + "text/css"
    CSV = PURL_PREFIX + "text/csv"
    DCR = PURL_PREFIX + "application/x-director"
    DER = PURL_PREFIX + "application/x-x509-ca-cert"
    DIR = PURL_PREFIX + "application/x-director"
    DLL = PURL_PREFIX + "application/x-msdownload"
    DMS = PURL_PREFIX + "application/octet-stream"
    DOC = PURL_PREFIX + "application/msword"
    DOCKERFILE = PURL_PREFIX + "text/x-dockerfile"
    DOCX = PURL_PREFIX + "application/msword"
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
    ONNX = PURL_PREFIX + "application/onnx"
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
    PKL = PURL_PREFIX + "application/octet-stream"
    PKO = PURL_PREFIX + "application/ynd.ms-pkipko"
    PMA = PURL_PREFIX + "application/x-perfmon"
    PMC = PURL_PREFIX + "application/x-perfmon"
    PML = PURL_PREFIX + "application/x-perfmon"
    PMR = PURL_PREFIX + "application/x-perfmon"
    PMW = PURL_PREFIX + "application/x-perfmon"
    PNG = PURL_PREFIX + "image/png"
    PNW = PURL_PREFIX + "image/x-portable-anymap"
    POT = PURL_PREFIX + "application/vnd.ms-powerpoint"
    PPM = PURL_PREFIX + "image/x-portable-pixmap"
    PPS = PURL_PREFIX + "application/vnd.ms-powerpoint"
    PPT = PURL_PREFIX + "application/vnd.ms-powerpoint"
    PRF = PURL_PREFIX + "application/pics-rules"
    PS = PURL_PREFIX + "application/postscript"
    PUB = PURL_PREFIX + "application/x-mspublisher"
    PY = PURL_PREFIX + "application/x-python"
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
    VCML = PURL_PREFIX + "application/x-vcell"
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
    XLSX = PURL_PREFIX + "application/vnd.ms-excel"
    XLT = PURL_PREFIX + "application/vnd.ms-excel"
    XLW = PURL_PREFIX + "application/vnd.ms-excel"
    XOF = PURL_PREFIX + "x-world/x-vrml"
    XPM = PURL_PREFIX + "image/x-xpixmap"
    XWD = PURL_PREFIX + "image/x-xwindowdump"
    YAML = PURL_PREFIX + "text/yaml"
    Z = PURL_PREFIX + "application/x-compress"
    ZIP = PURL_PREFIX + "application/zip"


class ManifestEntry(BaseModel):
    """A single file of the archive, as listed in the `manifest.xml`.

    Attributes:
        location: location of the file in the archive, relative and starting
            with `./`, e.g., `./models/model.xml`
        format: format URI of the file, see `EntryFormat`
        master: marks the entry a tool should open first, e.g., the SED-ML file
            of a simulation study

    Example:
        ```python
        entry = ManifestEntry(
            location="./model.xml", format=EntryFormat.SBML_L3V2, master=True
        )
        ```
    """

    location: str
    format: str
    master: bool = False

    # pydantic configuration
    model_config = {
        "use_enum_values": True,
    }

    @staticmethod
    def is_format(format_key: str, format: str) -> bool:
        """Check if a format URI matches a format key.

        Args:
            format_key: `sbml`, `sedml` or `sbgn`, which match all level and
                version variants, or the name of an `EntryFormat`
            format: format URI to check

        Returns:
            True if the format matches the key.
        """
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
    """Content of the `manifest.xml`, i.e., the entries of an archive.

    The manifest behaves like a mapping keyed by location and always contains
    the two entries required by the specification: the archive itself (`.`) and
    the manifest (`./manifest.xml`).

    Attributes:
        entries: the manifest entries

    Example:
        ```python
        print(len(omex.manifest))
        print("./model.xml" in omex.manifest)
        entry = omex.manifest["./model.xml"]
        ```
    """

    _entries_dict: dict[str, ManifestEntry] = PrivateAttr()
    entries: list[ManifestEntry] = [
        ManifestEntry(location=".", format=EntryFormat.OMEX),
        ManifestEntry(
            location="./manifest.xml",
            format=EntryFormat.OMEX_MANIFEST,
        ),
    ]

    def __init__(self, **data: Any) -> None:
        """Initialize Manifest."""
        super().__init__(**data)
        for e in self.entries:
            if not e.location.startswith("."):
                logger.warning(
                    "Relative location paths must start with './', but '%s'.",
                    e.location,
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
        """Read a manifest from a `manifest.xml` file.

        Args:
            manifest_path: path of the `manifest.xml`

        Returns:
            Manifest with the entries listed in the file.
        """
        tree = ET.parse(manifest_path)
        # `{*}` matches the manifest namespace and a missing namespace
        entries = [
            dict(content.attrib) for content in tree.getroot().findall("{*}content")
        ]
        return Manifest(entries=entries)

    def to_manifest_xml(self) -> str:
        """Serialize the manifest to `manifest.xml` content.

        Returns:
            The XML of the manifest as a string.
        """

        def content_line(e: ManifestEntry) -> str:
            master_token = ' master="true"' if e.master else ' master="false"'
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
        """Write the manifest to a `manifest.xml` file.

        Args:
            manifest_path: path of the file to write
        """
        with open(manifest_path, "w") as f_manifest:
            xml = self.to_manifest_xml()
            f_manifest.write(xml)

    def add_entry(self, entry: ManifestEntry) -> None:
        """Add an entry to the manifest.

        The location is normalized to a relative path starting with `./`.
        Duplicated locations are not checked, use `Omex.add_entry` to add
        a file together with its entry.

        Args:
            entry: entry to add
        """
        entry.location = self._check_and_normalize_location(entry.location)
        self.entries.append(entry)
        self._entries_dict[entry.location] = entry

    def remove_entry_for_location(self, location: str) -> ManifestEntry | None:
        """Remove entry for given location."""
        location = self._check_and_normalize_location(location)

        if location in [".", "./manifest.xml"]:
            logger.error(
                "Core location cannot be removed from manifest: '%s'.", location
            )
            return None
        if location not in self:
            logger.error("The location '%s' does not exist in manifest.", location)
            return None
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
    """COMBINE archive (OMEX), version 1.

    The content of the archive is kept in a temporary directory, `manifest`
    holds the corresponding entries. Use the `from_*` constructors to read an
    archive and the `to_*` methods to write one:

    | read | write |
    | --- | --- |
    | `Omex.from_omex` from an omex file | `Omex.to_omex` to an omex file |
    | `Omex.from_url` from a url | `Omex.to_directory` to a directory |
    | `Omex.from_directory` from a directory | |

    An empty archive is filled with `Omex.add_entry`.

    Attributes:
        manifest: entries of the archive, i.e., the content of the `manifest.xml`

    Example:
        Using the archive as a context manager removes the temporary
        directory when the block is left:

        ```python
        with Omex.from_omex(Path("archive.omex")) as omex:
            print(omex)
        ```
    """

    def __init__(self) -> None:
        """Create an empty COMBINE archive."""
        self.manifest: Manifest = Manifest()
        self._tmp_dir: Path = Path(tempfile.mkdtemp())

    def __enter__(self) -> "Omex":
        """Enter the context manager."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Remove the temporary directory with the archive content."""
        shutil.rmtree(self._tmp_dir, ignore_errors=True)

    def __str__(self) -> str:
        """Get contents of archive string."""
        return pprint.pformat(self.manifest.entries, indent=4, compact=True)

    def get_path(self, location: str) -> Path:
        """Get the path of an entry in the extracted archive.

        Args:
            location: location of the entry, e.g., `./model.xml`

        Returns:
            Path of the file in the temporary directory of the archive, which
            can be passed on to a reader such as libsbml.

        Raises:
            KeyError: if no entry exists for the location
        """
        # check that entry exists (raises KeyError)
        _ = self.manifest[location]
        return self._tmp_dir / location

    @staticmethod
    def _check_omex_path(omex_path: Path) -> Path:
        """Check if omex path exist, is a file and a COMBINE archive."""
        if isinstance(omex_path, str):
            logger.warning("'omex_path' should be 'Path': '%s'", omex_path)
            omex_path = Path(omex_path)

        if not omex_path.exists():
            raise ValueError(f"'omex_path' does not exist: '{omex_path}'.")
        if not omex_path.is_file():
            raise ValueError(f"'omex_path' is not a file: '{omex_path}'.")

        return omex_path

    @staticmethod
    def is_omex(omex_path: Path) -> bool:
        """Check if the path is a COMBINE archive.

        The file must be a zip archive containing a `manifest.xml`.

        Args:
            omex_path: path to check

        Returns:
            True if the path is a COMBINE archive.

        Raises:
            ValueError: if the path does not exist or is not a file
        """
        omex_path = Omex._check_omex_path(omex_path)

        if not zipfile.is_zipfile(str(omex_path)):
            logger.warning("Omex path '%s' is not a zip archive.", omex_path)
            return False

        with zipfile.ZipFile(omex_path, mode="r") as zf:
            try:
                zf.getinfo("manifest.xml")
                return True
            except KeyError:
                # manifest does not exist in archive
                logger.warning("No 'manifest.xml' in '%s'.", omex_path)
                return False

    @staticmethod
    def from_omex(omex_path: Path, password: bytes | None = None) -> "Omex":
        """Read a COMBINE archive from a path.

        The archive is extracted into a temporary directory; the entries are
        taken from the `manifest.xml` of the archive.

        Args:
            omex_path: path of the omex file
            password: password of an encrypted archive

        Returns:
            Omex with the content of the archive.

        Raises:
            ValueError: if the path does not exist or is not a file

        Example:
            ```python
            omex = Omex.from_omex(Path("archive.omex"))
            ```
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
                        logger.warning("Unsupported compression for: '%s'", info)
                # extract all files
                zf.extractall(tmp_dir, pwd=password)

            return Omex.from_directory(Path(tmp_dir))

    @staticmethod
    def from_url(omex_url: str, password: bytes | None = None) -> "Omex":
        """Read a COMBINE archive from a url.

        The archive is downloaded to a temporary file and read from there.

        Args:
            omex_url: url of the omex file
            password: password of an encrypted archive

        Returns:
            Omex with the content of the archive.

        Raises:
            requests.HTTPError: if the archive could not be downloaded

        Example:
            ```python
            omex = Omex.from_url(
                "https://github.com/matthiaskoenig/canagliflozin-model/"
                "releases/download/0.7.0/canagliflozin_model.omex"
            )
            ```
        """
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            r = requests.get(omex_url)
            r.raise_for_status()
            tmp.write(r.content)
            tmp_path = Path(tmp.name)

        return Omex.from_omex(tmp_path, password=password)

    @classmethod
    def from_directory(cls, directory: Path) -> "Omex":
        """Create a COMBINE archive from a directory.

        If the directory contains a `manifest.xml`, the entries listed there are
        reused. The format of every other file is inferred with
        `Omex.guess_format`; SED-ML files added this way get `master=True`,
        as they are the entry point of a simulation study.

        Args:
            directory: directory with the content of the archive

        Returns:
            Omex with one entry per file in the directory.

        Raises:
            ValueError: if the directory does not exist or is not a directory

        Example:
            ```python
            omex = Omex.from_directory(Path("./study"))
            omex.to_omex(Path("study.omex"))
            ```
        """
        if isinstance(directory, str):
            logger.warning("'directory' should be 'Path': '%s'", directory)
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
        manifest: Manifest | None = None
        if manifest_path.exists():
            manifest = Manifest.from_manifest(manifest_path)
        else:
            logger.error(
                "No 'manifest.xml' in directory: '%s'. Trying to create manifest.xml.",
                directory,
            )

        # new archive
        omex = Omex()

        # iterate over all locations and add entry
        for root, _dirs, files in os.walk(str(directory)):
            for file in files:
                file_path = os.path.join(root, file)
                location = f"./{os.path.relpath(file_path, directory)}"
                # bugfix for windows paths
                location = location.replace("\\", "/")
                if location == "./manifest.xml":
                    # manifest is created from the internal manifest entries
                    continue

                logger.debug("'%s' -> '%s'", file_path, location)
                entry: ManifestEntry
                if manifest and location in manifest:
                    # use entry from existing manifest
                    entry = manifest[location]
                else:
                    if manifest and location not in manifest:
                        logger.warning(
                            "Entry with location missing in manifest.xml: '%s'",
                            location,
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
        """Add a file to the archive.

        The file is copied into the archive, i.e., later changes to the source
        file do not affect the content of the archive. Adding a second entry for
        an existing location replaces the first one and logs a warning.

        Args:
            entry_path: path of the file to add
            entry: manifest entry describing location, format and master flag

        Raises:
            ValueError: if `entry_path` does not exist or is not a file

        Example:
            ```python
            omex.add_entry(
                entry_path=Path("model.xml"),
                entry=ManifestEntry(
                    location="./model.xml",
                    format=EntryFormat.SBML_L3V2,
                    master=True,
                ),
            )
            ```
        """
        if isinstance(entry_path, str):
            logger.warning("'entry_path' should be 'Path': '%s'", entry_path)
            entry_path = Path(entry_path)

        if not entry_path.exists():
            msg = f"'entry_path' does not exist: '{entry_path}'."
            logger.error(msg)
            raise ValueError(msg)

        if not entry_path.is_file():
            raise ValueError(f"'entry_path' is not a file: '{entry_path}'.")

        if entry.location in self.manifest:
            logger.warning(
                "Location already exists and is overwritten: '%s'.", entry.location
            )
            self.manifest.remove_entry_for_location(entry.location)

        # copy path
        destination = self._tmp_dir / entry.location
        if not destination.parent.exists():
            destination.parent.mkdir(parents=True)
        shutil.copy2(src=str(entry_path), dst=str(destination))

        # add entry
        self.manifest.add_entry(entry)

    def remove_entry_for_location(self, location: str) -> ManifestEntry | None:
        """Remove an entry and the corresponding file from the archive.

        Args:
            location: location of the entry, e.g., `./model.xml`

        Returns:
            The removed entry, or None if no entry exists for the location.
        """
        entry = self.manifest.remove_entry_for_location(location)
        if entry:
            destination = self._tmp_dir / entry.location
            os.remove(destination)
        return entry

    def to_omex(
        self,
        omex_path: Path,
        password: str | None = None,
        compression: int = zipfile.ZIP_DEFLATED,
        compresslevel: int = 9,
    ) -> None:
        """Write the archive to an omex file.

        The `manifest.xml` is generated from the entries of the archive. By
        definition OMEX files are zip deflated.

        Args:
            omex_path: path of the omex file to write
            password: unused, encrypted archives cannot be written yet
            compression: zipfile compression algorithm
            compresslevel: level of compression. Has no effect for `ZIP_STORED`
                and `ZIP_LZMA`; 0-9 for `ZIP_DEFLATED` (see zlib) and 1-9 for
                `ZIP_BZIP2` (see bz2). Larger values compress better.

        Example:
            ```python
            omex.to_omex(Path("archive.omex"))
            ```
        """
        if isinstance(omex_path, str):
            logger.warning("'omex_path' should be 'Path': '%s'", omex_path)
            omex_path = Path(omex_path)

        if omex_path.exists():
            logger.warning("Existing omex is overwritten: '%s'", omex_path)

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
        """Extract the archive to a directory.

        The `manifest.xml` is written next to the files, so the result can be
        read back with `Omex.from_directory`.

        Args:
            output_dir: directory to write to, created if it does not exist

        Example:
            ```python
            omex.to_directory(Path("./unpacked"))
            ```
        """
        if isinstance(output_dir, str):
            logger.warning("'output_dir' should be 'Path': '%s'", output_dir)
            output_dir = Path(output_dir)

        if output_dir and not output_dir.exists():
            logger.warning("Creating working directory: %s", output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)

        # iterate over all locations and copy to destination
        for entry in self.manifest.entries:
            if entry.location in [".", "./manifest.xml"]:
                continue
            src = self._tmp_dir / entry.location
            destination = output_dir / entry.location
            destination.parent.mkdir(parents=True, exist_ok=True)
            logger.debug("'%s' -> '%s", src, destination)
            shutil.copy2(src=str(src), dst=str(destination))

        # write manifest.xml
        self.manifest.to_manifest(manifest_path=output_dir / "manifest.xml")

    def entries_by_format(self, format_key: str) -> list[ManifestEntry]:
        """Get all entries of a given format.

        Args:
            format_key: `sbml`, `sedml` or `sbgn`, which match all level and
                version variants, or the name of an `EntryFormat`

        Returns:
            List of matching entries, empty if the archive contains none.

        Example:
            ```python
            for entry in omex.entries_by_format("sbml"):
                print(entry.location)
            ```
        """
        entries: list[ManifestEntry] = []
        for entry in self.manifest.entries:
            if ManifestEntry.is_format(format_key, entry.format):
                entries.append(entry)

        return entries

    @staticmethod
    def lookup_format(format_key: str) -> str:
        """Look up the format URI for a format key.

        Args:
            format_key: name of an `EntryFormat`, e.g., `sbml` or `csv`

        Returns:
            The format URI, or the URI for an unknown media type if the key
            cannot be resolved.
        """
        if hasattr(EntryFormat, format_key.upper()):
            return str(getattr(EntryFormat, format_key.upper()).value)

        logger.error("Unknown format_key: %s", format_key)
        return PURL_PREFIX + "application/x.unknown"

    @staticmethod
    def guess_format(path: Path) -> str:
        """Guess the format URI of a file.

        The start of `.xml` files is inspected to tell SBML, SED-ML, CellML and
        COPASI apart; for every other file the suffix decides.

        Args:
            path: path of the file

        Returns:
            The format URI, or the URI for an unknown media type if the format
            cannot be determined.
        """
        extension = path.suffix[1:] if path.suffix else ""
        if extension == "xml":
            with open(path) as f_in:
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
                        "UnicodeDecodeError in '%s', incorrect file encoding: '%s'",
                        path,
                        err,
                    )

        return Omex.lookup_format(extension)
