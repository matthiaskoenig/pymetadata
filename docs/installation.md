# Installation

`pymetadata` requires python >= 3.11 and is available from [pypi](https://pypi.python.org/pypi/pymetadata). It is pure python without compiled dependencies, so the installation is the same on Linux, macOS and Windows.

## With uv

[uv](https://docs.astral.sh/uv/) is the recommended way to install the package. In a project it is added as a dependency, which resolves and locks it together with the rest of the environment:

```bash
uv add pymetadata
```

For a quick look without setting up a project, `uv run` installs it into a temporary environment for the duration of the command:

```bash
uv run --with pymetadata python
```

Into an existing virtual environment it is installed through the pip interface of uv:

```bash
uv venv
uv pip install pymetadata
```

## With pip

```bash
pip install pymetadata
```

## Development version

The current state of the `develop` branch is installed directly from GitHub:

```bash
uv add "pymetadata @ git+https://github.com/matthiaskoenig/pymetadata.git@develop"
```

or, with pip,

```bash
pip install git+https://github.com/matthiaskoenig/pymetadata.git@develop
```

To work on the repository itself, with the test and documentation tooling, see [Development](development.md).

## Logging

`pymetadata` does not configure logging. It logs to loggers below the `pymetadata` logger and leaves handlers, levels and formatting to the application, so the messages of the package stay under your control:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("pymetadata").setLevel(logging.WARNING)
```

For scripts and interactive work the rich output of the package can be turned on explicitly:

```python
from pymetadata import log

log.enable_rich_logging()
```

## Cache

Some `pymetadata` features query web services: the [identifiers.org](https://identifiers.org) registry when annotations are validated, the [Ontology Lookup Service](https://www.ebi.ac.uk/ols4) when annotation information is resolved, and ChEBI and UniChem for substance cross references. Responses can be cached on disk so that repeated lookups of the same term do not hit the network again.

Caching is controlled by two module level settings:

```python
import pymetadata

pymetadata.CACHE_USE  # False by default
pymetadata.CACHE_PATH  # ~/.cache/pymetadata by default
```

Both are read when a query is made, so they can be changed at any point after importing the package:

```python
from pathlib import Path
import pymetadata

pymetadata.CACHE_USE = True
pymetadata.CACHE_PATH = Path("/tmp/pymetadata_cache")
```

The identifiers.org registry is cached independently of `CACHE_USE`. It is downloaded to `CACHE_PATH / "identifiers_registry.json"` and refreshed when the local copy is older than the cache duration (24 hours by default):

```python
from pymetadata.webservices.registry import Registry

registry = Registry(cache_duration=24, cache=True)
namespace = registry.ns_dict["chebi"]
print(namespace.pattern)
# ^CHEBI:\d+$
```

Deleting `CACHE_PATH` is always safe; everything in it is re-downloaded on demand.
