# Annotations

A model element on its own carries no meaning a machine can use. A species named `glc` could be glucose, a glucose transporter or a parameter someone abbreviated. [MIRIAM](https://identifiers.org/) annotations solve this by attaching two things to an element:

- a **qualifier** saying *how* the element relates to something else, e.g., "is", "is part of", "is version of"
- a **resource** pointing at a database entry, e.g., [CHEBI:17234](https://identifiers.org/CHEBI:17234)

Together they form a statement: *this species **is** the chemical entity CHEBI:17234*. `pymetadata` provides the qualifiers, parses resources written in any of the common notations, normalizes them, and validates them against the identifiers.org registry.

## Qualifiers

Biological qualifiers (`BQB`) relate an element to a biological entity, model qualifiers (`BQM`) describe the model itself:

```python
from pymetadata.core.miriam import BQB, BQM

BQB.IS  # the element is the annotated entity
BQB.IS_VERSION_OF  # the element is a version of the entity
BQB.IS_PART_OF  # the element is part of the entity
BQB.HAS_TAXON  # the entity occurs in the given taxon
BQM.IS_DESCRIBED_BY  # the model is described by the resource, e.g., a publication
```

Choosing the right qualifier matters: `BQB.IS` on a species that is only *one form* of a compound is a stronger claim than the model supports, which is what `BQB.IS_VERSION_OF` is for.

## Resources

`RDFAnnotation` accepts the notations found in the wild and reduces them to a `collection` and a `term`:

```python
from pymetadata.core.annotation import RDFAnnotation
from pymetadata.core.miriam import BQB

for resource in [
    "CHEBI:33699",  # compact identifier
    "chebi/CHEBI:33699",  # collection and term
    "https://identifiers.org/CHEBI:33699",  # identifiers.org URL
    "http://identifiers.org/chebi/CHEBI:33699",  # legacy identifiers.org URL
    "urn:miriam:chebi:CHEBI%3A33699",  # deprecated MIRIAM URN
]:
    annotation = RDFAnnotation(qualifier=BQB.IS, resource=resource)
    print(annotation.resource_normalized)
# https://identifiers.org/CHEBI:33699
```

All five spellings normalize to the same compact identifier. Arbitrary URLs are also valid resources; they are kept as they are, because there is no registry entry to normalize them against:

```python
RDFAnnotation(qualifier=BQB.IS, resource="https://en.wikipedia.org/wiki/Cytosol")
```

`resource_normalized` returns `https://identifiers.org/<prefix>:<accession>`. For namespaces which embed their prefix in the identifier (GO, CHEBI, SBO, BTO) the prefix is already part of the term and is not added a second time.

## Validation

Validation answers two questions: is the qualifier a real MIRIAM qualifier, and does the term match the pattern the identifiers.org registry defines for its collection?

```python
annotation = RDFAnnotation(qualifier=BQB.IS, resource="chebi/CHEBI:33699")
annotation.validate()  # qualifier and term
annotation.check_miriam_term()  # term against the registry pattern only
```

A term such as `chebi/CHEBI:X33699` fails, because the CHEBI pattern is `^CHEBI:\d+$`. The registry is downloaded once and cached, see [Installation](installation.md#cache).

## Resolving additional information

`RDFAnnotationData` takes an annotation and resolves what the identifier actually refers to.

Constructing it resolves the cross references: for every provider the identifiers.org registry lists for the collection, the provider's URL pattern is filled in with the term, giving one `CrossReference` per provider.

```python
from pymetadata.core.annotation import RDFAnnotation, RDFAnnotationData
from pymetadata.core.miriam import BQB

annotation = RDFAnnotation(qualifier=BQB.IS, resource="chebi/CHEBI:33699")
data = RDFAnnotationData(annotation)
print(data.url)  # url of the first provider
print(data.xrefs)  # one entry per identifiers.org provider
```

`query_ols()` then asks the [Ontology Lookup Service](https://www.ebi.ac.uk/ols4) for the term itself and fills in label, description and synonyms. Note that it also replaces `xrefs` with the cross references reported by OLS, which can be empty for a given term:

```python
data.query_ols()

print(data.label)  # messenger RNA
print(data.description)  # An RNA molecule that transfers the coding information ...
print(data.synonyms)  # mRNA, ...
```

Both steps require network access. Responses are cached on disk by default, so repeated terms are not queried again; see [Cache](installation.md#cache).

## Ontology terms { #ontology-terms }

Ontology terms are usually passed around as strings, which means typos surface at runtime or not at all, and nothing tells you what a term means. `pymetadata` ships three ontologies as python classes generated from the ontology releases themselves:

| enum | ontology | terms |
| --- | --- | --- |
| `SBO` | Systems Biology Ontology | roles of model components |
| `KISAO` | Kinetic Simulation Algorithm Ontology | simulation algorithms and their parameters |
| `PBPKO` | PBPK Ontology | physiologically based pharmacokinetic modeling |

Every term is available under both its identifier and its name:

```python
from pymetadata.ontologies import SBO, PBPKO

SBO.SBO_0000247  # by id
SBO.SIMPLE_CHEMICAL  # by name
PBPKO.BODYWEIGHT

SBO.get_name(SBO.SIMPLE_CHEMICAL)
# 'simple chemical'
```

`validate` accepts both the underscore and the colon notation and returns the enum member, which is the convenient way to accept terms from user input or from a file:

```python
SBO.validate("SBO:0000247")  # SBO.SBO_0000247
SBO.validate("SBO_0000247")  # SBO.SBO_0000247
SBO.validate("SBO_9999999")  # raises AttributeError, the term does not exist
```

### What a term knows { #term-information }

A term is the identifier, i.e., a `str`, and carries what the ontology release says about it. This is the information which otherwise has to be looked up in [OLS](https://www.ebi.ac.uk/ols4), and it is available offline. Since every term is a documented attribute of its ontology, an editor completes `SBO.` and shows the definition of the term it suggests:

```python
term = SBO.SIMPLE_CHEMICAL

term.value  # 'SBO_0000247', the enum is a str subclass
term.label  # 'simple chemical'
term.definition  # 'Simple, non-repetitive chemical entity.'
term.synonyms  # ()
term.deprecated  # False, the term is not obsolete
term.curie  # 'SBO:0000247'
term.url  # 'https://identifiers.org/SBO:0000247'

repr(term)
# <SBO.SBO_0000247: 'simple chemical'>
```

`get_term` resolves a term given as a string, and the ontology behaves like the enum it replaces, i.e., it can be iterated, asked for its length and indexed:

```python
from pymetadata.ontologies import KISAO

KISAO.get_term("KISAO:0000019").synonyms
# ('VODE', 'VODEPK', 'code value ordinary differential equation solver')

len(KISAO)  # number of terms
KISAO["KISAO_0000019"]  # lookup by identifier
"KISAO:0000019" in KISAO  # True
[term for term in KISAO if term.deprecated]
```

A term stays a string, i.e., `SBO.SIMPLE_CHEMICAL == "SBO_0000247"` is true and serializing a term gives the identifier, so terms can be passed wherever the identifier is expected. The name in the ontology is `label`, `name` is the identifier.

The ontologies are generated with the internal `pymetadata.ontologies._ontology_builder`, which downloads the ontology in OWL format and writes a python module from it. See [Development](development.md#regenerating-the-ontologies) for how to update them to a newer ontology release.
