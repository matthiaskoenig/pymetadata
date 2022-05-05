.. image:: https://github.com/matthiaskoenig/pymetadata/raw/develop/docs/images/favicon/pymetadata-100x100-300dpi.png
   :align: left
   :alt: pymetadata logo

pymetadata: python utilities for metadata and COMBINE archives
==============================================================

.. image:: https://github.com/matthiaskoenig/pymetadata/workflows/CI-CD/badge.svg
   :target: https://github.com/matthiaskoenig/pymetadata/workflows/CI-CD
   :alt: GitHub Actions CI/CD Status

.. image:: https://img.shields.io/pypi/v/pymetadata.svg
   :target: https://pypi.org/project/pymetadata/
   :alt: Current PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/pymetadata.svg
   :target: https://pypi.org/project/pymetadata/
   :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/pymetadata.svg
   :target: http://opensource.org/licenses/LGPL-3.0
   :alt: GNU Lesser General Public License 3

.. image:: https://codecov.io/gh/matthiaskoenig/pymetadata/branch/develop/graph/badge.svg
   :target: https://codecov.io/gh/matthiaskoenig/pymetadata
   :alt: Codecov

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg
   :target: https://doi.org/10.5281/zenodo.5308801
   :alt: Zenodo DOI

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Black

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
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

* Source Code: `LGPLv3 <http://opensource.org/licenses/LGPL-3.0>`__
* Documentation: `CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`__

The pymetadata source is released under both the GPL and LGPL licenses version 2 or
later. You may choose which license you choose to use the software under.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License or the GNU Lesser General Public
License as published by the Free Software Foundation, either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

Funding
=======
Matthias König is supported by the Federal Ministry of Education and Research (BMBF, Germany)
within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054) 
and by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151 
"`QuaLiPerF <https://qualiperf.de>`__ (Quantifying Liver Perfusion-Function Relationship in Complex Resection - 
A Systems Medicine Approach)" by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA).

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

© 2021-2022 Matthias König
