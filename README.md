![pymetadata logo](./_docs/images/favicon/pymetadata-100x100-300dpi.png)

# pymetadata: python utilities for metadata and COMBINE archives
[![GitHub Actions CI/CD Status](https://github.com/matthiaskoenig/pymetadata/workflows/CI-CD/badge.svg)](https://github.com/matthiaskoenig/pymetadata/actions/workflows/main.yml)
[![Version](https://img.shields.io/pypi/v/pymetadata.svg)](https://pypi.org/project/pymetadata/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pymetadata.svg)](https://pypi.org/project/pymetadata/)
[![MIT License](https://img.shields.io/pypi/l/pymetadata.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg)](https://doi.org/10.5281/zenodo.5308801)

pymetadata is a collection of python utilities for working with
metadata in the context of COMBINE standards with source code available from
[https://github.com/matthiaskoenig/pymetadata](https://github.com/matthiaskoenig/pymetadata).

Features include among others

- COMBINE archive version 1 support (OMEX)
- annotation classes and helpers
- SBO, KISAO and ECO ontology enums

If you have any questions or issues please [open an issue](https://github.com/matthiaskoenig/pymetadata/issues).

Documentation is available from https://matthiaskoenig.github.io/pymetadata.

A presentation from HARMONY2026 is available [here](https://matthiaskoenig.github.io/pymetadata/presentations/HARMONY2026/pymetadata.html).

# Installation
`pymetadata` is available from [pypi](https://pypi.python.org/pypi/pymetadata) and
can be installed via

```bash
pip install pymetadata
```

# Cache path
`pymetadata` caches some information for faster retrieval. The cache path is set to

```python
CACHE_PATH: Path = Path.home() / ".cache" / "pymetadata"
```

To use a custom cache path use

```python
import pymetadata
pymetadata.CACHE_PATH = <cache_path>
```


# How to cite
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg)](https://doi.org/10.5281/zenodo.5308801)

# License
- Source Code: [MIT](https://opensource.org/license/MIT)
- Documentation: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

# Funding
Matthias König is supported and by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151
"QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection -
A Systems Medicine Approach)" by grant number 436883643 and by grant number
465194077 (Priority Programme SPP 2311, Subproject SimLivA).

Matthias König was supported by the Federal Ministry of Education and Research (BMBF, Germany)
within the research network Systems Medicine of the Liver (LiSyM, grant number 031L0054).

© 2021-2026 Matthias König
