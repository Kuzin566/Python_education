class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0


p1 = Point(0, 1)
p2 = Point(1, 0)
# print(bool(p1))
print(bool(p2))

assert True is bool(p1), 'ебала'


class Person:
    def __init__(self, name):
        self.name = name


p1 = Person('Gena')
print(not p1)
