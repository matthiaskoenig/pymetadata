"""Example of using SBO terms."""

from pymetadata.console import console
from pymetadata.metadata import SBO

sbo_term1 = SBO.SIMPLE_CHEMICAL
sbo_term2 = SBO.PROCESS

for sbo in [sbo_term1, sbo_term2]:
    console.print(sbo)
