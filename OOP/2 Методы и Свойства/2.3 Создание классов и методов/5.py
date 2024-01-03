
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        s = self.width * self.height
        return s

    def perimeter(self):
        p = (self.width + self.height) * 2
        return p

r1 = Rectangle(2, 3)
assert r1.width == 2
assert r1.height == 3
assert r1.perimeter() == 10
assert r1.area() == 6
