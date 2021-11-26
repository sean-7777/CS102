"""
  CS102 - Programming Assignment 5
  14.11 - Count cons
  Sean X.
  Nov. 26th, 2021

  Summary
    ...
"""
from collections.abc import Iterable, Iterator
from itertools import islice, zip_longest

from vowels import CONSONANTS, VOWELS

LetterCount = dict[str, int]


def countInText(text: str, thingsToCount: Iterable[str]) -> LetterCount:
    """Count how many of each thing of a iterable in a text

    Example:
        >>> countInText("Hello, world!", "aeiou")
        {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}

    Arguments:
        text: The text to count things in
        thingsToCount: The things to count

    Returns:
        A dictionary of the things and their counts.

    """
    return {
        thing: text.count(thing) + text.count(thing.lower()) for thing in thingsToCount
    }


def formatCount(count: LetterCount) -> str:
    """Format a count as a string

    Example:
        >>> formatCount({'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0})
        a: 0         e: 1         i: 0         o: 2         u: 0

    Arguments:
        count: The count to format

    Returns:
        A formatted string of the count

    """

    sortedCount: LetterCount = dict(sorted(count.items(), key=lambda x: x[0]))

    return "\n".join(
        "".join(f"{key}: {sortedCount[key]:<10}" if key else "" for key in keys)
        for keys in zip_longest(*dictChunks(sortedCount, 5))
    )


def dictChunks(data: dict, chunkSize: int) -> list[dict]:
    """Split an iterable into chunks

    Example:
        >>> from random import random
        >>> dictChunks({i:random() for i in range(10)}, 3)
        [{0: 0.4950452935165729, 1: 0.37176037802037387, 2: 0.4053725520860376},
        {3: 0.562429505157191, 4: 0.9727553186830946, 5: 0.710450115392605},
        {6: 0.03368645934187631, 7: 0.4962253937467972, 8: 0.478604295660349},
        {9: 0.5809890831921646}]

    Arguments:
        iterable: The iterable to split
        chunkSize: The size of each chunk

    Returns:
        An iterable of chunks

    Raises:
        ValueError: If chunkSize is not a positive integer
    """

    if not chunkSize > 0:
        raise ValueError("Chunk size must be a positive integer")

    if len(data) <= chunkSize:
        return [{key: value} for key, value in data.items()]

    iterableData: Iterator[str] = iter(data.keys())
    chunks: list[dict] = []
    for _ in range(0, len(data), chunkSize):
        chunks.append({key: data[key] for key in islice(iterableData, chunkSize)})

    return chunks


def main(fileName: str) -> None:
    with open(fileName, "r") as file:
        text: str = file.read()
        consonantCount: LetterCount = countInText(text, CONSONANTS)
        vowelCount: LetterCount = countInText(text, VOWELS)

    print(f"{'VOWELS':=^75}")
    print(formatCount(vowelCount))
    print(f"{'CONSTANTS':=^75}")
    print(formatCount(consonantCount))
