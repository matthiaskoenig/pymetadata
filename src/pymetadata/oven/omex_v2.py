"""COMBINE archive version 2, draft.

A sketch of the version 2 metadata, not wired into `pymetadata.omex` and not
part of the public API, see `pymetadata.oven`.

See https://docs.google.com/document/d/1-UDgY5lQ6tv4mZILZzol-PvCoAYW8yr2Ydn1OxcHMjM/edit#
"""

from pydantic import BaseModel


class Creator(BaseModel):
    """Creator version 2."""

    name: str
    affiliation: str | None
    orcid: str | None


class Manifest(BaseModel):
    """Manifest version 2."""

    title: str
    description: str
    access_right: str
    access_conditions: str
    license: str
    creators: list[Creator]
    version: str | None
    doi: str | None
    keywords: list[str]
