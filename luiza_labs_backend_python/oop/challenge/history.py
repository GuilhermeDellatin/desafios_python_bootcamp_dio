from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from transaction import Transaction


class TransactionRecord(TypedDict):
    type: str
    value: float
    date: str


class History:
    """Stores the transaction history of an account."""

    def __init__(self) -> None:
        self._transactions: list[TransactionRecord] = []

    @property
    def transactions(self) -> tuple[TransactionRecord, ...]:
        return tuple(self._transactions)

    def add_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now(tz=UTC).isoformat(timespec="seconds"),
            }
        )
