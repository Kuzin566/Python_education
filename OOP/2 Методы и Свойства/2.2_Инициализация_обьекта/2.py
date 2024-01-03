
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{brand} {model}"

laptop1 = Laptop('Iphone', 'Lg', 100)
laptop2 = Laptop('Lg', "A2", 500)
print(laptop1.laptop_name)
print(laptop2.laptop_name)