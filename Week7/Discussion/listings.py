"""Compute primes"""
from math import sqrt


def listing4(n: int) -> int:
    """Compute primes with listing 16.4"""

    primeCount: int = 0
    number: int = 2

    while number <= n:
        isPrime = True

        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                isPrime = False
                break

        if isPrime:
            primeCount += 1

        number += 1

    return primeCount


def listing5(n: int) -> int:
    """Compute primes with listing 16.5"""

    primes: list[int] = []
    primeCount: int = 0
    number: int = 2
    squareRoot: int = 1

    while number <= n:
        isPrime = True

        if squareRoot * squareRoot < number:
            squareRoot += 1

        k = 0
        while k < len(primes) and primes[k] <= squareRoot:
            if number % primes[k] == 0:
                isPrime = False
                break
            k += 1

        if isPrime:
            primes.append(number)
            primeCount += 1

        number += 1

    return primeCount


def listing6(n: int) -> int:
    """Compute primes with listing 16.6"""

    primes: list[int] = []

    for i in range(n + 1):
        primes.append(True)

    k = 2
    while k <= n / k:
        if primes[k]:
            for i in range(k, int(n / k) + 1):
                primes[k * i] = False
        k += 1

    return primes.count(True)
