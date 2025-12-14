from abc import ABC, abstractmethod


class Transaction(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @classmethod
    def register(cls, bank_account):
        pass