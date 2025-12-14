from wsgiref.util import request_uri


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_birthdate(cls, month, day, year, name):
        age = 2025 - year
        print(f"Birthdate of {name} at {month}-{day}-{year}.")
        return cls(name=name, age=age)

    @staticmethod
    def is_legal_age(age):
        return age >= 18

person = Person.create_birthdate(month=12, day=31, year=1990, name="Testing")
print(person.name, person.age)

print(Person.is_legal_age(person.age))
print(Person.is_legal_age(17))