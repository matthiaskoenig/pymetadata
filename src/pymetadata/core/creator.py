"""Creator information for models and archives."""


class Creator:
    """A person credited with a model or archive.

    Used in the SBML ModelHistory and in the metadata of other COMBINE formats.

    Attributes:
        familyName: family name of the creator
        givenName: given name of the creator
        email: email address
        organization: affiliation of the creator
        site: url of a personal or institutional website
        orcid: ORCID of the creator, e.g., `0000-0003-1725-179X`

    Example:
        ```python
        creator = Creator(
            familyName="König",
            givenName="Matthias",
            email="konigmatt@googlemail.com",
            organization="Humboldt-University Berlin",
            orcid="0000-0003-1725-179X",
        )
        ```
    """

    def __init__(
        self,
        familyName: str,
        givenName: str,
        email: str,
        organization: str,
        site: str | None = None,
        orcid: str | None = None,
    ):
        """Initialize the creator."""
        self.familyName = familyName
        self.givenName = givenName
        self.email = email
        self.organization = organization
        self.site = site
        self.orcid = orcid

    def __str__(self) -> str:
        """Get the string representation of the creator."""
        return f"{self.familyName} {self.givenName} ({self.email}, {self.organization}, {self.site}, {self.orcid})"

    def __hash__(self) -> int:
        """Get the hash of the creator."""
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        """Check two creators for equality."""
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
