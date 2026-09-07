"""Web services queried by pymetadata.

Annotations are validated and enriched with information which does not ship
with the package, so the modules here query remote services:

| module | service |
| --- | --- |
| `registry` | the [identifiers.org](https://identifiers.org) registry, i.e., the namespaces and the patterns their terms match |
| `ols` | the [Ontology Lookup Service](https://www.ebi.ac.uk/ols4), i.e., labels, descriptions and synonyms of ontology terms |
| `chebi` | [ChEBI](https://www.ebi.ac.uk/chebi/), i.e., information on chemical entities |
| `unichem` | [UniChem](https://www.ebi.ac.uk/unichem/), i.e., cross references between substance databases |

All of them use the shared session of `webservice`, which retries transient
server responses and applies a default timeout, and cache their responses with
`pymetadata.cache` while `pymetadata.CACHE_USE` is set, which it is by default.

Every query needs network access, and the status code of a response has to be
checked before it is parsed: a service which is unavailable for longer than the
retries answers with an error page, not with the expected JSON.
"""
