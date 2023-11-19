# a = [1, '2', True]
# for i in a:
#     if isinstance(i, str):
#         print(i)
#
# a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
# sum_nums = 0
# for i in a:
#     if isinstance(i, (int, float)):
#         sum_nums += i
# print(sum_nums)
#
# yes = True
# num = 1
# print(isinstance(num, int), isinstance(yes, int))

"""Ваша задача написать функцию count_strings, которая принимает произвольное количество аргументов. 
Функция должна среди всех переданных значений найти только строки, найти их количество и  вернуть в качестве результата."""
# def count_strings(*args):
#     count = 0
#     for i in args:
#         if isinstance(i, str):
#             count += 1
#     return count
#
#
# a = count_strings('am', 'world', 'hello', 'is')
# print(a)


"""Ваша задача написать функцию find_keys, которая принимает произвольное количество именованных аргументов. 
Функция должна отобрать только те имена параметров, у которых значения являются списками или кортежами.
Функция find_keys должна собрать все имена таких параметров в список, отсортировать их по алфавиту вне
зависимости от регистра букв и вернуть в качестве результата."""


def find_keys(**kwargs):
    result = [i for i, value in kwargs.items() if isinstance(value, (list, tuple))]
    return sorted(result, key=str.casefold)


c = find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4])
print(c)
