#!/usr/bin/env python3.10-64
"""Launch program and check Python version."""
from sys import version_info as version, argv

from main import main

MIN_PYTHON_VERSION = (3, 0, 0)
CURRENT_VERSION = (version.major, version.minor, version.serial)

if not CURRENT_VERSION >= MIN_PYTHON_VERSION:
    formatVer = lambda ver: ".".join(str(elem) for elem in ver)
    print(
        f"""\033[91m
\t\t\tPython version {formatVer(MIN_PYTHON_VERSION)} required or higher.
\t\t\tYou are running Python version {formatVer(CURRENT_VERSION)}.
    \033[0m"""
    )
    exit(1)
else:
    if len(argv) > 1:
        main(argv[1])
    else:
        main(input("Enter the name of the file to use: "))
