from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bank_account import BankAccount
    from transaction import Transaction


class BankClient:
    """Base class for banking clients."""

    def __init__(self, address: str) -> None:
        self.address = address
        self.accounts: list[BankAccount] = []

    def perform_transaction(
        self, account: BankAccount, transaction: Transaction
    ) -> None:
        transaction.register(account)

    def add_account(self, account: BankAccount) -> None:
        self.accounts.append(account)


class Individual(BankClient):
    """Represents a natural person client."""

    def __init__(
        self, cpf: str, name: str, birth_date: str, address: str
    ) -> None:
        super().__init__(address)
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
