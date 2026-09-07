"""HTTP access to the web services.

The queried services (identifiers.org, OLS, ChEBI, UniChem) answer with a
transient error every now and then, e.g., a HTML error page with status 500
instead of the expected JSON. `get_session` provides a shared `requests.Session`
which retries these responses with an exponential backoff and applies a default
timeout, so that a single hiccup of a service does not fail the query.

```python
from pymetadata.webservices.webservice import get_json

data = get_json("https://www.ebi.ac.uk/unichem/rest/inchikey/...")
```

`get_json` raises a `WebserviceError` for everything which keeps a query from
answering, i.e., an unreachable service, an error response and a response which
is not JSON. A service which is down for longer than the retries answers with an
HTML error page, so the status code has to be checked before the response is
parsed; `get_json` does that and the callers fall back to their cache, see
`pymetadata.cache`.
"""

import logging
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

#: transient responses, retried with a backoff
RETRY_STATUS_CODES = (429, 500, 502, 503, 504)
#: number of retries after the initial request
RETRIES = 3
#: `backoff_factor` seconds between the retries, doubled after every retry
BACKOFF_FACTOR = 0.5
#: seconds to wait for a response
TIMEOUT = 30

_SESSION: requests.Session | None = None


class _TimeoutHTTPAdapter(HTTPAdapter):
    """Adapter which applies a default timeout to every request."""

    def __init__(self, timeout: int = TIMEOUT, **kwargs: Any) -> None:
        """Store the timeout used for requests without an explicit one."""
        self.timeout = timeout
        super().__init__(**kwargs)

    def send(
        self,
        request: requests.PreparedRequest,
        stream: bool = False,
        timeout: Any = None,
        verify: Any = True,
        cert: Any = None,
        proxies: Any = None,
    ) -> requests.Response:
        """Send the request, applying the default timeout if none is given."""
        if timeout is None:
            timeout = self.timeout
        return super().send(
            request,
            stream=stream,
            timeout=timeout,
            verify=verify,
            cert=cert,
            proxies=proxies,
        )


def get_session() -> requests.Session:
    """Get the shared session for the web service queries.

    The session retries the transient responses in `RETRY_STATUS_CODES` and
    times out after `TIMEOUT` seconds.

    Returns:
        The shared session, created on first use.
    """
    global _SESSION
    if _SESSION is None:
        retry = Retry(
            total=RETRIES,
            backoff_factor=BACKOFF_FACTOR,
            status_forcelist=RETRY_STATUS_CODES,
            allowed_methods=frozenset({"GET"}),
            # the status is checked by the caller, do not raise here
            raise_on_status=False,
        )
        adapter = _TimeoutHTTPAdapter(max_retries=retry)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        _SESSION = session

    return _SESSION


class WebserviceError(OSError):
    """Raised when a web service query cannot be answered.

    Covers the unreachable service, the error response and the response which
    is not JSON, i.e., everything a caller handles the same way: fall back to
    the cached content, see `pymetadata.cache.read_json_cache_fallback`.
    """


def get_json(url: str) -> Any:
    """Query a url and return the parsed JSON response.

    Args:
        url: url to query

    Returns:
        The parsed JSON response.

    Raises:
        WebserviceError: if the service cannot be reached, answers with a
            status other than 200, or does not answer with JSON
    """
    logger.debug("Query: %s", url)
    try:
        response = get_session().get(url)
    except requests.RequestException as err:
        # no network, DNS failure, timeout, too many retries, ...
        raise WebserviceError(f"Service is not reachable for '{url}': {err}") from err

    if response.status_code != 200:
        raise WebserviceError(f"'{response.status_code}' response for: '{url}'")

    try:
        return response.json()
    except ValueError as err:
        # a service which is down answers with an HTML error page
        raise WebserviceError(f"Response for '{url}' is not JSON: {err}") from err
