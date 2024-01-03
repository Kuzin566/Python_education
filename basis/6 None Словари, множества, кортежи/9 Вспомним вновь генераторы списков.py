# a = [
#     ("Sidorov", 1995),
#     ("Lukov", 2002),
#     ("Petrov", 1991),
#     ("Gorbachev", 1984),
#     ("Kostin", 2000),
#     ("Isaev", 2005),
#     ("Eliseev", 1999),
#     ("Kozlov", 2004),
#     ("Bukov", 1995),
#     ("Gavrilov", 1980),
#     ("Efremov", 2006),
# ]
#
# surnames = [elem[0] for elem in a] # Получим только фамилии
# years = [elem[1] for elem in a] # Получим только год рождения
# print(surnames)
# print('-'*20)
# print(years)

"""В вашем распоряжении есть двумерный список vector. 
Ваша задача при помощи генератора-списка сделать на основании vector линейный(одномерный ) список и вывести его"""
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

result = [value for values in vector for value in values]
print(result)
