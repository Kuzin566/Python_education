# class Square:
#     def __init__(self, s):
#         self._side = s
#         self.__area = None
#
#     @property
#     def side(self):
#         return self._side
#
#     @side.setter
#     def side(self, value):
#         self._side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if not self.__area:
#             print('Считаем')
#             self.__area = self.side ** 2
#         return self.__area
#
#
# a = Square(5)
# print(a.area)
# a.side = 7
#
# print(a.area)


class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__square = None

    @property
    def area(self):
        if not self.__square:
            self.__square = self._length * self._width
        return self.__square


r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976
print('Good')
