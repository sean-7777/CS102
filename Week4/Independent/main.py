"""
  CS102 - Programming Assignment 4
  13.5 - Replace text
  Sean X.
  Nov. 16th, 2021

  Summary
    Replace all occurrences of a string with another string in a file.
"""
from typing import TextIO


def prompt(promptStr: str) -> str:
    """Get a input.

    Returns:
        The result of the prompt.
    """

    return input(f"Enter {promptStr}: ")


def replaceInFile(fileName: str, toReplace: str, toReplaceWith: str) -> None:
    """Replace all occurrences of string in a file with another string.

    Args:
        fileName: The name of the file to read.
        toReplace: The string to replace.
        toReplaceWith: The string to replace with.
    """

    with open(fileName, "r+t") as file:
        file: TextIO
        text: str = file.read()
        replaced: str = text.replace(toReplace, toReplaceWith)

        file.seek(0)
        file.write(replaced)


def main() -> None:
    """Main function."""

    fileName: str = prompt("file name")
    toReplace: str = prompt("string to replace")
    toReplaceWith: str = prompt("string to replace with")

    replaceInFile(fileName, toReplace, toReplaceWith)
