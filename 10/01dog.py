"""1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
atrybuty: imię, kolor sierści, rasę
metody: szczekaj, machaj ogonem"""

class Dog:
    def __init__(self, name, coat, breed):
        self.name = name
        self.coat = coat
        self.breed = breed
    def bark(self):
        print("bork")
obj_dog = Dog('forest', 'white', 'mix')

print(obj_dog.name)
obj_dog.bark()