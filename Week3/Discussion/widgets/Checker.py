"""Checks if there is a winner in a tic tac toe board"""

WINS = ("cross", "circle")


def Checker(cells):
    """Checker functionality

    Go through each check and return the winner if there is one.

    Args:
        cells: Matrix of Cell objects in the board.

    Returns:
        String of the winner, "none" if there is no winner or "tie" if there is a tie.
    """

    # Get the imageType property of each cell.
    board = [[cell.image.imageType for cell in row] for row in cells]

    winState = checkRow(board)
    if winState in WINS:
        return winState

    winState = checkCol(board)
    if winState in WINS:
        return winState

    winState = checkDiag(board)
    if winState in WINS:
        return winState

    winState = checkAntiDiag(board)
    if winState in WINS:
        return winState

    winState = checkTie(board)
    if winState == "tie":
        return winState

    return None


def checkTie(board):
    """Checks for ties

    Loop through each row. If there are empty cells, then there is no tie.
    This is because that means that there are possible moves left.
    So there is no tie.
    This method should be called after all other check methods,
    as it also means that there is no winner.

    Args:
        board: Matrix of "cross" or "circle".

    Returns:
        "tie" if there is a tie, "none" if there is no tie.
    """

    winState = "tie"
    for row in board:
        if len([cell for cell in row if cell != "empty"]) != len(row):
            winState = "none"
            break

    return winState


def checkRow(board):
    """Checks for row wins

    Loop through rows, check if the row is only of one type.

    Args:
        board: Matrix of "cross" or "circle".

    Returns:
        The winner if there is one, "none" if there is no winner.
    """

    winState = "none"
    for row in board:
        if row.count("cross") == len(row):
            winState = "cross"
            break
        elif row.count("circle") == len(row):
            winState = "circle"
            break

    return winState


def checkCol(board):
    """Checks for column wins

    Tilt the matrix 90 degrees and use the row checker.
    This is because if the columns are the rows, the row checker would work.
    This enables reusability.

    Args & Returns:
        Same as other checks.
    """

    winState = checkRow(zip(*board))
    return winState


def checkDiag(board):
    """Checks for diagonal wins

    Get the diagonal by looping through the matrix.
    If the diagonal is only of one type, then there is a winner.

    Args & Returns:
        Same as other checks.
    """

    winState = "none"

    diag = []
    for diagNum in range(len(board)):
        cell = board[diagNum][diagNum]
        diag.append(cell)

    if diag.count("cross") == len(diag):
        winState = "cross"
    elif diag.count("circle") == len(diag):
        winState = "circle"

    return winState


def checkAntiDiag(board):
    """Checks for anti-diagonal wins

    Similar to checkCol, but we reverse the matrix instead of turning it.

    Args & Returns:
        Same as other checks.
    """

    winState = checkDiag([[elem for elem in reversed(row)] for row in board])
    return winState
