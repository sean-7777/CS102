"""Displays a tic tac toe board element"""
from os import path
import tkinter as tk

# Use the tk.button not ttk.button because
# ttk.button doesn't support disabling border.
class Cell(tk.Button):
    """Displays a tic tac toe board element

    Attributes:
        parent: The parent of the cell.
    """

    def __init__(self, parent, onClick):
        """Initializes the cell

        Set the click command.
        Set the image.

        Args:
            parent: The parent of the cell.
            onClick: The function to call when the cell is clicked.
        """

        self.parent = parent
        super().__init__(
            master=self.parent,
            borderwidth=0,
            command=lambda: onClick(self),
        )
        self.setImage("empty")

    def setImage(self, image):
        """Sets the image of the cell

        Args:
            image: The image to set.
        """

        # TL;DR Images need to be stored in a variable.
        # The image is set the self.image because
        # if I did self.configure(image=EmptyImage()),
        # it wouldn't work.
        if image == "cross":
            self.image = CrossImage()
        elif image == "circle":
            self.image = CircleImage()
        elif image == "empty":
            self.image = EmptyImage()
        self.configure(image=self.image)


class CellImage(tk.PhotoImage):
    """Displays a cell's image"""

    @staticmethod
    def getSrc(img):
        """Gets the image source path

        Get the folder the file is in. (/widgets)
        Get the parent folder of that. (/)
        Get the assets folder. (/assets)
        Get the image file source. (/assets/img.png)

        Args:
            img: The image to get the source path of.

        Returns:
            The source path of the image.
        """

        rootFolder = path.dirname(path.dirname(__file__))
        source = path.join(rootFolder, "assets", f"{img}.png")
        return source

    def __init__(self, img):
        """Displays the image

        Args:
            imgSrc: The image to display.
        """

        super().__init__(file=img, width=100, height=100)


class CrossImage(CellImage):
    """Cross Image"""

    imageType = "cross"

    def __init__(self):
        """Initializes the image"""

        super().__init__(img=CellImage.getSrc("cross"))


class CircleImage(CellImage):
    """Circle Image"""

    imageType = "circle"

    def __init__(self):
        """Initializes the image"""

        super().__init__(img=CellImage.getSrc("circle"))


class EmptyImage(CellImage):
    """Blank image with border"""

    imageType = "empty"

    def __init__(self):
        """Initializes the image"""

        super().__init__(img=CellImage.getSrc("empty"))
