
class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, object):
        if isinstance(object, Point):
            c = ((self.x - object.x)**2 + (self.y - object.y)**2)**0.5
            return c
        else:
            print("Передана не точка")

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4,6)
print(p1.get_distance(10))

