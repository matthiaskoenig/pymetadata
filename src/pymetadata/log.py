"""Logging of the package.

`pymetadata` follows the convention for libraries: it only gets loggers and logs
to them, it does not configure logging. Handlers, levels and formatting are left
to the application, which keeps the messages of the package under the control of
whoever uses it.

Modules get their logger with

```python
from pymetadata import log

logger = log.get_logger(__name__)
```

which is `logging.getLogger(__name__)`. All loggers are below the `pymetadata`
logger, so an application configures them in one place:

```python
import logging

logging.getLogger("pymetadata").setLevel(logging.WARNING)
```

For scripts and interactive work the rich formatting of the package can be
enabled explicitly, which is what the examples do:

```python
from pymetadata import log

log.enable_rich_logging()
```
"""

import logging

from rich.console import Console
from rich.logging import RichHandler

from pymetadata.console import console as default_console

#: name of the logger all loggers of the package are below
PACKAGE_LOGGER = "pymetadata"


def get_logger(name: str) -> logging.Logger:
    """Get the logger for a module.

    No handler is attached and no level is set, see the module documentation.

    Args:
        name: name of the logger, usually `__name__`

    Returns:
        The logger for the name.
    """
    return logging.getLogger(name)


def enable_rich_logging(
    level: int = logging.INFO, console: Console | None = None
) -> logging.Logger:
    """Log the messages of the package on a rich console.

    This configures logging and is meant for scripts, examples and interactive
    work. Applications should configure logging themselves instead of calling
    this. Calling it repeatedly replaces the handler instead of adding a second
    one.

    Args:
        level: level from which messages are logged
        console: console to log on, the console of the package by default

    Returns:
        The `pymetadata` logger.
    """
    logger = logging.getLogger(PACKAGE_LOGGER)

    # remove a handler of an earlier call, logging twice is worse than not at all
    for handler in list(logger.handlers):
        if isinstance(handler, RichHandler):
            logger.removeHandler(handler)

    handler = RichHandler(
        markup=False,
        rich_tracebacks=True,
        show_time=False,
        console=console if console is not None else default_console,
    )
    handler.setFormatter(logging.Formatter(fmt="%(message)s", datefmt="[%X]"))

    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
