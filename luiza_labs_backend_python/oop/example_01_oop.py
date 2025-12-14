class Bicycle:
    def __init__(self, color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    @staticmethod
    def honk():
        print("Trim trim...")

    @staticmethod
    def stop():
        print("Stop bicyle...")
        print("Bicycle stoped!")

    @staticmethod
    def run():
        print("Vrummmm...")

    @staticmethod
    def change_gear(gear_number):
        print(f"Gear shifted to {gear_number}")

    # def __str__(self):
    # return f"Bicycle: color = {self.color}, model = {self.model}, year = {self.year}, value = {self.value}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


bicycle1 = Bicycle(color="Silver", model="JNA 1", year=2001, value=150)
bicycle1.honk()
bicycle1.run()
bicycle1.stop()
print(bicycle1.color, bicycle1.model, bicycle1.year, bicycle1.value)

# When we make this call:
# bicycle1.honk is equivalent to Bicycle.honk(bicycle1)

bicycle2 = Bicycle(color="Green", model="Monark", year=1995, value=50)
print(bicycle2)
