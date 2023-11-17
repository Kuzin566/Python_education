# h = lambda a=1, b=2, c=3: print(a + b + c)
#
# r = lambda x: x ** 2
#
# h()


# def f(x):
#     if x > 0:
#         return 'positive'
#     else:
#         return 'negative'

# t = lambda x: 'positive' if x > 0 else 'negative'
# print(t(2))
#
# a = [78, 56, 23, 8, 54512]
# a.sort(key=lambda x: x % 10)


# def linear(k, b):
#     return lambda x: x * k + b
#
#
# graf1 = linear(2, 5)
# print(graf1(3))

#
# adding_10 = lambda x: x + 10
# print(adding_10(10))

# starts_with = lambda x: True if x.startswith('W') else False
# print(starts_with('Word'))
#
# sale_lambda = lambda x: x * 0.9 if x > 50 else x


sq = lambda x, y: x ** 2 + y ** 2
print(sq(8, 11))

average = lambda *args: sum(args) / len(args)
