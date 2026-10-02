"""Helpers for writing files.

Files are written atomically by writing a temporary file next to the target
and replacing the target with it. `tempfile` creates the temporary file
readable by its owner only, so the permissions of a regular new file have to be
set before the temporary file replaces the target.
"""

import os
from pathlib import Path


def regular_file_mode() -> int:
    """Get the permissions of a regular new file, i.e., `0o666` minus the umask.

    Returns:
        The permission bits for a new file.
    """
    # the umask can only be read by setting it
    umask = os.umask(0o022)
    os.umask(umask)
    return 0o666 & ~umask


def set_regular_file_mode(path: Path) -> None:
    """Give a temporary file the permissions of a regular new file.

    Args:
        path: path of the file
    """
    path.chmod(regular_file_mode())
