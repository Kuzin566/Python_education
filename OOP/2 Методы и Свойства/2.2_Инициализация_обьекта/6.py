class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old"


bro = Person('Nikolay', 34)
assert bro.age == 34
assert bro.name == 'Nikolay'
assert bro.greet() == 'Hello, my name is Nikolay, and I am 34 years old'
