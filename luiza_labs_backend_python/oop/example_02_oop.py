class Dog:
    def __init__(self, name, color, awake=True):
        print("Initializing Class...")
        self.name = name
        self.color = color
        self.awake = awake

    def song(self):
        print("Auau")

    def __del__(self):
        print("Removing Class Instance...")


dog = Dog(name="Dog", color="caramel")
dog.song()


def create_dog():
    dog2 = Dog(name="Dog2", color="caramel", awake=False)
    print(dog2.name)

create_dog()

print("Hello World!")
del dog
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
