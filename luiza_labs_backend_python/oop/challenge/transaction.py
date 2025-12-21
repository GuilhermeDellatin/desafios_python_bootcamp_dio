from abc import ABC, abstractmethod


class Transaction(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @classmethod
    def register(cls, bank_account):
        pass

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, bank_account):
        success = bank_account.deposit(self._value)
        if success:
            bank_account.history.add_transaction(self)

class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, bank_account):
        success = bank_account.withdraw(self._value)
        if success:
            bank_account.history.add_transaction(self)