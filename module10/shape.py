from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod

    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius #calsulate and return the area of the circle


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length #calculate and return area of the squarec


circle_1 = Circle(7)

square_1 = Square(10)

print(circle_1.area())
print(square_1.area())

