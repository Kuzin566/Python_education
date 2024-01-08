class CoordinateValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')

    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner_class={owner_class}')


class Point:
    x = CoordinateValue()
    y = CoordinateValue()


# Point.x
# p = Point()
# p.x
# p.x = 100


class StringValidation:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner, name):
        print(f'__set_name__ called: owner={owner}, attr_name={name}')
        self.attribute_name = name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            key = '_' + self.attribute_name
            return getattr(instance, key, None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
        if len(value) < self.min_length:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                             f'быть не меньше {self.min_length} символов')
        key = '_' + self.attribute_name
        setattr(instance, key, value)


class Person:
    name = StringValidation(5)
    last_name = StringValidation(7)


p = Person()
try:
    p.name = 'Alexsdf'
except ValueError as ex:
    print(ex)


