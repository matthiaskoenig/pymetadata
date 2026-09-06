# API reference

The API reference is generated from the docstrings of the package.

## pymetadata

Top level modules. The ontology terms of SBO, KISAO, ECO and PBPKO are generated enums, see [Annotations](../annotations.md#ontology-enums).

| module | description |
| --- | --- |
| [cache](cache.md) | Caching of web service responses |
| [chebi](chebi.md) | Substance information from ChEBI |
| [console](console.md) | Shared rich console |
| [log](log.md) | Logging of the package |
| [omex](omex.md) | COMBINE archive (OMEX) support |
| [unichem](unichem.md) | Substance cross references from UniChem |
| [webservice](webservice.md) | HTTP access to the web services |

## pymetadata.core

Core data structures for annotations, creators and cross references.

| module | description |
| --- | --- |
| [core.annotation](core.annotation.md) | MIRIAM annotations |
| [core.creator](core.creator.md) | Creator information for models and archives |
| [core.xref](core.xref.md) | Cross references to database entries |

## pymetadata.identifiers

MIRIAM qualifiers and the identifiers.org registry.

| module | description |
| --- | --- |
| [identifiers.miriam](identifiers.miriam.md) | MIRIAM qualifiers |
| [identifiers.registry](identifiers.registry.md) | The identifiers.org registry |

## pymetadata.ontologies

Ontology lookup service and generation of the enum modules.

| module | description |
| --- | --- |
| [ontologies.ols](ontologies.ols.md) | Lookup of ontology terms in OLS |
| [ontologies.ontology](ontologies.ontology.md) | Downloading ontologies and generating the enums |
