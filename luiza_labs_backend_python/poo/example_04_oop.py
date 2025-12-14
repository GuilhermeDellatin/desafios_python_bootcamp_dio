class Animal:
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

class Mammal(Animal):
    def __init__(self, fur_color, **kwargs):
        super().__init__(**kwargs)
        self.fur_color = fur_color

    #def __str__(self):
        #return "Mammal"

class Bird(Animal):
    def __init__(self, beak_color, **kwargs):
        super().__init__(**kwargs)
        self.beak_color = beak_color

    #def __str__(self):
        #return "Bird"

class Lion(Mammal):
    pass

class Cat(Mammal):
    pass

class Dog(Mammal):
    pass

class Platypus(Mammal, Bird):
    def __init__(self, number_of_legs, fur_color, beak_color):
        super().__init__(number_of_legs=number_of_legs, fur_color=fur_color, beak_color=beak_color)
        print(Platypus.__mro__)
        #print(Platypus.mro())

    #def __del__(self):
        #return "Platypus"

cat = Cat(number_of_legs=4, fur_color='Black')
print(cat)

platypus = Platypus(number_of_legs=4, fur_color='Brown', beak_color = "orange")
print(platypus)

