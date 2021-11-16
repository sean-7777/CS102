"""
  CS102 - Programming Assignment 4
  13.8 - Encrypt files
  Sean X.
  Nov. 15th, 2021

  Summary
    Encrypt a file by adding 5 to every byte.
"""
import typing as t
from itertools import chain


def getFileNames() -> tuple[str, str]:
    """Get the file names to encrypt and output to.

    Returns:
        A tuple of the input and output file names.
    """

    return (input("Enter the name of the file to encrypt: ") or "decrypted.txt"), (
        input("Enter the name of the file to output to: ") or "encrypted.txt"
    )


def encrypt(inputFileName: str, outputFileName: str) -> None:
    """Encrypt a file

    Loop through each character in the file and add 5 to the digit represented by the character.
    chain.from_iterable method is used to convert the matrix of characters, the file into a single list.

    Args:
        inputFileName: The name of the file to encrypt
        outputFileName: The name of the file to output to
    """

    inputFile: t.TextIO = open(inputFileName, mode="rt")
    outputFile: t.TextIO = open(outputFileName, mode="wt")

    for char in chain.from_iterable(inputFile):
        outputFile.write(chr(ord(char) + 5))


def main() -> None:
    encrypt(*getFileNames())
