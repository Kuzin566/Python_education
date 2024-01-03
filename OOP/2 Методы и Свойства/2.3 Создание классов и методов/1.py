
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"



d = Dog("Nick", 18)
print(d.description())
print(d.speak("Privet vika"))