r"""The identifiers.org registry.

The registry defines, for every collection (`chebi`, `uniprot`, `taxonomy`, ...),
the pattern a valid term matches and the providers which resolve a term to a
web page. `pymetadata` uses it to validate annotations and to build cross
references.

The registry is downloaded once and cached in
`CACHE_PATH / "identifiers_registry.json"`, and refreshed when the local copy is
older than the cache duration of `CACHE_DURATION_REGISTRY` hours. Namespaces are
added and corrected continuously, so the registry is refreshed daily, much more
often than the ontology information of `pymetadata.webservices.ols`. If the
refresh fails, because identifiers.org is unreachable, the outdated copy is used
and a warning is logged.

```python
from pymetadata.webservices.registry import Registry

registry = Registry()
namespace = registry.ns_dict["chebi"]
print(namespace.pattern)  # ^CHEBI:\d+$
```

See <https://identifiers.org/> and
<https://docs.identifiers.org/articles/api.html>.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any

import pymetadata
from pymetadata.cache import (
    CACHE_DURATION_REGISTRY,
    DataclassJSONEncoder,
    cache_age,
    read_json_cache,
    read_json_cache_fallback,
    write_json_cache,
)
from pymetadata.console import console
from pymetadata.webservices.webservice import WebserviceError, get_json

logger = logging.getLogger(__name__)


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
    institution: dict[str, Any] = field(repr=False)
    location: dict[str, Any] = field(repr=False)
    deprecated: bool = field(repr=False)
    deprecationDate: str = field(repr=False)
    protectedUrls: bool = field(repr=False, default=False)
    renderProtectedLanding: bool = field(repr=False, default=False)
    authHelpUrl: str | None = field(repr=False, default=None)
    authHelpDescription: str | None = field(repr=False, default=None)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Resource:
        """Create a resource from a registry response, ignoring unknown keys.

        Args:
            d: resource of the registry response or of the cached registry

        Returns:
            The resource.
        """
        return cls(**{k: v for k, v in d.items() if k in _RESOURCE_FIELDS})


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
    resources: list[Resource] | None = field(repr=False, default=None)
    created: str | None = field(repr=False, default=None)
    modified: str | None = field(repr=False, default=None)
    sampleId: str | None = field(repr=False, default=None)
    deprecated: bool = field(repr=False, default=False)
    deprecationDate: str | None = field(repr=False, default=None)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Namespace:
        """Create a namespace from a registry response, ignoring unknown keys.

        Args:
            d: namespace of the registry response or of the cached registry

        Returns:
            The namespace with its resources.
        """
        return cls(**{k: v for k, v in d.items() if k in _NAMESPACE_FIELDS})

    def __post_init__(self) -> None:
        """Set resources, creating them from dictionaries if necessary."""
        self.resources = [
            Resource.from_dict(r) if isinstance(r, dict) else r
            for r in self.resources or []
        ]


# field names to filter registry responses with, unknown keys are ignored
_RESOURCE_FIELDS: frozenset[str] = frozenset(f.name for f in fields(Resource))
_NAMESPACE_FIELDS: frozenset[str] = frozenset(f.name for f in fields(Namespace))


class Registry:
    """The identifiers.org registry, cached on disk.

    The cached registry is refreshed once it is older than the cache duration.
    If identifiers.org cannot be reached, the outdated copy is used however old
    it is, so that validating annotations keeps working offline.

    Attributes:
        ns_dict: namespaces of the registry by prefix
        registry_path: path of the cached registry
    """

    URL = "https://registry.api.identifiers.org/resolutionApi/getResolverDataset"

    def __init__(
        self,
        cache_duration: float = CACHE_DURATION_REGISTRY,
        cache: bool = True,
    ):
        """Load the registry, updating the cached copy if it is outdated.

        Args:
            cache_duration: maximum age of the cached registry in hours
            cache: use the cached registry; if False the registry is downloaded
                and the cache is not read, not even when the download fails

        Raises:
            WebserviceError: if the registry is neither cached nor retrievable
        """
        self.registry_path = pymetadata.CACHE_PATH / "identifiers_registry.json"

        # check if update needed
        age = cache_age(self.registry_path) if cache else None
        update = age is None or age > cache_duration

        if not update:
            try:
                self.ns_dict: dict[str, Namespace] = Registry.load_registry(
                    self.registry_path
                )
                return
            except OSError as err:
                # e.g., a corrupt cache, which is removed by reading it
                logger.warning("Cached registry is downloaded again: %s", err)

        try:
            self.ns_dict = self.update()
        except WebserviceError as err:
            # prefer an outdated registry over none, e.g., when offline
            data = (
                read_json_cache_fallback(self.registry_path, reason=str(err))
                if cache
                else None
            )
            if data is None:
                raise
            self.ns_dict = Registry.namespaces_from_dict(data)

    def update(self) -> dict[str, Namespace]:
        """Download the registry, cache it and return the namespaces.

        The namespaces are the downloaded ones, they are not read back from the
        cache: writing the cache is best effort and fails, e.g., on Windows
        while another process reads the cached registry.

        Returns:
            Namespaces of the registry by prefix.

        Raises:
            WebserviceError: if the registry could not be downloaded
        """
        return Registry.update_registry(registry_path=self.registry_path)

    @staticmethod
    def namespaces_from_dict(data: dict[str, Any]) -> dict[str, Namespace]:
        """Build the namespaces from the serialized registry.

        Args:
            data: content of the cached registry

        Returns:
            Namespaces of the registry by prefix.
        """
        return {k: Namespace.from_dict(v) for k, v in data.items()}

    @staticmethod
    def update_registry(
        registry_path: Path | None = None,
    ) -> dict[str, Namespace]:
        """Download the registry from the identifiers.org web service.

        Namespaces without a prefix are skipped.

        Args:
            registry_path: path to cache the registry in, not cached if None.
                Writing the cache is best effort, see
                `pymetadata.cache.write_json_cache`

        Returns:
            Namespaces of the registry by prefix.

        Raises:
            WebserviceError: if the registry could not be downloaded
        """
        logger.info("Update registry from '%s'", Registry.URL)
        namespaces = get_json(Registry.URL)["payload"]["namespaces"]

        ns_dict: dict[str, Namespace] = {}
        for _, data in enumerate(namespaces):
            ns = Namespace.from_dict(data)
            if ns.prefix is None:
                logger.warning("Namespace without prefix is ignored: '%s'", ns)
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

        Raises:
            OSError: if the cached registry cannot be read or is corrupt
            WebserviceError: if the registry is missing and could not be
                downloaded
        """
        if not registry_path.exists():
            return Registry.update_registry(registry_path=registry_path)

        d = read_json_cache(cache_path=registry_path)
        if not d:
            raise ValueError("Registry could not be loaded from cache.")

        return Registry.namespaces_from_dict(d)


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
