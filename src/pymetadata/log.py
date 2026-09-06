"""Logging setup.

Every module gets its logger from here instead of calling `logging` directly, so
that all messages are formatted by rich and printed on the shared console.

```python
from pymetadata import log

logger = log.get_logger(__name__)
logger.info("message")
```
"""

import logging

from rich.logging import RichHandler

from pymetadata.console import console


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Get a logger which logs to the shared rich console.

    Args:
        name: name of the logger, usually `__name__`
        level: level from which messages are logged

    Returns:
        The configured logger.
    """
    formatter = logging.Formatter(
        fmt="%(message)s",
        datefmt="[%X]",
    )

    # handler = logging.StreamHandler()
    handler = RichHandler(
        markup=False, rich_tracebacks=True, show_time=False, console=console
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
