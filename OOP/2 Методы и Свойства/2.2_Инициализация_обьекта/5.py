class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        full_name = f"{self.last_name} " + f"{self.first_name}"
        return full_name

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


p1 = Person("Kuzin", "Nick", 18)
print(p1.full_name())
p1.is_adult()
