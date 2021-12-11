"""
  CS102 - Programming Assignment 7
  16.10 - Execution time for prime numbers
  Sean X.
  Monday, Dec. 8, 2021

  Summary
    ...
"""
from datetime import timedelta
from threading import Thread
from timeit import Timer
from typing import Callable

from listings import listing4, listing5, listing6

ONE_MILLION: int = 1000000


def listingWrapper(listing: Callable[[int], int], n: int) -> Callable[[], int]:
    """Create a function to run a listing"""
    return lambda: listing(n)


def threadWrapper(timer: Timer, name: str, n: int) -> None:
    """Template to execute a timer in a thread"""
    print(f"Started {name} with {n}")
    time = timer.timeit(1)
    print(formatTime(time, f"run {name} with n={n}"))


def formatTime(seconds: float, what: str) -> str:
    """Format a time in seconds to a string"""
    return f"It took {timedelta(seconds=seconds)} to {what}."


def createTimers():
    """Create a list of timers and run them in threads"""
    for listing in [listing4, listing5, listing6]:
        for n in [
            8 * ONE_MILLION,
            10 * ONE_MILLION,
            12 * ONE_MILLION,
            14 * ONE_MILLION,
            16 * ONE_MILLION,
            18 * ONE_MILLION,
        ]:
            thread = Thread(
                target=threadWrapper,
                args=(Timer(listingWrapper(listing, n)), listing.__name__, n),
            )
            thread.start()
