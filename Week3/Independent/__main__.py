from main import main
from typing import Tuple

sides: Tuple[float, float, float] = (
    float(input("Enter the first side's length: ")),
    float(input("Enter the second side's length: ")),
    float(input("Enter the third side's length: ")),
)
color: str = input("Enter the color: ")
filled: bool = bool(int(input("Enter 1 if the triangle is filled: ")))
print("-" * 80)
main(sides, color, filled)
