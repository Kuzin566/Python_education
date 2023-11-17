from typing import Callable


def get_math_func(operation: str) -> Callable[[int, int], str]:
    def add(a: int, b: int) -> str:
        return str(a + b)

    def subtract(a: int, b: int) -> str:
        return str(a - b)

    if operation == "+":
        return add
    elif operation == "-":
        return subtract


h = get_math_func(operation='+')
print(h('2', 2))
#
# def colors():
#     a = 1
#     b = 2
#
#     def print_a():
#         print(a)
#
#     def print_b():
#         print(b)
#
#     print_a()
#     print_a()
#
#
# colors()
