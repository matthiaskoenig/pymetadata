"""Time reading and writing COMBINE archives with `pymetadata.omex`.

Run with `uv run python scripts/omex_timing.py`. Every archive of
`tests/data/omex` is read with `Omex.from_omex`, and written back with
`Omex.to_omex` without a change. A table of the median and the fastest of
several runs is printed in milliseconds, which is where the figures of the
release notes come from.
"""

import argparse
import statistics
import tempfile
import time
from collections.abc import Callable
from pathlib import Path

from pymetadata.omex import Omex

FIXTURES: Path = Path(__file__).parent.parent / "tests" / "data" / "omex"
RUNS: int = 7


def measure(function: Callable[[], object], runs: int) -> tuple[float, float]:
    """Time a function, after one run which is not counted.

    Args:
        function: the function to call
        runs: the number of timed runs

    Returns:
        The median and the minimum of the runs in milliseconds.
    """
    function()
    times: list[float] = []
    for _ in range(runs):
        start = time.perf_counter()
        function()
        times.append((time.perf_counter() - start) * 1000)
    return statistics.median(times), min(times)


def time_archive(
    path: Path, runs: int
) -> tuple[int, tuple[float, float], tuple[float, float]]:
    """Time the read and the write of one archive.

    Args:
        path: the `.omex` file
        runs: the number of timed runs

    Returns:
        The number of entries, and (median, minimum) of the read and of the write
        in milliseconds.
    """
    omex = Omex.from_omex(path)
    with tempfile.TemporaryDirectory() as tmp_dir:
        target = Path(tmp_dir) / "out.omex"
        read = measure(lambda: Omex.from_omex(path), runs)
        write = measure(lambda: omex.to_omex(target), runs)
    entries = len(omex.manifest.entries)
    omex.close()
    return entries, read, write


def main() -> None:
    """Print the timing table of all fixtures."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", type=int, default=RUNS, help="timed runs per figure")
    runs = parser.parse_args().runs

    print(f"median (min) of {runs} runs in ms")
    print(f"{'archive':<30} {'KiB':>6} {'entries':>8} {'read':>16} {'write':>16}")
    for path in sorted(FIXTURES.glob("*.omex")):
        entries, read, write = time_archive(path, runs)
        print(
            f"{path.name:<30} {path.stat().st_size // 1024:>6} {entries:>8} "
            f"{read[0]:>8.2f} ({read[1]:>5.2f}) {write[0]:>8.2f} ({write[1]:>5.2f})"
        )


if __name__ == "__main__":
    main()
