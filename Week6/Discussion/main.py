from fractions import Fraction
from typing import Callable


def compute(i: int) -> Fraction:
    """Compute using the formula in the description

    Compute with the variable i, this formula:
    1 + ½ + ⅓ + ¼ + ... + ¹⁄ᵢ

    Args:
        i: The variable i in the formula

    Returns:
        The computed result of the formula
    """

    return 1 + compute_helper(2, Fraction(0, 1), i + 1)


def compute_helper(i: int, cur: Fraction, target: int) -> Fraction:
    return cur if i == target else compute_helper(i + 1, cur + Fraction(1, i), target)


def format_fraction(fraction: Fraction) -> str:
    """Format the fraction with Unicode super/subscript numbers

    Args:
        fraction: The fraction to format

    Returns:
        The formatted fraction
    """

    # fmt: off
    symbols: dict[str, dict[int, str] | str] = {
        "numerator": {
            0: "⁰", 1: "¹", 2: "²",
            3: "³", 4: "⁴", 5: "⁵",
            6: "⁶", 7: "⁷", 8: "⁸",
            9: "⁹",
        },
        "denominator": {
            0: "₀", 1: "₁", 2: "₂",
            3: "₃", 4: "₄", 5: "₅",
            6: "₆", 7: "₇", 8: "₈",
            9: "₉",
        },
        "slash": "⁄",
    }
    # fmt: on

    number: int = fraction.numerator // fraction.denominator
    remainder: int = fraction.numerator - number * fraction.denominator
    subSupScript: Callable[[int, str], str] = lambda n, l: "".join(
        symbols[l][int(s)] for s in list(str(n))
    )

    return f"{number}{subSupScript(remainder, 'numerator')}{symbols['slash']}{subSupScript(fraction.denominator, 'denominator')}"
