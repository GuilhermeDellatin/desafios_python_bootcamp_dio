class BankAccount:
    def __init__(self, value, branch):
        self._value = value
        self.branch = branch

    def deposit(self, amount):
        self._value += amount

    def withdraw(self, amount):
        self._value -= amount

    def show_value(self):
        return self._value

bank = BankAccount(value=100, branch="0001")
bank.deposit(100)
bank.deposit(100)
#print(bank._value) For convention do not make this
print(bank.branch)
print(bank.show_value())