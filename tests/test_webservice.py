"""Testing the shared web service session."""

import requests

from pymetadata.webservice import (
    BACKOFF_FACTOR,
    RETRIES,
    RETRY_STATUS_CODES,
    TIMEOUT,
    get_session,
)


def test_session_is_shared() -> None:
    """Test that the session is created once."""
    assert get_session() is get_session()
    assert isinstance(get_session(), requests.Session)


def test_session_retries_transient_responses() -> None:
    """Test that the transient server responses are retried."""
    adapter = get_session().get_adapter("https://www.ebi.ac.uk")
    retries = adapter.max_retries

    assert retries.total == RETRIES
    assert retries.backoff_factor == BACKOFF_FACTOR
    for status_code in RETRY_STATUS_CODES:
        assert status_code in retries.status_forcelist

    # the status is checked by the caller, the retries must not raise
    assert retries.raise_on_status is False


def test_session_has_timeout() -> None:
    """Test that a default timeout is applied."""
    adapter = get_session().get_adapter("https://www.ebi.ac.uk")
    assert adapter.timeout == TIMEOUT
