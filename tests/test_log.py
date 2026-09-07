"""Testing the logging policy of the package."""

import logging
import sys

from rich.logging import RichHandler

from pymetadata import log


def test_module_logger_is_not_configured() -> None:
    """Test that a module of the package neither adds a handler nor sets a level.

    Configuring logging is the task of the application, not of the library.
    """
    import pymetadata.omex  # noqa: F401

    logger = logging.getLogger("pymetadata.omex")

    assert logger.handlers == []
    assert logger.level == logging.NOTSET


def test_package_logger_has_null_handler() -> None:
    """Test that the package logger swallows messages without configuration."""
    handlers = logging.getLogger(log.PACKAGE_LOGGER).handlers
    assert any(isinstance(handler, logging.NullHandler) for handler in handlers)


def test_import_does_not_change_displayhook() -> None:
    """Test that importing the package leaves the interpreter alone."""
    import pymetadata.console  # noqa: F401

    assert sys.displayhook is sys.__displayhook__


def test_enable_rich_logging_is_idempotent() -> None:
    """Test that enabling the rich output twice does not log twice."""
    package_logger = logging.getLogger(log.PACKAGE_LOGGER)
    level_before = package_logger.level
    handlers_before = list(package_logger.handlers)

    try:
        log.enable_rich_logging()
        log.enable_rich_logging()

        rich_handlers = [
            handler
            for handler in package_logger.handlers
            if isinstance(handler, RichHandler)
        ]
        assert len(rich_handlers) == 1
        assert package_logger.level == logging.INFO
    finally:
        package_logger.handlers = handlers_before
        package_logger.setLevel(level_before)
