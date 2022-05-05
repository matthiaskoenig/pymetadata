"""Creator information."""
from typing import Optional


class Creator:
    """Creator in ModelHistory and other COMBINE formats."""

    def __init__(
        self,
        familyName: str,
        givenName: str,
        email: str,
        organization: str,
        site: Optional[str] = None,
        orcid: Optional[str] = None,
    ):
        """Initialize Creator."""
        self.familyName = familyName
        self.givenName = givenName
        self.email = email
        self.organization = organization
        self.site = site
        self.orcid = orcid

    def __str__(self) -> str:
        """Get string representation."""
        return f"{self.familyName} {self.givenName} ({self.email}, {self.organization}, {self.site}, {self.orcid})"

    def __hash__(self) -> int:
        """Get hash."""
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        """Check for equality."""
        if not isinstance(other, Creator):
            return NotImplemented

        return (
            self.familyName == other.familyName
            and self.givenName == other.givenName
            and self.email == other.email
            and self.organization == other.organization
            and self.site == other.site
            and self.orcid == other.orcid
        )
