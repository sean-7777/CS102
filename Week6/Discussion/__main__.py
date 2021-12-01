#!/usr/bin/env python3.10-64
"""Launch program and check Python version."""
from random import randint
from sys import setrecursionlimit
from sys import version_info as version
from typing import Callable

from main import compute as compute_formula
from main import format_fraction

VersionTuple = tuple[int, int, int]
MIN_PYTHON_VERSION: VersionTuple = (3, 0, 0)
CURRENT_VERSION: VersionTuple = (version.major, version.minor, version.serial)

if not CURRENT_VERSION >= MIN_PYTHON_VERSION:
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
    setrecursionlimit(10 ** 6)
    inputI: str = input("Enter the variable i: ")
    if not inputI.isdecimal():
        i: int = randint(1, 10)
        print(f"i is not a number. i is now {i}")
    else:
        i: int = int(inputI)

    print(format_fraction(compute_formula(i)))
