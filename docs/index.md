![](images/favicon/pymetadata-100x100-300dpi.png)

# pymetadata: python utilities for metadata and COMBINE archives
[![GitHub Actions CI/CD Status](https://github.com/matthiaskoenig/pymetadata/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/matthiaskoenig/pymetadata/actions/workflows/ci-cd.yml) [![Documentation](https://img.shields.io/badge/docs-pymetadata-008080.svg)](https://matthiaskoenig.github.io/pymetadata) [![Version](https://img.shields.io/pypi/v/pymetadata.svg)](https://pypi.org/project/pymetadata/) [![Python Versions](https://img.shields.io/pypi/pyversions/pymetadata.svg)](https://pypi.org/project/pymetadata/) [![MIT License](https://img.shields.io/pypi/l/pymetadata.svg)](https://opensource.org/licenses/MIT) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg)](https://doi.org/10.5281/zenodo.5308801)

`pymetadata` is a collection of python utilities for working with metadata in the context of [COMBINE](https://co.mbine.org/) standards. The source code is available from [https://github.com/matthiaskoenig/pymetadata](https://github.com/matthiaskoenig/pymetadata).

## Background

Computational models in systems biology are rarely a single file. A study typically consists of one or more models (SBML, CellML), simulation experiments (SED-ML), figures, data files and a description of what the whole thing is about. Two problems follow from this:

**How do you ship such a study as one unit?** The [COMBINE archive](https://combinearchive.org/) (OMEX) answers this. It is a ZIP container with a `manifest.xml` listing every file and, for each file, the format it is in as an identifiers.org URI ([Bergmann et al. 2014](https://doi.org/10.1186/s12859-014-0369-z), [Bergmann et al. 2015](https://doi.org/10.2390/biecoll-jib-2015-261)). `pymetadata` reads, writes and validates these archives, see [COMBINE archives](omex.md).

**How do you say what the parts of a model mean?** A species named `glc` is meaningless to a machine. MIRIAM annotations attach a qualifier (*what is the relation?*) and a resource (*which database entry?*) to a model element, e.g., "this species **is** [CHEBI:17234](https://identifiers.org/CHEBI:17234)". `pymetadata` parses, normalizes and validates these annotations against the [identifiers.org](https://identifiers.org) registry and resolves additional information from the [Ontology Lookup Service](https://www.ebi.ac.uk/ols4), see [Annotations](annotations.md).

## Features

- **[COMBINE archives](omex.md)** — read and write OMEX archives, work with the `manifest.xml`, create archives from directories or single files, and read archives directly from a URL.
- **[Annotations](annotations.md)** — MIRIAM qualifiers (`BQB`, `BQM`), normalization of resources to identifiers.org compact identifiers, validation against the identifiers.org registry, and lookup of labels, descriptions, synonyms and cross references via OLS.
- **[Ontologies](annotations.md#ontology-terms)** — SBO, KISAO and PBPKO are shipped as python classes of terms, so a term is completed by the editor, checked at runtime and carries its label, definition and synonyms.

## Quickstart

Create a COMBINE archive from a model file, then read it back and resolve an entry to a file:

```python
from pathlib import Path
from pymetadata.omex import EntryFormat, ManifestEntry, Omex

# create an archive
omex = Omex()
omex.add_entry(
    entry_path=Path("model.xml"),
    entry=ManifestEntry(
        location="./model.xml", format=EntryFormat.SBML_L3V2, master=True
    ),
)
omex.to_omex(Path("archive.omex"))

# read an archive; the context manager removes the temporary directory
with Omex.from_omex(Path("archive.omex")) as omex:
    print(omex.manifest["./model.xml"].format)
    # http://identifiers.org/combine.specifications/sbml.level-3.version-2

    for entry in omex.entries_by_format("sbml"):
        print(entry.location, omex.get_path(entry.location))
        # ./model.xml /tmp/tmpb0m1xyz/model.xml
```

Annotate a model element with a MIRIAM qualifier and use ontology terms instead of strings:

```python
from pymetadata.core.annotation import RDFAnnotation
from pymetadata.core.miriam import BQB
from pymetadata.ontologies import SBO

annotation = RDFAnnotation(qualifier=BQB.IS, resource="CHEBI:17234")
print(annotation.resource_normalized)
# https://identifiers.org/CHEBI:17234

# a term is its identifier and knows what it means
print(SBO.SIMPLE_CHEMICAL, SBO.SIMPLE_CHEMICAL.label)
# SBO_0000247 simple chemical
```

If you have any questions or issues please [open an issue](https://github.com/matthiaskoenig/pymetadata/issues).

# How to cite
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg)](https://doi.org/10.5281/zenodo.5308801)

If you use `pymetadata` please cite the archived software on [Zenodo](https://doi.org/10.5281/zenodo.5308801):

> König, M. (2026). *pymetadata are python utilities for working with metadata* (Version 0.5.12) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.19709022

```bibtex
@software{konig_pymetadata,
  author    = {König, Matthias},
  title     = {pymetadata are python utilities for working with metadata},
  year      = {2026},
  month     = apr,
  version   = {0.5.12},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.19709022},
  url       = {https://doi.org/10.5281/zenodo.19709022},
}
```

# License
- Source Code: [MIT](https://opensource.org/license/MIT)
- Documentation: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

# Funding
Matthias König is supported and by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151 "QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach)" by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA).

Matthias König was supported by the Federal Ministry of Education and Research (BMBF, Germany) within the research network Systems Medicine of the Liver (LiSyM, grant number 031L0054).


© 2021-2026 Matthias König
