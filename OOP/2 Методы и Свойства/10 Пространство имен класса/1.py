# class MyClass:
#     class_attribute = "I am a class attribute"
#
#     def __init__(self):
#         self.instance_attribute = "I am an instance attribute"
#
#     @staticmethod
#     def change(new_value):
#         MyClass.class_attribute = new_value
#
#
# example_1 = MyClass()
# example_2 = MyClass()
# example_3 = MyClass()
#
# example_1.change("Class attribute modified")
#
# print(example_2.class_attribute)
# print(example_3.class_attribute)


class Container:
    items = []
    a = "2"

    def add_item(self, value):
        self.items.append(value)

    def primer(self):
        self.a += '1'


box1 = Container()
box1.add_item(2)
box1.add_item(4)
box1.primer()
box2 = Container()
box2.add_item(5)
box2.add_item(7)
box2.primer()
print(Container.items)
print(Container.a)
