"""Run the main file"""
from main import main
from tkinter import Tk

boardSize = input("Enter the board size: ")
if not boardSize.isnumeric():
    print("Invalid option. Defaulting to 3.")
    boardSize = 3
else:
    boardSize = int(boardSize)

root = Tk()
main(root, boardSize)
