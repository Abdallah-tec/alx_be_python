import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    length = 0
    width = 0
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    radius = 0
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

    