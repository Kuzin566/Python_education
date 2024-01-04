class Person:
    def __init__(self, name):
        self._name = name

    @property
    def my_name(self):
        print("Get name")
        return self._name

    @my_name.setter
    def my_name(self, value):
        print("Set name")
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        self._name = value

    @my_name.deleter
    def my_name(self):
        print("Delete name")
        del self._name
