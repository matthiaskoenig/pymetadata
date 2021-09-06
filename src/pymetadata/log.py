"""Logging helpers."""
import logging

from rich import inspect, syntax
from rich.console import Console
from rich.logging import RichHandler
from rich.markdown import Markdown


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

console = Console()
