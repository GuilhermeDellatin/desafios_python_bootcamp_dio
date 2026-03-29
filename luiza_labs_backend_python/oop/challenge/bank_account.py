from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from history import History

if TYPE_CHECKING:
    from bank_client import BankClient


@dataclass(frozen=True, slots=True)
class OperationResult:
    """Represents the outcome of a banking operation."""

    success: bool
    message: str


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

    def withdraw(self, value: float) -> OperationResult:
        if value <= 0:
            return OperationResult(
                success=False,
                message="Error: The withdrawal amount must be greater than zero.",
            )

        if value > self._balance:
            return OperationResult(success=False, message="Error: Insufficient funds.")

        self._balance -= value
        return OperationResult(success=True, message="Withdrawal successful!")

    def deposit(self, value: float) -> OperationResult:
        if value <= 0:
            return OperationResult(
                success=False,
                message="Error: The deposit amount must be greater than zero.",
            )

        self._balance += value
        return OperationResult(success=True, message="Deposit successful!")


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

    def withdraw(self, value: float) -> OperationResult:
        withdrawals_count = sum(
            1
            for transaction in self.history.transactions
            if transaction["type"] == "Withdrawal"
        )

        if value > self.limit:
            return OperationResult(
                success=False,
                message="Error: Amount exceeds per-withdrawal limit.",
            )

        if withdrawals_count >= self.withdrawal_limit:
            return OperationResult(
                success=False,
                message="Error: Maximum number of withdrawals reached.",
            )

        return super().withdraw(value)

    def __str__(self) -> str:
        holder = getattr(self.client, "name", "N/A")
        return f"Agency:\t{self.branch}\nAccount:\t{self.number}\nHolder:\t{holder}"
