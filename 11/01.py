"""Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że
rzeczywiście korzystają z klas rodziców."""

from abc import ABC, abstractmethod

class Animals:
    @abstractmethod
    def show_name(self): #abstract method
        pass

class Mammals(Animals):
    name = True
    drink_milk = True
    spine = True
    ectothermic = False

    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)

class Cat(Mammals):
    def __init__(self, c_name, age):
        self.name = c_name
        self.age = age
    def drink_milk(self):
        print("drinking milk")
    def show_name(self):
        print(self.name)
obj_cat = Cat('Mruczek', 5)

class Dog(Mammals):
    def __init__(self, d_name, coat, breed):
        self.name = d_name
        self.coat = coat
        self.breed = breed
    def bark(self):
        print("bork")
    def show_name(self):
        print(self.name)
obj_dog = Dog('Forest', 'white', 'mix')

class Human(Mammals):
    def __init__(self, h_name, language, nationality):
        self.name = h_name
        self.language = language
        self.nationality = nationality
    def show_name(self):
        print(self.name)
obj_human = Human('Magda', 'PL', 'PL')

print(obj_cat.name, obj_dog.name, obj_human.name)

print(obj_cat.spine)