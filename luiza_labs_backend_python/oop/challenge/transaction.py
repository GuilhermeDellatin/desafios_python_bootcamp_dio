from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bank_account import BankAccount


class Transaction(ABC):
    """Interface for financial transactions."""

    @property
    @abstractmethod
    def value(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def register(self, account: BankAccount) -> None:
        raise NotImplementedError


class Deposit(Transaction):
    """Handles deposit transactions."""

    def __init__(self, value: float) -> None:
        self._value = value

    @property
    def value(self) -> float:
        return self._value

    def register(self, account: BankAccount) -> None:
        success = account.deposit(self.value)
        if success:
            account.history.add_transaction(self)


class Withdrawal(Transaction):
    """Handles withdrawal transactions."""

    def __init__(self, value: float) -> None:
        self._value = value

    @property
    def value(self) -> float:
        return self._value

    def register(self, account: BankAccount) -> None:
        success = account.withdraw(self.value)
        if success:
            account.history.add_transaction(self)
