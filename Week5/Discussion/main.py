"""
  CS102 - Programming Assignment 5
  14.3 - Count the occurrences of each keyword
  Sean X.
  Nov. 22th, 2021

  Summary
    This program will count the occurrences of each keyword in a text file.
"""
from keywords import keywords


KeywordCount = dict[str, int]


def countKeywords(fileText: str) -> KeywordCount:
    """Count the occurrences of each keyword

    Arguments:
        fileText: The text content of the file

    Returns:
        The dictionary of keywords (key) and their counts (value)
    """

    return {keyword: fileText.count(keyword) for keyword in keywords}


def prettyPrintDict(toPrettyPrint: KeywordCount, skipZero: bool = False) -> str:
    """Pretty print a dictionary

    Arguments:
        toPrettyPrint: The dictionary to pretty print

    Returns:
        The pretty printed dictionary
    """

    return "\n".join(
        f"{keyword}: {toPrettyPrint[keyword]}"
        for keyword in dict(
            sorted(
                (
                    {key: value for key, value in toPrettyPrint.items() if value != 0}
                    if skipZero
                    else toPrettyPrint
                ).items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
    )


def main(fileName: str) -> None:
    """Run the app

    Arguments:
        fileName: The name of the file to read
    """

    with open(fileName, "r") as file:
        fileText: str = file.read()

    keywordCount: KeywordCount = countKeywords(fileText)

    print(
        prettyPrintDict(
            keywordCount,
            input("Remove keywords with zero occurrences? ").lower()
            in ("yes", "ok", "y"),
        )
    )
