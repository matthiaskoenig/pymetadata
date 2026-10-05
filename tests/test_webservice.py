"""Testing the shared web service session."""

import pytest
import requests

from pymetadata.webservices.webservice import (
    BACKOFF_FACTOR,
    RETRIES,
    RETRY_STATUS_CODES,
    TIMEOUT,
    _TimeoutHTTPAdapter,
    get_session,
)


def test_session_is_shared() -> None:
    """Test that the session is created once."""
    assert get_session() is get_session()
    assert isinstance(get_session(), requests.Session)


def test_session_retries_transient_responses() -> None:
    """Test that the transient server responses are retried."""
    adapter = get_session().get_adapter("https://www.ebi.ac.uk")
    assert isinstance(adapter, _TimeoutHTTPAdapter)
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
    assert isinstance(adapter, _TimeoutHTTPAdapter)
    assert adapter.timeout == TIMEOUT


def test_get_json_raises_not_found_for_404(monkeypatch: pytest.MonkeyPatch) -> None:
    """A 404 is the dedicated not found error, a subclass of the webservice error."""
    from pymetadata.webservices import webservice

    class Response:
        status_code = 404

    class Session:
        def get(self, url: str, params: object = None) -> Response:
            return Response()

    monkeypatch.setattr(webservice, "get_session", lambda: Session())
    with pytest.raises(webservice.WebserviceNotFoundError):
        webservice.get_json("https://example.org/missing")
    assert issubclass(webservice.WebserviceNotFoundError, webservice.WebserviceError)
