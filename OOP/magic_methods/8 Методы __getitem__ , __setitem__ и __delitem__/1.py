class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError("Индекс за границами нашей коллекции")

    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):
            self.values[key - 1] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff)
            self.values[key - 1] = value
        else:
            raise IndexError("Индекс за границами нашей коллекции")

    def __delitem__(self, key):
        if 1 <= key <= len(self.values):
            del self.values[key - 1]
        else:
            raise IndexError("Индекс за границами нашей коллекции")


v1 = Vector(1, 2, 434, 32)
# print(v1)

v2 = Vector(3, 43, 5, 56, 45, 3423)

# v2[1] = 10
print(v2[6])
v2[10] = 10
print(v2)

# del v2[1]
# print(v2[1])
