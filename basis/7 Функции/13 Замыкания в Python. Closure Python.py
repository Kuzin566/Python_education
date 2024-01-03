from typing import Callable


def adder(value: int) -> Callable[[int], int]:
    def inner(a):
        return value + a
    return inner


a2 = adder(2)
print(a2(5))
print(a2(57))


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


q = counter()
r = counter()
print(q())
q()
print(q())
print(r())
