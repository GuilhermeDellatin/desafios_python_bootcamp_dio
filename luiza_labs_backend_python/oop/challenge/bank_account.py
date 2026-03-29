from __future__ import annotations

from typing import TYPE_CHECKING

from history import History

if TYPE_CHECKING:
    from bank_client import BankClient


class BankAccount:
    """Base class for bank accounts."""

    def __init__(self, number: int, client: BankClient) -> None:
        self._balance: float = 0.0
        self._number: int = number
        self._branch: str = "0001"
        self._client: BankClient = client
        self._history: History = History()

    @classmethod
    def new_account(cls, client: BankClient, number: int) -> BankAccount:
        return cls(number, client)

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def number(self) -> int:
        return self._number

    @property
    def branch(self) -> str:
        return self._branch

    @property
    def client(self) -> BankClient:
        return self._client

    @property
    def history(self) -> History:
        return self._history

    def withdraw(self, value: float) -> bool:
        if value <= 0:
            print("\nError: The withdrawal amount must be greater than zero.")
            return False

        if value > self._balance:
            print("\nError: Insufficient funds.")
            return False

        self._balance -= value
        print("\nWithdrawal successful!")
        return True

    def deposit(self, value: float) -> bool:
        if value <= 0:
            print("\nError: The deposit amount must be greater than zero.")
            return False

        self._balance += value
        print("\nDeposit successful!")
        return True


class CheckingAccount(BankAccount):
    """Bank account with withdrawal limits."""

    def __init__(
        self,
        number: int,
        client: BankClient,
        limit: float = 500.0,
        withdrawal_limit: int = 3,
    ) -> None:
        super().__init__(number, client)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit

    @classmethod
    def new_account(cls, client: BankClient, number: int) -> CheckingAccount:
        return cls(number, client)

    @property
    def limit(self) -> float:
        return self._limit

    @property
    def withdrawal_limit(self) -> int:
        return self._withdrawal_limit

    def withdraw(self, value: float) -> bool:
        withdrawals_count = sum(
            1
            for transaction in self.history.transactions
            if transaction["type"] == "Withdrawal"
        )

        if value > self.limit:
            print("\nError: Amount exceeds per-withdrawal limit.")
            return False

        if withdrawals_count >= self.withdrawal_limit:
            print("\nError: Maximum number of withdrawals reached.")
            return False

        return super().withdraw(value)

    def __str__(self) -> str:
        holder = getattr(self.client, "name", "N/A")
        return (
            f"Agency:\t{self.branch}\n"
            f"Account:\t{self.number}\n"
            f"Holder:\t{holder}"
        )
