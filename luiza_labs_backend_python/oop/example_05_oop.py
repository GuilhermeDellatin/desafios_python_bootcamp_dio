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

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = 0
        #del self._x


foo = Foo(10)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)

class Person:
    def __init__(self, name, birthday):
        self._name = name
        self._birthday = birthday

    @property
    def name(self):
        return self._name

    #Its more Pythonic turns name in public name instead _name...
    #@name.setter
    #def name(self, new_name):
        #self._name = new_name

    @property
    def age(self):
        _current_year = 2025
        return _current_year - self._birthday

    # No Pythonic code
    def get_name(self):
        return self._name

    # No Pythonic code
    def get_age(self):
        return self.age

person = Person("John", birthday=1985)
print(f"Name: {person.name} \tAge: {person.age}")