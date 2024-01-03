# a = [5, 6, 7, 8]
# b = [100, 200, 300, 40]
# c = 'asdasd'
# rez = zip(a, b, c)
# print(rez)
#
# col1, col2, col3 = zip(*rez)
# print(col1)


# x = [1, 2]
# y = [4, 5, 6]
# zipped = zip(x, y)
# result = list(zipped)
# print(result)

#
# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y, strict=True)
# result = list(zipped)
# print(result)
#
# x = [1, 2]
# y = [4, 5, 6]
# zipped = zip(x, y, strict=True)
# result = list(zipped)
# print(result)


"""Перед вами два списка одинаковой длины keys и values
Ваша задача создать словарь result, в котором пара ключ-значение берется из значений списков,
стоящих на одинаковых индексах. В качестве ответа выведите словарь result"""
from pprint import pprint

keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = dict(zip(keys, values))
print(result)