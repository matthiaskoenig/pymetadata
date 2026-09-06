r"""The identifiers.org registry.

The registry defines, for every collection (`chebi`, `uniprot`, `taxonomy`, ...),
the pattern a valid term matches and the providers which resolve a term to a
web page. `pymetadata` uses it to validate annotations and to build cross
references.

The registry is downloaded once and cached in
`CACHE_PATH / "identifiers_registry.json"`, and refreshed when the local copy is
older than the cache duration.

```python
from pymetadata.identifiers.registry import Registry

registry = Registry()
namespace = registry.ns_dict["chebi"]
print(namespace.pattern)  # ^CHEBI:\d+$
```

See <https://identifiers.org/> and
<https://docs.identifiers.org/articles/api.html>.
"""

from __future__ import annotations

import inspect
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import requests

import pymetadata
from pymetadata import log
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache
from pymetadata.console import console

logger = log.get_logger(__name__)


@dataclass
class Resource:
    """A provider which resolves terms of a collection.

    A collection can have several providers; `urlPattern` contains the
    placeholder `{$id}` which is replaced by the term to build the url of an
    entry.
    """

    id: int | None
    providerCode: str
    name: str
    urlPattern: str
    mirId: str | None = field(repr=False)
    description: str = field(repr=False)
    official: bool = field(repr=False)

    sampleId: str | None = field(repr=False)
    resourceHomeUrl: str | None = field(repr=False)
    institution: dict = field(repr=False)
    location: dict = field(repr=False)
    deprecated: bool = field(repr=False)
    deprecationDate: str = field(repr=False)
    protectedUrls: bool = field(repr=False, default=False)
    renderProtectedLanding: bool = field(repr=False, default=False)
    authHelpUrl: str | None = field(repr=False, default=None)
    authHelpDescription: str | None = field(repr=False, default=None)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Resource:
        """Create a resource from a registry response, ignoring unknown keys."""
        return cls(
            **{k: v for k, v in d.items() if k in inspect.signature(cls).parameters}
        )


@dataclass
class Namespace:
    """A collection of the identifiers.org registry.

    Attributes:
        prefix: prefix of the collection, e.g., `chebi`
        name: name of the collection
        pattern: regular expression a valid term matches
        namespaceEmbeddedInLui: whether the prefix is part of the term itself,
            as for `CHEBI:33699` and `GO:0005829`
        resources: providers which resolve terms of this collection
    """

    id: str | None
    prefix: str | None
    name: str
    pattern: str
    namespaceEmbeddedInLui: bool
    description: str = field(repr=False)
    mirId: str | None = field(repr=False, default=None)
    resources: list | None = field(repr=False, default=None)
    created: str | None = field(repr=False, default=None)
    modified: str | None = field(repr=False, default=None)
    sampleId: str | None = field(repr=False, default=None)
    deprecated: bool = field(repr=False, default=False)
    deprecationDate: str | None = field(repr=False, default=None)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Namespace:
        """Create a namespace from a registry response, ignoring unknown keys."""
        return cls(
            **{k: v for k, v in d.items() if k in inspect.signature(cls).parameters}
        )

    def __post_init__(self) -> None:
        """Set resources."""
        if self.resources is not None:
            self.resources = [Resource.from_dict(d) for d in self.resources]
        else:
            self.resources = []


class Registry:
    """The identifiers.org registry, cached on disk.

    Attributes:
        ns_dict: namespaces of the registry by prefix
        registry_path: path of the cached registry
    """

    URL = "https://registry.api.identifiers.org/resolutionApi/getResolverDataset"

    def __init__(
        self,
        cache_duration: int = 24,
        cache: bool = True,
    ):
        """Load the registry, updating the cached copy if it is outdated.

        Args:
            cache_duration: maximum age of the cached registry in hours
            cache: use the cached registry; if False the registry is downloaded
        """
        self.registry_path = pymetadata.CACHE_PATH / "identifiers_registry.json"

        # check if update needed
        if cache:
            if os.path.exists(self.registry_path):
                registry_age = (
                    time.time() - os.path.getmtime(self.registry_path)
                ) / 3600  # [hr]
                update = registry_age > cache_duration
            else:
                update = True
        else:
            update = True

        self.ns_dict: dict[str, Namespace] = (
            self.update() if update else Registry.load_registry(self.registry_path)
        )

    def update(self) -> dict[str, Namespace]:
        """Download the registry and return the namespaces.

        Returns:
            Namespaces of the registry by prefix.
        """
        Registry.update_registry(registry_path=self.registry_path)
        return Registry.load_registry(registry_path=self.registry_path)

    @staticmethod
    def update_registry(
        registry_path: Path | None = None,
    ) -> dict[str, Namespace]:
        """Download the registry from the identifiers.org web service.

        Namespaces without a prefix are skipped.

        Args:
            registry_path: path to cache the registry in, not cached if None

        Returns:
            Namespaces of the registry by prefix.
        """
        logger.info(f"Update registry from '{Registry.URL}'")
        response = requests.get(Registry.URL)
        namespaces = response.json()["payload"]["namespaces"]

        ns_dict: dict[str, Namespace] = {}
        for _, data in enumerate(namespaces):
            ns = Namespace.from_dict(data)
            if ns.prefix is None:
                logger.warning(f"Namespace without prefix is ignored: '{ns}'")
                continue
            ns_dict[ns.prefix] = ns

        if registry_path is not None:
            write_json_cache(
                data=ns_dict,
                cache_path=registry_path,
                json_encoder=DataclassJSONEncoder,
            )

        return ns_dict

    @staticmethod
    def load_registry(registry_path: Path) -> dict[str, Namespace]:
        """Load the registry from the cached file, downloading it if missing.

        Args:
            registry_path: path of the cached registry

        Returns:
            Namespaces of the registry by prefix.
        """
        if not registry_path.exists():
            Registry.update_registry(registry_path=registry_path)

        d = read_json_cache(cache_path=registry_path)
        if not d:
            raise ValueError("Registry could not be loaded from cache.")

        return {k: Namespace(**v) for k, v in d.items()}


_REGISTRY: Registry | None = None


def get_registry() -> Registry:
    """Get the shared registry, loading it on first use.

    The registry is loaded lazily so that importing pymetadata does not query
    the identifiers.org web service.

    Returns:
        The shared registry instance.
    """
    global _REGISTRY
    if _REGISTRY is None:
        _REGISTRY = Registry()
    return _REGISTRY


def __getattr__(name: str) -> Any:
    """Resolve `REGISTRY` lazily (PEP 562)."""
    if name == "REGISTRY":
        return get_registry()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


if __name__ == "__main__":
    registry = Registry(cache=False)
    console.print(registry.ns_dict)
