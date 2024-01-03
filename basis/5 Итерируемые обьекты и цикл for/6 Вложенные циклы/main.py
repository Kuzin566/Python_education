# count = 0
# for b1 in "tukva":
#     for b2 in "tukva":
#         for b3 in "tukva":
#             for b4 in "tukva":
#                 for b5 in "tukva":
#                     for b6 in "tukva":
#                         rez = b1 + b2 + b3 + b4 + b5 + b6
#                         if rez[0] in "tkv" and rez[-1] in "tkv":
#                             if rez.count("a") + rez.count("u") == 2:
#                                 count += 1


# for i in range(1, 100001):
#     x = i
#     s = 0
#     while x > 0:
#         s += x % 10
#         x //= 10
#     print(i, s)

"""Ваша задача найти сумму всех четырехзначных натуральных чисел, сумма цифр которых равна 20.
Примерами таких чисел являются 9065, 8129, 7355 и тд. У каждого из указанных чисел сумма цифр равна 20"""

# result = []
# for i in range(1000, 10000):
#     x = i
#     s = 0
#     while x > 0:
#         s += x % 10
#         x //= 10
#     if s == 20:
#         result.append(i)
# print(sum(result))

# a = int(input())
# for i in range(1, a + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

numbers = list(map(int, input().split()))

for number in numbers:
    print('*' * number)
