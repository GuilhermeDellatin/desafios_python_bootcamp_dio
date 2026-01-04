class BankClient:
    def __init__(self, address):
        self._address = address
        self.accounts = []

    @staticmethod
    def make_transaction(bank_account, transaction):
        transaction.register(bank_account)

    def add_bank_account(self, bank_account):
        self.accounts.append(bank_account)