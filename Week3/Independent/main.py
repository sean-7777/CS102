""""
Draw the UML diagrams for the classes Triangle and GeometricObject.
Implement the Triangle class. Write a test program that prompts the user to
enter the three sides of the triangle, a color, and 1 or 0 to indicate whether the triangle is filled.
The program should create a Triangle object with these sides and
set the color and filled properties using the input. The program should display the
triangle’s area, perimeter, color, and True or False to indicate whether the triangle is filled or not.
"""
import typing as t
from math import sqrt


class GeometricObject:
    """A geometry object

    This is a template for a geometric object.

    Attributes:
        color: The color of the object.
        filled: Whether the object is filled.
    """

    def __init__(self, color: str = "green", filled: bool = True) -> None:
        """Initialize the attributes of a GeometricObject.

        Args:
            color: The color of the shape.
            filled: Whether the shape is filled.
        """

        self.__color, self.__filled = color, filled

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, newColor: str) -> None:
        self.__color = newColor

    @property
    def filled(self) -> bool:
        return self.__filled

    @filled.setter
    def filled(self, newFilled: bool) -> None:
        self.__filled = newFilled

    def __str__(self) -> str:
        return f"Color: {self.color}, Filled: {self.filled}"


class Triangle(GeometricObject):
    """A triangle."""

    def __init__(
        self,
        side1: float,
        side2: float,
        side3: float,
        color: str = "green",
        filled: bool = True,
    ) -> None:
        """Initialize the attributes of a Triangle."""

        super().__init__(color, filled)
        self.__side1, self.__side2, self.__side3 = side1, side2, side3

    @property
    def side1(self) -> float:
        return self.__side1

    @property
    def side2(self) -> float:
        return self.__side2

    @property
    def side3(self) -> float:
        return self.__side3

    @property
    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    @property
    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

    def __str__(self) -> str:
        return f"Side 1: {self.side1}, Side 2: {self.side2}, Side 3: {self.side3}"


def main(sides: t.Tuple[float, float, float], color: str, filled: bool):
    """Test the triangle"""
    triangle: Triangle = Triangle(*sides, color, filled)

    triangleProp: str
    for triangleProp in ("area", "perimeter", "color", "filled"):
        print(f"{triangleProp.capitalize()}: {getattr(triangle, triangleProp)}")
