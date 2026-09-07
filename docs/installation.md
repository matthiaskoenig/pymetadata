# Installation

`pymetadata` requires python >= 3.11 and is available from [pypi](https://pypi.python.org/pypi/pymetadata). It is pure python without compiled dependencies, so the installation is the same on Linux, macOS and Windows.

## With uv

[uv](https://docs.astral.sh/uv/) is the recommended way to install the package. In a project it is added as a dependency, which resolves and locks it together with the rest of the environment:

```bash
uv add pymetadata
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

Some `pymetadata` features query web services: the [identifiers.org](https://identifiers.org) registry when annotations are validated, the [Ontology Lookup Service](https://www.ebi.ac.uk/ols4) when annotation information is resolved, and ChEBI and UniChem for substance cross references. Responses are cached on disk so that repeated lookups of the same term do not hit the network again.

Caching is controlled by two module level settings:

```python
import pymetadata

pymetadata.CACHE_USE  # True by default
pymetadata.CACHE_PATH  # ~/.cache/pymetadata by default
```

Both are read when a query is made, so they can be changed at any point after importing the package, e.g., to cache elsewhere or to always see the current state of a service:

```python
from pathlib import Path
import pymetadata

pymetadata.CACHE_PATH = Path("/tmp/pymetadata_cache")
pymetadata.CACHE_USE = False  # query the services every time
```

### Cache duration

Cached content is refreshed once it is older than the cache duration of its service:

| content | duration | why |
| --- | --- | --- |
| OLS, ChEBI and UniChem responses | 30 days | they describe the terms of an ontology release, which changes with the release |
| identifiers.org registry | 24 hours | namespaces and their patterns are added and corrected continuously |

The durations are `CACHE_DURATION_ONTOLOGY` and `CACHE_DURATION_REGISTRY` in `pymetadata.cache`.

### Outdated content instead of a failure

If content has to be refreshed but the service cannot be reached, because there is no network or the service is down, the outdated content is used and a warning is logged:

```
Using the cache from 1080.0 h ago, it could not be refreshed:
/home/user/.cache/pymetadata/ols/....json (Service is not reachable for ...)
```

A query which was answered before therefore keeps working offline. Only a query which was never cached fails: `ChebiQuery.query` and `OLSQuery.query_ols` report the problem in their result, `UnichemQuery` and `Registry` raise a `WebserviceError`.

### The registry

The identifiers.org registry is cached independently of `CACHE_USE`. It is downloaded to `CACHE_PATH / "identifiers_registry.json"` and refreshed when the local copy is older than the cache duration:

```python
from pymetadata.webservices.registry import Registry

registry = Registry(cache_duration=24, cache=True)
namespace = registry.ns_dict["chebi"]
print(namespace.pattern)
# ^CHEBI:\d+$
```

Deleting `CACHE_PATH` is always safe; everything in it is re-downloaded on demand.
