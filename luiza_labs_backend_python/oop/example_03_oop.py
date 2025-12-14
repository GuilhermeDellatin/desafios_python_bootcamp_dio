# Simple Inheritance

class Vehicle:
    def __init__(self, color, license_plate, number_of_wheels):
        self.color = color
        self.license_plate = license_plate
        self.number_of_wheels = number_of_wheels

    @staticmethod
    def turn_on():
        print("Turn on the motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

class Motorcycle(Vehicle):
    def __init__(self, color, license_plate, number_of_wheels):
        super().__init__(color, license_plate, number_of_wheels)

class Car(Vehicle):
    def __init__(self, color, license_plate, number_of_wheels):
        super().__init__(color, license_plate, number_of_wheels)

class Truck(Vehicle):
    def __init__(self, color, license_plate, number_of_wheels, is_loaded):
        super().__init__(color, license_plate, number_of_wheels)
        self.is_loaded = is_loaded

    def verify_is_loaded(self):
        print(f"{'Yes' if self.is_loaded else 'No'}, is loaded!")

motorcycle = Motorcycle(color="Black", license_plate="abc-1234", number_of_wheels=2)
motorcycle.turn_on()

car = Car(color="Dark Gray", license_plate="abc-5678", number_of_wheels=4)
car.turn_on()

truck = Truck(color="Blue", license_plate="abc-9012", number_of_wheels=8, is_loaded=True)
truck.turn_on()
truck.verify_is_loaded()

print(motorcycle)
print(car)
print(truck)