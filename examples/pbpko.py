"""Example of using PBPKO terms."""

from pymetadata.console import console
from pymetadata.ontologies import PBPKO

pbpko_term1 = PBPKO.BODYWEIGHT
pbpko_term2 = PBPKO.WHOLE_BODY_PBPK

for pbpko in [pbpko_term1, pbpko_term2]:
    console.print(pbpko)
