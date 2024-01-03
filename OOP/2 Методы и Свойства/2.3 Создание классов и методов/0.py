from math import sqrt
class Point():
    list_point = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_point.append(self.x)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0,0)

    def print_point(self):
        print(f"Точка с координатами ({self.x},{self.y})")

    def calc_distance(self, anoter_point):
        if not isinstance(anoter_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Point")
        else:
            return sqrt((self.x - anoter_point.x)**2 + (self.y - anoter_point.y)**2)


p = Point(6,0)
p2 = Point(0, 8)
print(p.calc_distance(p2))
# print(p2.list_point)