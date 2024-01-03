from string import ascii_uppercase

# a = [i for i in range(7)]
# print(a)
#
# a = list(map(int, input().split()))
# print(a)


# list = [1, 2, 3, 4, 5]
#
# res = [x+7 for x in list if x !=3 if x%2==1]
# res2 = []
# for x in list:
#         if x!=3 and x%2==1:
#                 res2.append(x+7)
#
# print(res)
# print(res2)

#
# a = [i*j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i*j >= 10]
# print(a)


# zeroes = [0*i for i in range(100)]
# print(zeroes)

"""При помощи генератора-списка создайте список [1, 2, 3, ..., n], 
само натуральное число n будет поступать на вход вашей программе.
В качестве ответа просто выведите получившийся список"""

# n = int(input())
#
# zeroes = [i for i in range(1, n + 1)]
# print(zeroes)

"""На вход программе подается натуральное число n (n<=1000).
При помощи list comprehension создайте список, состоящий из делителей введенного числа и выведите его на экран"""

# n = int(input())
# a = [i for i in range(1, n + 1) if n % i == 0]
# print(a)

"""При помощи list comprehension создайте список, состоящий из нечетных натуральных чисел в интервале [n; n**2]
 и вывести его на экран. Само число n поступает на вход программе
Вводится натуральное число n
Вывести список, содержащий нечетные натуральные числа в интервале [n; n**2]"""

# n = int(input())
# result = [i for i in range(n, n ** 2 + 1) if i % 2 != 0]
# print(result)

"""Программа принимает на вход два целых числа a и b.
Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно и вывести его на экран.
Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно,
 двигаясь в порядке убывания, и затем вывести его.
Не забывайте пользоваться генератором списков """

# a, b = map(int, input().split())
# result = [i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b - 1, -1)]
# print(result)

"""Создайте список первых букв каждого слова из строки st и выведите его на экран"""
# st = 'Create a list of the first letters of every word in this string'
# result = [i[0] for i in st.split()]
# print(result)

"""При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского 
алфавита ['A', 'B', 'C', 'D', ...]. 

Входные данные
На вход программе подается натуральное число n, n≤26.

Формат выходных данных
Программа должна вывести список из первых n заглавных букв английского алфавита"""

# n = int(input())
# result = [ascii_uppercase[index] for index in range(n)]
# print(result)


# n = int(input())
# result = [ascii_uppercase[index]*(index+1) for index in range(n)]
# print(result)


"""При помощи генератора-списков создайте список, состоящий из слов,  начинающихся с буквы 't'
или 'T'. Слова возьмите из переменной phrase, также не забывайте про метод split()
В качестве ответа выведите полученный список, слова в нем должны стоять в том же порядке,
 в котором они стояли в изначальной фразе"""

phrase = 'Take only the words that start with t in this sentence'
result = [word for word in phrase.split() if word.lower().startswith('t')]
print(result)
