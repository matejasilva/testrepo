"""Tests for the unified utils CLI entrypoint."""

import subprocess
import sys

import pytest

from utils import __version__


def _run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "utils", *args],
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.mark.parametrize("flag", ["--version", "-v"])
def test_cli_version_flags(flag):
    proc = _run_cli(flag)
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == f"utils {__version__}"
