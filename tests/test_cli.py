import subprocess
import sys

from actions import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "actions", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
