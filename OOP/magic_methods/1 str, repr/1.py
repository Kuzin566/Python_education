class Lion:

    def __init__(self, name):
        self.name = name
        self.id = None

    def __repr__(self):
        return f"The object Lion - {self.name}, id : {self.id}"

    # def __str__(self):
    #     return f"Lion - {self.name}"

    def pri(self):
        print(self)


    # def __str__(self):




a = Lion('Bob')
print(a)
a.pri()
# print(str(a))
