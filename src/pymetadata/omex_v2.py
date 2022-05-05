"""COMBINE archive version 2.

See https://docs.google.com/document/d/1-UDgY5lQ6tv4mZILZzol-PvCoAYW8yr2Ydn1OxcHMjM/edit#
"""
from typing import List, Optional

from pydantic import BaseModel


class Creator(BaseModel):
    """Creator version 2."""

    name: str
    affiliation: Optional[str]
    orcid: Optional[str]


class Manifest(BaseModel):
    """Manifest version 2."""

    title: str
    description: str
    access_right: str
    access_conditions: str
    license: str
    creators: List[Creator]
    version: Optional[str]
    doi: Optional[str]
    keywords: List[str]
