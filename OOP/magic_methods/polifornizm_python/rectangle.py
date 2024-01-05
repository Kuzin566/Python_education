"""Полиморфизм происходит от греческих слов poly (много) и morphism (формы),
что в буквальном значении полиморфизм означает множество форм. Это означает,
что одна и та же сущность (операция, функция, метод, объект)
может использоваться для разных типов. Это делает программирование
более интуитивным и простым.
В Python есть разные способы определения полиморфизма.
Давайте посмотрим на эти варианты."""


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Rectangle {self.a}x{self.b}"

    def get_area(self):
        return self.a * self.b


class Square:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Square {self.a}x{self.a}"

    def get_area(self):
        return self.a * self.a
