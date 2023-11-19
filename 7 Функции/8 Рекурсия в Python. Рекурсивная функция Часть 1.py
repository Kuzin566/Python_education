# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x + 1)
#         print(x)
#
#
# rec(1)


# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x - 1) * x
#
#
# print(fact(5))

"""Fibonacci"""


# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(5))

# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     print(s[1:-1])
#     return palindrom(s[1:-1])


# def print_from(n) -> None:
#     if n >= 1:
#         print(n)
#         print_from(n - 1)
#
# print_from(7)
