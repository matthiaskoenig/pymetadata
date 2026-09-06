# API reference

The API reference is generated from the docstrings of the package.

## pymetadata

Top level modules.

| module | description |
| --- | --- |
| [cache](cache.md) | Caching of the web service responses |
| [console](console.md) | Shared rich console |
| [log](log.md) | Logging of the package |
| [omex](omex.md) | COMBINE archive (OMEX) support |

## pymetadata.core

Core data structures: annotations with their qualifiers, creators and cross references.

| module | description |
| --- | --- |
| [core.annotation](core.annotation.md) | MIRIAM annotations |
| [core.creator](core.creator.md) | Creator information for models and archives |
| [core.miriam](core.miriam.md) | MIRIAM qualifiers |
| [core.xref](core.xref.md) | Cross references to database entries |

## pymetadata.webservices

The services queried for the information which does not ship with the package. They share one session and the cache.

| module | description |
| --- | --- |
| [webservices.chebi](webservices.chebi.md) | Substance information from ChEBI |
| [webservices.ols](webservices.ols.md) | Lookup of ontology terms in the Ontology Lookup Service |
| [webservices.registry](webservices.registry.md) | The identifiers.org registry |
| [webservices.unichem](webservices.unichem.md) | Substance cross references from UniChem |
| [webservices.webservice](webservices.webservice.md) | The shared HTTP session |

## pymetadata.ontologies

The ontology terms of SBO, KISAO, ECO and PBPKO as generated enums, see [Annotations](../annotations.md#ontology-enums). They are built by the internal `_ontology_builder` module, see [Regenerating the ontology enums](../development.md#regenerating-the-ontology-enums), and are not part of the reference: the modules are generated and list one member per ontology term.
