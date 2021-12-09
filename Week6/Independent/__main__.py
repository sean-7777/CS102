#!/usr/bin/env python3.10-64
"""Launch program and check Python version."""
from sys import version_info as version

MIN_PYTHON_VERSION = (3, 10, 0)
CURRENT_VERSION = (version.major, version.minor, version.serial)
formatVer = lambda ver: ".".join(map(str, ver))
if not CURRENT_VERSION >= MIN_PYTHON_VERSION:
    print(
        "\n".join(
            line.center(120)
            for line in [
                f"\033[31m",
                f"Python version {formatVer(MIN_PYTHON_VERSION)} required or higher.",
                f"You are running Python version {formatVer(CURRENT_VERSION)}.",
                f"Try using the command 'py -{formatVer(MIN_PYTHON_VERSION[:2])}' or 'py{formatVer(MIN_PYTHON_VERSION[:2])}' to run this program.",
                f"\033[0m",
            ]
        )
    )
    exit(1)
else:
    print(
        f"\033[32mScript successfully started with Python version {formatVer(CURRENT_VERSION)}.\033[0m".center(
            120
        )
    )

#####################################################################################
#####################################################################################

numbers = (
    input("Enter two numbers seperated by a comma: ")
    .strip()
    .replace(" ", "")
    .split(",")
)[:2]

if len(numbers) < 2:
    print("\033[91m\t\t\tYou must enter two numbers.\033[0m")
    exit(1)

from main import gcd

print(gcd(*map(float, numbers)))
