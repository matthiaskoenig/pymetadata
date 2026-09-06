# Installation

`pymetadata` requires python >= 3.11 and is available from [pypi](https://pypi.python.org/pypi/pymetadata):

```bash
pip install pymetadata
```

With [uv](https://docs.astral.sh/uv/):

```bash
uv add pymetadata
```

The package has no compiled dependencies, so the installation works the same on Linux, macOS and Windows. To install the current development version directly from GitHub use

```bash
pip install git+https://github.com/matthiaskoenig/pymetadata.git@develop
```

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

## Optional dependencies

Regenerating the ontologies reads OWL files and writes python modules, which needs `pronto`. These are optional, because the enums in `pymetadata.ontologies` are shipped with the package and using them requires nothing extra:

```bash
pip install pymetadata[ontology]
```

Without it `pymetadata.ontologies._ontology_builder` can still be imported, but `Ontology` raises an `ImportError` explaining what to install. See [Regenerating the ontologies](development.md#regenerating-the-ontologies).

For a development setup with the test and documentation tooling see [Development](development.md).

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
