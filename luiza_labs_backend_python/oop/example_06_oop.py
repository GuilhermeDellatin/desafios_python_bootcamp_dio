class Bird:
    @staticmethod
    def fly():
        print("Flying...")

class Sparrow(Bird):
    def fly(self):
        super().fly()

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly.")

# Polymorphism concept
def flight_plan(obj):
    obj.fly()

sparrow = Sparrow()
ostrich = Ostrich()

flight_plan(sparrow)
flight_plan(ostrich)