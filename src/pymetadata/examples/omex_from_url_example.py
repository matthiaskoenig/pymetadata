from pymetadata.console import console
from pymetadata.omex import Omex

omex_url = "https://github.com/matthiaskoenig/canagliflozin-model/releases/download/0.7.0/canagliflozin_model.omex"
omex = Omex.from_url(omex_url)
console.print(omex)
