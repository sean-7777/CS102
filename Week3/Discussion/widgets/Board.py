"""Displays a tic tac toe board"""
import tkinter as tk
from tkinter import ttk

from .Cell import Cell


class Board(ttk.Frame):
    """Displays a tic tac toe board

    Attributes:
        parent: The parent widget.
        cells: A matrix of Cell objects.
    """

    def __init__(self, parent, onClick, gridSize=3):
        """Initializes the board

        Args:
            parent: The parent widget.
            onClick: The function to call when a cell is clicked.
            gridSize: The size of the grid.
        """

        self.parent = parent
        super().__init__(master=self.parent)

        self.cells = []
        for row in range(gridSize):
            self.cells.append([])

            for col in range(gridSize):
                self.cells[row].append(Cell(parent=self, onClick=onClick))
                self.cells[row][col].grid(row=row, column=col)

            self.rowconfigure(row, minsize=100)
            self.columnconfigure(row, minsize=100)

    def reset(self):
        """Reset the board

        Set each cell to a empty image.
        """

        for row in self.cells:
            for cell in row:
                cell.setImage("empty")
