
class Constructor:

    def add_atribute(self, name, value):
        setattr(self, name, value)

    def display(self):
        print(self.__dict__)


c = Constructor()
c.add_atribute("color", "red")
c.display()

