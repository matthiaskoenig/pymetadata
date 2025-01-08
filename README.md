![pymetadata logo](https://github.com/matthiaskoenig/pymetadata/raw/develop/docs/images/favicon/pymetadata-100x100-300dpi.png)

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
- SBO and KISAO ontology enums
 
If you have any questions or issues please [open an issue](https://github.com/matthiaskoenig/pymetadata/issues).

# Documentation
Documentation is still work in progress. For an example usage of the COMBINE archive
see [omex_example.py](src/pymetadata/examples/omex_example.py).

# How to cite
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg)](https://doi.org/10.5281/zenodo.5308801)

# Contributing
Contributions are always welcome! Please read the [contributing guidelines](https://github.com/matthiaskoenig/pymetadata/blob/develop/.github/CONTRIBUTING.rst) to get started.

# License
- Source Code: [MIT](https://opensource.org/license/MIT)
- Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

# Funding
Matthias König (MK) was supported by the Federal Ministry of Education and Research (BMBF, Germany) within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054). MK is supported by the Federal Ministry of Education and Research (BMBF, Germany) within ATLAS by grant number 031L0304B and by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA).

# Installation
`pymetadata` is available from [pypi](https://pypi.python.org/pypi/pymetadata) and 
can be installed via

```bash
pip install pymetadata
```

## Develop version
The latest develop version can be installed via
```bash
pip install git+https://github.com/matthiaskoenig/pymetadata.git@develop
```

Or via cloning the repository and installing via
```bash
git clone https://github.com/matthiaskoenig/pymetadata.git
cd pymetadata
pip install -e .
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

© 2021-2025 Matthias König
