"""Run the program"""
from sys import version_info as version
from typing import Callable

from main import createTimers

VersionTuple = tuple[int, int, int]
MIN_PYTHON_VERSION: VersionTuple = (3, 0, 0)
CURRENT_VERSION: VersionTuple = (version.major, version.minor, version.serial)

if CURRENT_VERSION < MIN_PYTHON_VERSION:
    formatVer: Callable[[VersionTuple], str] = lambda ver: ".".join(
        str(elem) for elem in ver
    )
    print(
        f"""\033[91m
\t\t\tPython version {formatVer(MIN_PYTHON_VERSION)} required or higher.
\t\t\tYou are running Python version {formatVer(CURRENT_VERSION)}.
    \033[0m"""
    )
    exit(1)
else:
    createTimers()
