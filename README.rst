.. image:: https://github.com/matthiaskoenig/pymetadata/raw/develop/docs/images/favicon/pymetadata-100x100-300dpi.png
   :align: left
   :alt: pymetadata logo

pymetadata: python utilities for metadata and COMBINE archives
==============================================================
|icon1| |icon2| |icon3| |icon4| |icon5| |icon6|


.. |icon1| image:: https://github.com/matthiaskoenig/pymetadata/workflows/CI-CD/badge.svg
   :target: https://github.com/matthiaskoenig/pymetadata/workflows/CI-CD
   :alt: GitHub Actions CI/CD Status
.. |icon2| image:: https://img.shields.io/pypi/v/pymetadata.svg
   :target: https://pypi.org/project/pymetadata/
   :alt: Current PyPI Version
.. |icon3| image:: https://img.shields.io/pypi/pyversions/pymetadata.svg
   :target: https://pypi.org/project/pymetadata/
   :alt: Supported Python Versions
.. |icon4| image:: https://img.shields.io/pypi/l/pymetadata.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT License
.. |icon5| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg
   :target: https://doi.org/10.5281/zenodo.5308801
   :alt: Zenodo DOI
.. |icon6| image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: http://mypy-lang.org/
   :alt: mypy

pymetadata is a collection of python utilities for working with
metadata in the context of COMBINE standards with source code available from 
`https://github.com/matthiaskoenig/pymetadata <https://github.com/matthiaskoenig/pymetadata>`__.

Features include among others

- COMBINE archive version 1 support (OMEX)
- annotation classes and helpers
- SBO and KISAO ontology enums
 
If you have any questions or issues please `open an issue <https://github.com/matthiaskoenig/pymetadata/issues>`__.

Documentation
=============
Documentation is still work in progress. For an example usage of the COMBINE archive
see `src/pymetadata/examples/omex_example.py <src/pymetadata/examples/omex_example.py>`__.

How to cite
===========

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg
   :target: https://doi.org/10.5281/zenodo.5308801
   :alt: Zenodo DOI

Contributing
============

Contributions are always welcome! Please read the `contributing guidelines
<https://github.com/matthiaskoenig/pymetadata/blob/develop/.github/CONTRIBUTING.rst>`__ to
get started.

License
=======
* Source Code: `MIT <https://opensource.org/license/MIT>`__
* Documentation: `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`__

Funding
=======
Matthias König (MK) was supported by the Federal Ministry of Education and Research (BMBF, Germany) within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054). MK is supported by the Federal Ministry of Education and Research (BMBF, Germany) within ATLAS by grant number 031L0304B and by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA).

Installation
============
`pymetadata` is available from `pypi <https://pypi.python.org/pypi/pymetadata>`__ and 
can be installed via:: 

    pip install pymetadata

Develop version
---------------
The latest develop version can be installed via::

    pip install git+https://github.com/matthiaskoenig/pymetadata.git@develop

Or via cloning the repository and installing via::

    git clone https://github.com/matthiaskoenig/pymetadata.git
    cd pymetadata
    pip install -e .


To install for development use::

    pip install -e .[development]


Cache path
==========
`pymetadata` caches some information for faster retrieval. The cache path is set to::

    CACHE_PATH: Path = Path.home() / ".cache" / "pymetadata"

To use a custom cache path use::

    import pymetadata
    pymetadata.CACHE_PATH = <cache_path>


Checks
==========
- uv for project setup
- ruff for linting, formating
- mypy for type checking

© 2021-2025 Matthias König
