from pymetadata.console import console
from pymetadata.identifiers.miriam import BQB
from pymetadata.core.annotation import RDFAnnotation

for resource in [
    "urn:miriam:chebi:CHEBI%3A33699",
    "CHEBI:33699",
    "chebi/CHEBI:33699",
    "https://identifiers.org/chebi/CHEBI:33699",
    "http://identifiers.org/CHEBI:33699",
]:
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource)
    console.print(a)


for resource in [
    "CHEB:33699",
    "chebi/CHEBI:X33699",
]:
    a = RDFAnnotation(qualifier=BQB.IS, resource=resource)
    console.print(a)
