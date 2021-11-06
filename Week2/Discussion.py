"""
  CSC101 - Programming Assignment 1
  7.4 - The Fan class
  Sean X.
  Nov. 2nd, 2021

  Summary
    This program creates a Fan class that represents a fan. It then tests the Fan class by creating two fans and turning one on, the other off. After, it prints out the information of the fans.
"""


class Fan:
    """A class that represents a fan"""

    SLOW: int = 1
    MEDIUM: int = 2
    FAST: int = 3

    def __init__(
        self,
        speed: int = SLOW,
        radius: float = 5.0,
        color: str = "blue",
        on: bool = False,
    ) -> None:
        """Constructor, set properties according to passed arguments"""
        self.__speed: int = speed
        self.__radius: float = radius
        self.__color: str = color
        self.__on: bool = on

    @property
    def speed(self) -> int:
        """Get the speed"""
        return self.__speed

    @speed.setter
    def speed(self, speed: int) -> None:
        """Set the speed"""
        if speed in (self.SLOW, self.MEDIUM, self.FAST):
            self.__speed = speed
        else:
            raise ValueError("Invalid speed")

    @property
    def on(self) -> int:
        """Get the on state"""
        return self.__on

    @on.setter
    def on(self, on: bool) -> None:
        """Set the on state"""
        if type(on) != bool:
            raise ValueError("Invalid on state")
        else:
            self.__on = on

    @property
    def radius(self) -> float:
        """Get the radius"""
        return self.__radius

    @radius.setter
    def radius(self, radius: float) -> None:
        """Set the radius"""
        if type(radius) != float:
            raise ValueError("Invalid radius")
        else:
            self.__radius = radius

    @property
    def color(self) -> str:
        """Get the color"""
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        """Set the color"""
        if type(color) != str:
            raise ValueError("Invalid color")
        else:
            self.__color = color


fan1: Fan = Fan(speed=Fan.FAST, radius=10, color="yellow")
fan1.on = True

fan2: Fan = Fan(speed=Fan.MEDIUM, radius=5)
fan2.on = False

for fanProperty in ("speed", "radius", "color", "on"):
    fanPropertyName = fanProperty if fanProperty != "on" else "on state"
    print(f"Fan1's {fanPropertyName} is {getattr(fan1, fanProperty)}")
    print(f"Fan2's {fanPropertyName} is {getattr(fan2, fanProperty)}")
