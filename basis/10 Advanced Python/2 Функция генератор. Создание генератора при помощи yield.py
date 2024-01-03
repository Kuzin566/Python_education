# def f():
#     return [43, 65, 32]
#
#
# print(f())


# def genf():
#     s = 7
#     for i in [43, 65, 32]:
#         yield i
#         print(s)
#         s = s * 10 + 7
#
#
# s = genf()
# print(next(s))
# print(next(s))
# print(next(s))


# def fact(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr = pr * i
#         yield pr
#
#
# s = fact(10)
#
# for i in fact(10):
#     print(i)


# def gen_squares(n: int):
#     for i in range(1, n + 1):
#         yield i ** 2
#
#
# for i in gen_squares(5):
#     print(i)
# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(5))

def gen_fibonacci_numbers(n):
    if n == 1:
        yield 0
    if n == 2:
        yield 1
    yield gen_fibonacci_numbers(n - 1) + gen_fibonacci_numbers(n - 2)
#
#
for i in gen_fibonacci_numbers(5):
    print(i)
