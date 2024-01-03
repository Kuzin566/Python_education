"""Ваша задача создать список из n строк. Программа сперва будет
принимать натуральное число n, а затем n строк в каждой отдельной строке.
В качестве ответа выведите получившийся список."""

# n = int(input())
# list_1 = []
# for i in range(n):
#     list_1.append(str(input()))
#
# print(list_1)


"""Входные данные
На первой строке вводится один символ — строчная буква.
На второй строке вводится предложение.
Выходные данные
Нужно вывести список слов (словом считается часть предложения, окружённая символами пустого пространства), 
в которых присутствует введённая буква в любом регистре, в том же порядке, в каком они встречаются в предложении."""

# letter = str(input().lower())
# strings = str(input()).split()
#
# for word in strings:
#     if letter in word.lower():
#         print(word)


"""На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение. 
В случае, если положительных значений нет, выведите строку "Empty"""

# numbers = list(map(int, input().split()))
# filter_list = []
# for number in numbers:
#     if number > 0:
#         filter_list.append(number)
# if not filter_list:
#     print('Empty')
# else:
#     print(min(filter_list))

# Вспомним, что есть метод который считает количество указанных символов в строке - .count :)


"""Напишите программу, которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.
Формат ввода
Вводится одна строка.
Формат вывода
Выводится одно целое число — максимальное количество раз, которое встречается какая-либо буква (без учёта регистра) 
или иной символ во введённой строке."""

# string = str(input().lower())
# count_letter = []
# for letter in string:
#     count = string.count(letter)
#     if not count in count_letter:
#         count_letter.append(count)
# print(max(count_letter))
"""Вариант №2"""
# string = str(input().lower())
# max_retry = 0
# for letter in string:
#     count = string.count(letter)
#     if count > max_retry:
#         max_retry = count
# print(max_retry)

"""а вход программе подается строка, состоящая из различных символов: буквы, цифры, знаки препинания и т.д.
Ваша задача определить сколько символов в данной строке являются цифрами и также найти сумму всех этих цифр.
 Например, в строке "Комната 1408" содержится 4 цифры и их сумма равна 13.
В качестве ответа необходимо через пробел вывести 2 числа - количество цифр в введенной строке и их сумму"""

# string = str(input())
# symbols = []
# for letter in string:
#     if letter.isdigit():
#         symbols.append(int(letter))
# print(len(symbols), sum(symbols))

#
# a = input()
# count = 0
# for i in range(len(a)):
#     if count == -1:
#         break
#     elif a[i] == '(':
#         count += 1
#     elif a[i] == ')':
#         count -= 1
#
# if count == 0:
#     print("YES")
# else:
#     print('NO')

string = list(map(str, input().split()))
filter_string = []
for word in string:
    if word.lower() not in [value.lower() for value in filter_string]:
        filter_string.append(word)
print(*filter_string)
