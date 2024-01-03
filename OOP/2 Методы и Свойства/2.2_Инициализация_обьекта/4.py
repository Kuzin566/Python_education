class Zebra():
    count = 0
    def __init__(self):
        self.white = "Полоска белая"
        self.black = "Полоска черная"

    def which_stripe(self, count=1):
        self.count = self.count + count
        if self.count % 2 == 0:
            print(f"{self.black}")
        else:
            print(f"{self.white}")


a = Zebra()
print(a.count)
a.which_stripe()
a.which_stripe()
a.which_stripe()
a.which_stripe()