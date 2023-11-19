# a = [i ** 2 for i in range(1,6)]
# print(a)
from random import randint

# b = (i ** 2 for i in range(1,6))
# d = iter(b)
# print(next(d))
# print(next(d))


# d = (i**2 for i in range(1, 6))
# a = list(d)
# b = tuple(d)
# print(b)


# d = (i ** 2 for i in range(1, 6))
# print(9 in d, 4 in d)


d = (i ** 2 for i in range(1, 6))
print(7 in d, 4 in d)


# Создайте генератор
from_10_to_20 = (i for i in range(10, 20 +1))

# Распечатайте три первых значения
print(next(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))

for value in from_10_to_20:
    print(value)


words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
         'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am']

lens = (len(word) for word in words)

for i in lens:
    print(i)
