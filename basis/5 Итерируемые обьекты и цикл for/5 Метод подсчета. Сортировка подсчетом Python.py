import random

# a = [0, 1, 2, 3, 2, 1]
# count = [0] * 6
#
# for i in a:
#     count[i] += 1
# print(count)


# s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
# letters = [0] * 26
# for i in s.lower():
#     if i >= "a" and i <= "z":
#         nomer = ord(i) - 97
#         letters[nomer] += 1
# for i in range(26):
#     if letters[i] > 0:
#         print(chr(i + 97), letters[i])


#
# a = []
# for i in range(10):
#     a.append(random.randint(-10, 10))
#
# count = [0] * 21
# for i in a:
#     count[i+10] += 1
# print(a)
#
# for i in range(21):
#     if count[i] > 0:
#         print(i-10, count[i])

"""Давайте на практике применим метод подсчета
На вход вашей программе поступает положительное целое число n, а ваша задача вывести в порядке возрастания все цифры, 
которые встречались в этом числе, и напротив каждого также необходимо вывести 
сколько раз данная цифра встречалась в числе n"""

# string = str(input())
# numbers = [0] * 10
#
# for symbol in string:
#     if symbol.isdigit():
#         # index = int(symbol)
#         numbers[int(symbol)] += 1
#
# for number in range(len(numbers)):
#     if numbers[number] > 0:
#         print(number, numbers[number])


# Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100
# включительно, сортировкой подсчетом.
# Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
# Вам необходимо вывести отсортированный список
# P.S. не пользуйтесь встроенной функцией sorted или методом sort


n = int(input())
list_number = list(map(int, input().split()))
numbers = []

for i in range(-100, 101):
    for a in list_number:
        if i == a:
            numbers.append(i)
print(*numbers)



# result = [0] * 201
# for i in range(-100, 101):
#     for number in list_number:
#         if i == number:
#             result[i+100] = number


