class Marks:
    def __init__(self, values):
        self.values = values
        self.index = 0


    def __iter__(self):
        print('call iter')
        self.index = 0
        return self


    def __next__(self):
        print('call next marks')
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        letter = self.values[self.index]
        self.index += 1
        return letter




class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks


    def __iter__(self):
        print('call iter')
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print('call next Student')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


m = Marks([3, 4, 5, 6, 3])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)


class Iterator:
    def __init__(self, text):
        self.text = text.upper()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.text[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


phrase = Iterator('Qwerty')
it_1 = iter(phrase)
it_2 = iter(phrase)
for i in it_1:
    print(i)
for i in it_1:
    print(i)
for i in it_2:
    print(i)
