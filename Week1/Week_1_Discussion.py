"""
  CSC101 - Programming Assignment 1
  11.14 - Explore Matrix
  Sean X.
  Oct. 25, 2021

  Summary
    This program generates a matrix of 0s and 1s, and then checks if the matrix has the same values in rows, columns, and diagonals.
"""
import typing as t
from random import randint


def generateMatrix(size: int) -> list:
    matrix: list = []  # init matrix
    for rowNum in range(size):
        matrix.append([])  # loop through row count and add the row

        for elem in range(size):
            random: int = randint(0, 1)
            matrix[rowNum].append(random)  # add random number to row
    return matrix


# check if the matrix has the same values in rows, columns, and diagonals
def checkEq(matrix: list) -> t.List[str]:

    # check if a matrix has the same values 1, or 0 in the rows in the given list
    def isSame(toCheck: list, checkType: str) -> t.List[str]:
        # list which says which rows are the same
        sames: t.List[t.Union[int, None]] = []
        for row in toCheck:
            if row.count(1) == len(row):  # if row is all something, add to sames list
                sames.append(1)
            elif row.count(0) == len(row):
                sames.append(0)
            else:
                sames.append(None)  # if not all 1 or 0, add None to sames list

        samesStr: t.List[str] = []
        if sames.count(None) == len(sames):  # if all None, then no rows are the same
            samesStr.append(f"No {checkType} are the same")
        else:
            samesStr.append(checkType.capitalize())  # add the header
            for sameNum in range(len(sames)):
                if sames[sameNum] != None:  # if it is not None, add the str to the list
                    samesStr.append(
                        f"\t{checkType[:-1].capitalize()} {sameNum + 1} is all {sames[sameNum]}."
                    )
        return samesStr

    ans: t.List[str] = []
    # check rows
    ans.extend(isSame(matrix, "rows"))

    # check cols
    # change rows into cols using zip function
    cols: list = list(zip(*matrix))
    ans.extend(isSame(cols, "columns"))

    # check diagonals
    # get diagonals
    diagonal1: list = []
    diagonal2: list = []
    for i in range(len(matrix)):
        diagonal1.append(matrix[i][i])
        diagonal2.append(matrix[i][-(i + 1)])
    ans.extend(isSame([diagonal1, diagonal2], "diagonals"))
    return ans


def main() -> None:
    # generate matrix
    matrixSize: int = int(input("Enter the size of matrix you would like: "))
    matrix: list = generateMatrix(matrixSize)

    # print matrix
    print("Matrix:")
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

    # print sames
    sames: t.List[str] = checkEq(matrix)
    print("\n".join(sames))


main()
