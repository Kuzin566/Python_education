class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


class Otrezok:
    def __init__(self, point_1: int | float, point_2: int | float):
        self.x_1: int | float = point_1
        self.x_2: int | float = point_2

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.x_2 - self.x_1)


t = Otrezok(10, 5.5)

print(abs(t))


