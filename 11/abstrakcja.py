from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def sides(self): # abstract method
        pass

class Square(Shape):

    def sides(self):
        print("I have 4 sides")

class Triangle(Shape):

    def sides(self):
        print("I have 3 sides")


T = Triangle()
T.sides()

S = Square()
S.sides()