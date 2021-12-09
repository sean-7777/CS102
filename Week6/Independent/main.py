"""
  CS102 - Programming Assignment 6
  15.5 - Compute greatest common divisor using recursion
  Sean X.
  Thursday, December 2, 2021

  Summary
    Compute the greatest common divisor of two numbers using recursion.
"""

Number = int | float


def gcd(x: Number, y: Number) -> Number:
    """Compute the greatest common factor of two numbers

    Arguments:
        x: The first number
        y: The second number

    Returns:
        The greatest common factor of x and y
    """

    return y if x % y == 0 else gcd(y, x % y)
