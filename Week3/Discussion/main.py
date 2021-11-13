"""
  CS102 - Programming Assignment 3
  12.5 - Tic Tac Toe
  Sean X.
  Nov. 9th, 2021

  Summary
    A tic tac toe game.
"""
from tkinter import ttk
import tkinter.messagebox as tkMsg

import widgets


class App(ttk.Frame):
    """The themed tkinter app wrapper.

    This is necessary because the themed tkinter widgets
    use a different color than the regular tkinter,
    so I have to have a themed tkinter widget wrapper for the background color.

    Attributes:
        isXTurn: A boolean that determines which player's turn it is.
        parent: The parent tkinter widget, usually the root window.
        toplevel: The top level tkinter widget, usually the root window.
        board: The board widget.
    """

    isXTurn = True

    def __init__(self, parent, gridSize):
        """Initialize the app

        Name the tic tac toe window, add the board widget,
        and add margins around the board.

        Args:
            parent: The parent tkinter widget, usually the root window.
        """

        self.parent = parent
        super().__init__(master=self.parent)

        self.toplevel = self.winfo_toplevel()
        self.toplevel.title("Tic Tac Toe")

        self.board = widgets.Board(parent=self, onClick=self.onClick, gridSize=gridSize)
        self.board.grid(column=0, columnspan=5, row=0, rowspan=5)

        for i in range(5):
            self.columnconfigure(i, minsize=100)
            self.rowconfigure(i, minsize=100)

    def onClick(self, cell):
        """Handle click events

        Place the appropriate symbol in the clicked cell.
        Update the current player turn.
        Check for a winner.

        Args:
            cell: The cell that was clicked.
        """

        if cell.image.imageType != "empty":
            return

        if self.isXTurn:
            cell.setImage("cross")
        else:
            cell.setImage("circle")

        self.isXTurn = not self.isXTurn
        self.isWinner()

    def isWinner(self):
        """Check for winner

        Decide if a player has won. If so, display a win message box and ask to reset the board.
        If the reset is declined, close the window.
        """

        winner = widgets.Checker(cells=self.board.cells)
        if winner:
            if winner == "cross":
                tkMsg.showinfo(title="Winner", message="Cross wins!", parent=self)
                self.reset()
            elif winner == "circle":
                tkMsg.showinfo(title="Winner", message="Circles wins!", parent=self)
                self.reset()
            elif winner == "tie":
                tkMsg.showinfo(title="Tie", message="It is a tie!", parent=self)
                self.reset()

    def reset(self):
        """Asks to reset

        Asks the user if they want to reset the board.
        Reset the board or close the window if the user declines.
        """

        if tkMsg.askyesno(title="Restart", message="Do you want to restart?"):
            self.board.reset()
        else:
            self.toplevel.destroy()


def main(root, gridSize):
    """Create the app and run it

    Create the app and pack it into the root.
    Create minium and maximum window size.
    Add weight.

    Args:
        root: The root tkinter widget, usually the root window.
    """

    app = App(parent=root, gridSize=gridSize)
    # Use grid method, because it works with columnconfigure and rowconfigure.
    app.grid(column=0, row=0)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.update()
    width, height = root.winfo_width(), root.winfo_height()
    root.minsize(width, height)
    root.maxsize(width * 3, height * 3)

    root.mainloop()
