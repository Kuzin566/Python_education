from OOP.magic_methods.polifornizm_python.rectangle import Rectangle, Square



rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.get_area())
print(rect2.get_area())

sq1 = Square(5)
sq2 = Square(7)
print(sq1.get_area())
print(sq2.get_area())

figures = [rect1, rect2, sq2, sq1]
for figure in figures:
    print(figure, figure.get_area())