"""Shared rich console.

All output of the package goes through this console, which is also used by the
logging handler in `pymetadata.log`. It records what is printed, so the output
of a script can be exported afterwards.

```python
from pymetadata.console import console

console.print(omex)
console.rule("Section", style="white")
```
"""

from rich import pretty
from rich.console import Console
from rich.theme import Theme

pretty.install()
custom_theme = Theme(
    {
        "success": "green",
        "info": "blue",
        "warning": "orange3",
        "error": "red",
    }
)

console = Console(record=True, theme=custom_theme)
