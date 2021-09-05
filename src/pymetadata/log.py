from rich.console import Console
from rich.markdown import Markdown
from rich import inspect
from rich import syntax

import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

console = Console()