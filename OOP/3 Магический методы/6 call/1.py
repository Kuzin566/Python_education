class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print(f'init object : {self}')

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Наш экземпляр вызывался  {self.counter} раз')

    def average(self):
        return self.summa / self.length


c = Counter()
c(3, 4, 5)
c(1, 6)
print(c.summa)
print(c.length)
print(c.average())
