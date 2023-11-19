# def greater_10(x):
#     return x > 10
#
#
# numbers = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
# numbers_gt_10 = list(filter(greater_10, numbers))
# print(numbers_gt_10)
#
# b = list(filter(bool, numbers))
# print(b)
#
# phrase = 'IphonE 12 cost 645,89$'
# only_digits = list(filter(str.isdigit, phrase))
# print(only_digits)
#
# only_alpha = list(filter(str.isalpha, phrase))
# print(only_alpha)
#
#
# cities = {
#     'moscow': 800,
#     'boston': 750,
#     'LA': 400,
#     'SF': 900,
#     'Chicago': 650,
#     'SP': 600,
# }
# more_700 = list(filter(lambda x: cities[x] > 700, cities))
# print(more_700)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)

"""Напишите программу, которая отфильтрует список days так,
чтобы в нем остались только дни, названия которых состоят из
четырех символов или начинаются с буквы S. Используйте при этом lambda функцию.

Распечатайте получившийся список в алфавитном порядке, каждый элемент на новой строчке"""
days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']

result = list(filter(lambda x: len(x) == 4 or x.startswith('S'), days))
for word in sorted(result):
    print(word)

