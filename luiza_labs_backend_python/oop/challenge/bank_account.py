from luiza_labs_backend_python.oop.challenge.history import History


class BankAccount:
    def __init__(self, client, account_number, branch="0001"):
        self._client = client
        self._account_number = account_number
        self._branch = branch
        self._balance = 0
        self._history = History()