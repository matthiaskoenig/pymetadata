"""Reading a COMBINE archive directly from a url.

The archive is downloaded to a temporary file and read from there, so no local
copy has to be managed.

Run with `python examples/omex/omex_from_url.py`.
"""

from pymetadata import log
from pymetadata.console import console
from pymetadata.omex import Omex

OMEX_URL: str = (
    "https://github.com/matthiaskoenig/canagliflozin-model/releases/download/"
    "0.7.0/canagliflozin_model.omex"
)

if __name__ == "__main__":
    log.enable_rich_logging()
    omex = Omex.from_url(OMEX_URL)
    console.print(omex)

    for entry in omex.entries_by_format("sbml"):
        console.print(f"SBML: {entry.location}")
