class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point_slots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)
p = Point_slots(3, 4)
print(s.__sizeof__(), s.__dict__.__sizeof__())
print(p.__sizeof__())
