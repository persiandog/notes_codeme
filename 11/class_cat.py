#stwórz klasę kot
#kot ma imię i wiek
#kot może wykonać akcję "pij mleko"

#utwórz metodę generującą 5 kotów
import random

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def drink_milk(self):
        print("drinking milk")
    def __str__(self):
        return f"My cat {self.name} is {self.age}"

def generate_cats():
    names = ['mruczek', 'miauczek', 'filemon', 'kot w butach', 'szarik']
    for name in names:
        temp_age = random.randint(2, 10)
        cat = Cat(name.capitalize(), temp_age)
        print(Cat)

generate_cats()

