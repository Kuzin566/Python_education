# *a, b, c = [True, 1, 2, 3, 4]
# print(a, b, c)

#


a, *b, c = 'No money', 'no honey'
print(b)
print(a)


def count_args(*args):
    return len(args)

count_args(1, 2)