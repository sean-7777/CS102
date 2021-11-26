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

    # Sort by the letter because we are using sets, and sets are unordered
    # so even though it looks like it is in order when it is created, it is not
    sortedCount: LetterCount = dict(sorted(count.items(), key=lambda x: x[0]))

    # First, we split the dictionary into 5 bits. This way, we will only have 5 lines, making the output easier to read and more compact.
    # Then, we use zip_longest to be able to iterate over multiple things at once.
    # The zip_longest function is equivalent to zip, but instead of stopping at the shortest iterable, it will stop at the longest iterable,
    # and fill in the rest of the iterables with None.
    # When we loop, the keys variable will be a iterable containing the nth keys for all the dictionaries on the nth loop.
    # We then loop through the keys, and for each key, we get the value from the dictionary.
    # We then format the value as a string. In the string format we use the String Format Mini-Language which lets us align the data to form columns.
    # In the code, we left align within 10 characters.
    # There is also a check which checks if key is a truthy value, if it is not, the it provides a blank string. 
    # This is because we might have left over data which is not a full length dictionary from dictChunks and zip_longest will insert a NoneType to make the a equal length. 
    # If it is None, that means that there is no data, so we provide a empty string. 
    # Then, we join the strings with no seperator, then joining them with a newline. 
    return "\n".join(
        "".join(f"{key}: {sortedCount[key]:<10}" if key else "" for key in keys)
        for keys in zip_longest(*dictChunks(sortedCount, 5))
    )


def dictChunks(data: dict, chunkSize: int) -> list[dict]:
    """Split an iterable into chunks

    Splits a dictionary into multiple sections with the given size.
    Left over items are put into their own dictionary.
    If the size is greater or equal to the length of the data,
    the length is assumed to be 1.

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

    # If size is greater than data size, do this, essentially size=1
    # Each key/value gets its own chunk
    if len(data) <= chunkSize:
        return [{key: value} for key, value in data.items()]

    # Create an iterator with the keys of the data
    iterableData: Iterator[str] = iter(data.keys())
    # Create a list to store the chunks
    chunks: list[dict] = []
    # Loop a amount of times enough to use all the data in the chunks
    for _ in range(0, len(data), chunkSize):
        # The islice function returns a section of the given iterable with length given
        # So by calling the islice function here, we get the data for the chunk
        # The rest of the dictionary comprehension is just to obtain the data
        # You might think that we would get the same data each time,
        # but we don't, because we are using an iterator
        # So when the first chunk is created, the data for the first chunk will be gone
        # And when the second chunk is created, we will get different data,
        # as there is no first chunk anymore
        chunks.append({key: data[key] for key in islice(iterableData, chunkSize)})

    return chunks


def main(fileName: str) -> None:
    with open(fileName, "r") as file:
        text: str = file.read()
        consonantCount: LetterCount = countInText(text, CONSONANTS)
        vowelCount: LetterCount = countInText(text, VOWELS)

    # Title centered within 75 characters and = filling whitespace
    print(f"{'VOWELS':=^75}")
    print(formatCount(vowelCount))
    print(f"{'CONSTANTS':=^75}")
    print(formatCount(consonantCount))
