"""Создайте класс  Fruit, который имеет:
метод __init__, который устанавливает значения атрибутов name и price: название и цена фрукта
методы сравнения. Здесь вы сами решаете какие магические методы
реализовывать, главное чтобы фрукты могли сравниваться с числами и другими фруктами по цене. Смотрите тесты ниже в коде"""
from functools import total_ordering


# Напишите определение класса Fruit
@total_ordering
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        """=="""
        print('__eq__ call')
        if isinstance(other, Fruit):
            other = other.price
        return self.price == other

    def __lt__(self, other):
        """<"""
        print('__lt__ call')
        if isinstance(other, Fruit):
            other = other.price
        return self.price < other

    def __le__(self, other):
        """<="""
        return self == other or self < other


# Ниже код для проверки методов класса Fruit

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')
