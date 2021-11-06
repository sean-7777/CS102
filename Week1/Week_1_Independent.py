"""
  CSC101 - Programming Assignment 1
  11.10 - Largest rows and columns
  Sean X.
  Oct. 25, 2021

  Summary
    Generates a random 4x4 matrix of 0s and 1s, and finds the largest rows and columns.
"""
import typing as t
from random import randint

# NOTE Logging stuff, I log to a file so the terminal isn't cluttered when debugging
# Logger src: https://gist.github.com/sean-7777/f19ad9f40c14b83f6015c1a0d02f310e
# from logging import shutdown as logShutdown
# import Logger

# logger = Logger.createLogger(__import__("os").path.basename(__file__))

Row = t.List[int]
Matrix = t.List[Row]


def generateMatrix() -> Matrix:
    """Generate a 4x4 matrix of 0 or 1 randomly."""
    return [[randint(0, 1) for _ in range(4)] for _ in range(4)]


def formatMatrix(matrix: Matrix) -> str:
    """Format a matrix for printing."""
    return "\n".join([" ".join(map(str, row)) for row in matrix])


def getLargest(matrix: Matrix) -> str:
    """Return the rows and columns with the largest sum. (most 1s)"""
    MaxTypeSingle = t.Tuple[int, t.List[int], int]  # DOC (sum of row, row, sun of row)
    MaxType = t.List[MaxTypeSingle]

    def getLargestIn(matrix: Matrix) -> MaxType:
        """Loop through each row of a matrix and find if it is greater than the previous rows."""
        maxRows: MaxType = []
        for rowNum, row in enumerate(matrix):
            rowSum: int = sum(row)
            toAdd: MaxTypeSingle = (rowNum, row, rowSum)

            # DOC First row, so maxRows is empty, so we just add the first row and skip iteration
            if rowNum == 0:
                maxRows.append(toAdd)
                continue

            # DOC If the current row is greater than the row in maxRows, replace it, as it is wrong
            # If it is the same, add to maxRows, as we want to see all the rows
            greatestSum: int = sum(maxRows[0][1])
            if rowSum > greatestSum:
                maxRows = [toAdd]
            elif sum(row) == greatestSum:
                maxRows.append(toAdd)
        return maxRows

    def generateMaxTxt(maxs: MaxType, name: str) -> str:
        """Helper function to generate text for the result of the parent function."""
        multiple: t.Callable[[str, str], str] = (
            lambda yes, no: yes if len(maxs) > 1 else no
        )  # NOTE quick function to not have to do if len(maxs) > 1 every time

        return "\n".join(
            [
                (
                    f"The {name}{multiple('s', '')} that {multiple('have', 'has')} "
                    f"the greatest sum {multiple('are', 'is')}:"  # Generate heading text
                ),
                *[
                    (
                        f"\tIndex {elem[0]} ({name} {elem[0] + 1}), "
                        f"contents {formatMatrix([elem[1]])}, sum {elem[2]}"
                    )
                    for elem in maxs
                ],  # DOC Loop through each greatest row and display it.
            ]
        )

    maxRows: MaxType = getLargestIn(matrix)
    maxCols: MaxType = getLargestIn(list(map(list, zip(*matrix))))

    return f"{generateMaxTxt(maxRows, 'row')}\n{generateMaxTxt(maxCols, 'column')}"


def main() -> None:
    """Run the program."""
    matrix: Matrix = generateMatrix()
    print(formatMatrix(matrix))
    print(getLargest(matrix))


main()
# NOTE More logging stuff
# Logger.stopFileLogger(logger)
# logShutdown()
