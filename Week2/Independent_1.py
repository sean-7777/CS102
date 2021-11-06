"""
  CSC101 - Programming Assignment 1
  7.3 - The Account class
  Sean X.
  Nov. 2nd, 2021

  Summary
    Creates a class to represents a bank account. Then tests the class.
"""


class Account:
    """A class to represent a bank account"""

    def __init__(
        self, id: int = 0, balance: float = 100.00, interest: float = 0
    ) -> None:
        self.__id, self.__balance, self.__annualInterestRate = id, balance, interest

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id: int = id

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, balance: float) -> None:
        self.__balance: float = balance

    def deposit(self, amount: float = 15.0) -> None:
        self.__balance += amount

    def withdraw(self, amount: float = 15.0) -> None:
        self.__balance -= amount

    @property
    def annualInterestRate(self) -> float:
        return self.__annualInterestRate

    @annualInterestRate.setter
    def annualInterestRate(self, annualInterestRate: float) -> None:
        self.__annualInterestRate: float = annualInterestRate

    @property
    def monthlyInterest(self) -> float:
        return self.monthlyInterestRate * self.__balance

    @property
    def monthlyInterestRate(self) -> float:
        return self.__annualInterestRate / 100 / 12


def test() -> None:
    """
    Test function.
    """
    account = Account(id=1122, balance=20000.00, interest=4.5)
    account.withdraw(2500)
    account.deposit(3000)
    print(f"Account ID: {account.id}")
    print(f"Account Balance: {account.balance}")
    print(f"Account Monthly Interest Rate: {account.monthlyInterestRate}")
    print(f"Account Monthly Interest: {account.monthlyInterest}")


if __name__ == "__main__" and __debug__:
    test()
