"""
__eq__(self, other)	отвечает за сравнение на равенство с помощью оператора ==
__ne__(self, other)	отвечает за сравнение на неравенство с помощью оператора !=
__lt__(self, other)	отвечает за сравнение на меньше с помощью оператора <
__le__(self, other)	отвечает за сравнение на меньше или равно с помощью оператора <=
__gt__(self, other)	отвечает за сравнение на больше с помощью оператора >
__ge__(self, other)	отвечает за сравнение на больше или равно с помощью оператора >="""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b


    def __eq__(self, other):
        """=="""
        print('__eq__ call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        """<"""
        print('__lt__ call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        """<="""
        return self == other or self < other


v = Rectangle(1, 4)
r = Rectangle(1, 3)
# print(v != r)
print(v >= r)
