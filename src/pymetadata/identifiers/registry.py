"""
Helper tools to work with identifiers registry.

https://identifiers.org/
https://docs.identifiers.org/articles/api.html
"""

from __future__ import annotations

import inspect
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

import pymetadata
from pymetadata import log
from pymetadata.cache import DataclassJSONEncoder, read_json_cache, write_json_cache
from pymetadata.console import console

logger = log.get_logger(__name__)


@dataclass
class Resource:
    """Resource."""

    id: Optional[int]
    providerCode: str
    name: str
    urlPattern: str
    mirId: Optional[str] = field(repr=False)
    description: str = field(repr=False)
    official: bool = field(repr=False)

    sampleId: Optional[str] = field(repr=False)
    resourceHomeUrl: Optional[str] = field(repr=False)
    institution: dict = field(repr=False)
    location: dict = field(repr=False)
    deprecated: bool = field(repr=False)
    deprecationDate: str = field(repr=False)
    protectedUrls: bool = field(repr=False, default=False)
    renderProtectedLanding: bool = field(repr=False, default=False)
    authHelpUrl: Optional[str] = field(repr=False, default=None)
    authHelpDescription: Optional[str] = field(repr=False, default=None)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Resource:
        """Handle additional keyword arguments."""
        return cls(
            **{k: v for k, v in d.items() if k in inspect.signature(cls).parameters}
        )


@dataclass
class Namespace:
    """Namespace."""

    id: Optional[str]
    prefix: Optional[str]
    name: str
    pattern: str
    namespaceEmbeddedInLui: bool
    description: str = field(repr=False)
    mirId: Optional[str] = field(repr=False, default=None)
    resources: Optional[List] = field(repr=False, default=None)
    created: Optional[str] = field(repr=False, default=None)
    modified: Optional[str] = field(repr=False, default=None)
    sampleId: Optional[str] = field(repr=False, default=None)
    deprecated: bool = field(repr=False, default=False)
    deprecationDate: Optional[str] = field(repr=False, default=None)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Namespace:
        """Handle additional keyword arguments."""
        return cls(
            **{k: v for k, v in d.items() if k in inspect.signature(cls).parameters}
        )

    def __post_init__(self) -> None:
        """Set resources."""
        if self.resources is not None:
            self.resources = [Resource.from_dict(d) for d in self.resources]
        else:
            self.resources = list()


class Registry:
    """Managing the available annotation information.

    Registry of meta information.
    """

    URL = "https://registry.api.identifiers.org/resolutionApi/getResolverDataset"

    def __init__(
        self,
        cache_duration: int = 24,
        cache: bool = True,
    ):
        """Initialize registry.

        :param cache_path: Path of cached identifiers.org path
        :param cache_duration: Duration of caching in hours.
        :param cache: boolean flag to stop caching
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

        self.ns_dict: Dict[str, Namespace] = (
            self.update() if update else Registry.load_registry(self.registry_path)
        )

    def update(self) -> Dict[str, Namespace]:
        """Update registry."""
        Registry.update_registry(registry_path=self.registry_path)
        return Registry.load_registry(registry_path=self.registry_path)

    @staticmethod
    def update_registry(
        registry_path: Optional[Path] = None,
    ) -> Dict[str, Namespace]:
        """Update registry from identifiers.org webservice."""
        logger.info(f"Update registry from '{Registry.URL}'")
        response = requests.get(Registry.URL)
        namespaces = response.json()["payload"]["namespaces"]

        ns_dict = {}
        for _, data in enumerate(namespaces):
            ns = Namespace.from_dict(data)
            ns_dict[ns.prefix] = ns

        if registry_path is not None:
            write_json_cache(
                data=ns_dict,
                cache_path=registry_path,
                json_encoder=DataclassJSONEncoder,
            )

        return ns_dict  # type: ignore

    @staticmethod
    def load_registry(registry_path: Path) -> Dict[str, Namespace]:
        """Load namespaces with resources from path."""
        if not registry_path.exists():
            Registry.update_registry(registry_path=registry_path)

        d = read_json_cache(cache_path=registry_path)
        if not d:
            raise ValueError("Registry could not be loaded from cache.")

        return {k: Namespace(**v) for k, v in d.items()}


REGISTRY = Registry()

if __name__ == "__main__":
    registry = Registry(cache=False)
    console.print(registry.ns_dict)
