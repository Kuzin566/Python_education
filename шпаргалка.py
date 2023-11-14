# Шпаргалки


# ЧИСЛА

# import this

# import math
# num1 = math.sqrt(2)     # вычисление корня квадратного из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз

# from math import *
# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз

# bin() - перевод в 2ичную
# oct() - перевод в 8ичную
# hex() - перевод в 16ичную

# res=round(x,2) -- округляет до 2 знаков после .


# СТРОКИ

# capitalize() - только первая буква большшая
# swapcase() - верхний в нижний, нижний в верхний
# title() - каждое слово с большой буквы
# lower() - все слова в нижнем регистре
# upper() - все символы имеют верхний регистр

# count(<sub>, <start>, <end>) - количество непересекающихся вхождений подстроки
# startswith(<suffix>, <start>, <end>) - начинается ли исходная строка подстрокой
# endswith(<suffix>, <start>, <end>) - оканчивается ли исходная строка  подстрокой
# find(<sub>, <start>, <end>) - находит индекс первого вхождения подстроки
# rfind(<sub>, <start>, <end>) - начиная с конца
# strip(<chars>) - удалены все пробелы стоящие в начале и конце строки (набор символов для удаления)
# lstrip() / rstrip() - удалеет пробелы в начале / в конце
# replace(<old>, <new>, <count>) - заменить

# isalnum() - только цифры и буквы ?
# isalpha() - только буквы ?
# isdigit() - только из цифр ?
# islower() - только в нижнем регистре ?
# isupper() - только заглавные ?
# isspace() - только пробелы ?

# ord() - символ какой код ?
# chr() - код какой символ ?


# СПИСКИ

# list() - список из символов
# append() - добавляет строку как один элемент
# extend() - делит строку на элементы и добавляет все
# del

# print(*list) - распаковка элементов списка через пробел

# split() - разбивает строку на слова
# join() - собирает строку из элементов списка,
#          используя в качестве разделителя строку, к которой применяется метод
# s = ' '.join(words)

# insert(index, value) - вставить значение в список в заданной позиции
# index()
# remove(value) - удаляет первый  value
# pop() - выносит из списка элемент. В списке он удаляется
# count() - количество искомого элемента в списке
# reverse() - инвертирует порядок следования значений в текущем списке
# clear() - удаляет все элементы из списка
# copy() - создает поверхностную копию списка
# sort()
# (key=int)
# sort(reverse = True)
# sorted(l) - сортирует и возвращает копию, а не исходный

# [input() for _ in range(n)]
# [int(input()) for _ in range(int(input()))]
# [int(x) for x in input().split()]

# ljust(num,sym) - дополняет элемент символами до определенного кол-ва
# print('ab'.ljust(5, '$')) -- ab$$$
# print('ab'.rjust(5, '$')) -- $$$ab


# ФУНКЦИИ

# def draw_box(): - функция
# def do_nothing():
#     pass          - содержит единственную строку кода, которая ничего не делает

# def название_функции(параметры):
#     блок кода
# ef draw_box(height, width):    # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)

# num = 7  # глобальная num
# def get_nam1():     # Так делать можно
#     num = 1         # Инициализируется локальная num
#     num = num + 1   # Локальная num = 2, глобальная num = 7
#     return num
# _____________________________________________________________

# num = 7  # глобальная num
# def get_nam2():         # Так делать можно
#     number = num + 1    # Функция поищет num в локальной области видимости,
#     return number       # не найдёт, поищет в глобальной и возьмёт значение 7
#                         # Локальная number = 8, глобальная num = 7
# _____________________________________________________________

# num = 7  # глобальная num
# def get_nam3():     # Так делать нельзя !!
#     num = num + 1   # Обявляется локальная num. Но не может инициализироваться.
#     return num      # Так как в правой части выражения num уже считается локаньй
#                     # но никак не определена.
#                     # UnboundLocalError: local variable 'num' referenced before assignment
#                     # локальная переменная 'num', на которую ссылаются перед назначением
# _____________________________________________________________

# num = 7  # глобальная num
# def get_nam4():     # Так делать можно
#     global num      # На прямую указывается, что используем глобальную num
#     num = num + 1   # Глобальная num = 8
#     return num

# def название_функции():
#     блок кода
#     return выражение


# РАНДОМ

# from random import *
# randint(a,b) - возвращает случайное целое число из отрезка [a;b]
# randrange(0, 101, 10) - возвращает случайное целое число из последовательности
# random() - выводит случайное число с плавающей точкой из диапазона [0.0;1.0)
# uniform(a,b) - число с плавающей точкой из диапазона [a;b]
# seed() - всегда генерировать одну и ту же последовательность случайных чисел

# shuffle() - принимает список в качестве аргумента и перемешивает его
# choice() - возвращает один случайный элемент из переданного списка (строки)
# sample(text,count) - список случайных элементов в указанном количестве


# while any(friends[i] == friends2[i] for i in range(len(friends))):


# Метод МОНТЕ-КАРЛО
# Вычисление площади рандомной фигуры

# from random import uniform

# n = 10**6
# k = 0
# s0 = 1
# for _ in range(n):
#     x = uniform(-1, 1)
#     y = uniform(-1, 1)

#     if x**2 + y**2 == 1:
#         k += 1

# print((k/n)*s0)


# import string
# help(string)

# DATA
# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# hexdigits = '0123456789abcdefABCDEF'
# octdigits = '01234567'
# printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# whitespace = ' \t\n\r\x0b\x0c'


# БУЛЕНЫ
# isinstance(переменная, тип данных) -- True - соответствует, False - не соответствует
# type() -- переменная какой тип данных


# МАТРИЦЫ

# выше главной диагонали, то i < j, ниже, i > j.
# выше побочной диагонали, то i + j + 1 < n, ниже, i + j + 1 > n.

# Вывод матрицы
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# Считывание матрицы
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)


# КОРТЕЖИ

# tuple() - кортеж
# index(), count()
# len(), sum(), min() и max()
# tuple(sorted())
# join()

# colors = ('red', 'green', 'blue')
# a, b, _ = colors -- распаковка отдельных значений из кортежа

# a, b, *tail = 1, 2, 3, 4, 5, 6
# tail = [3, 4, 5, 6]

# a = 1,      # не распаковка, а просто присвоение
# b, = 1,     # распаковка

# print(a) -- (1,)
# print(b) -- 1

# partition() -- split() для кортежей


# МНОЖЕСТВА

# a= set() -- пустое множество
# sorted(a) -- сортирует множество (возвращает отсортированный список)
# .add() -- добавить эл-т
# .remove(x) -- удалить эл-т. Если эт-та нет -- ошибка
# .discard() -- удалить эл-т. Если эт-та нет -- ничего не происходит
# num = numbers.pop() -- удаляет случайный элемент множества, возвращая его. Если эт-та нет -- ошибка
# clear() удаляет все элементы из множества


# a = b.union(c) -- объединение множеств. создает новое множество
#               a = b|c
# a.update(b) -- изменение текущего множества
#               a|=b

# a = b.intersection(c)
#               a = b&c -- пересечение множеств. создает новое множество
# a.intersection_update(b) -- изменение текущего множества
#               a&=b

# a = b.difference(c)
#               a = b-c -- вычитание. убирает из множества эл-ты, входящие в другое множество
# difference_update()
#               a-=b

# a = b.symmetric_difference(c)
#               a = b^c -- симметричная разница
# symmetric_difference_update()
#               a^=b

# issubset() -- множество является подмножеством другого?
#               a<=b -- нестрогое
#               a<b -- строгое (точно не равны)

# issuperset() -- множество является надмножеством другого?
#               a>=b -- нестрогое
#               a>b -- строгое (точно не равны)

# isdisjoint() -- множества не имеют общих элементов?

# digits = {int(c) for c in input()}

# frozenset() -- замороженное множество


# СЛОВАРИ

# a={"ключ" : "значение"}
# a["ключ"] == "значение"

# a = dict(name = 'Timur', age = 28)
# a = dict([('name', 'Timur'), ('age', 28)])
# a = dict.fromkeys(['name', 'age'], 'одинаковое значение')

# dict1 = {} -- пустые словари
# dict2 = dict()

# a= dict(zip(keys, values))

# len() -- кол-во пар ключ-значение
# in -- ищет ключ
# sum(), min(), max(), min(), max() -- по ключам

# ==, != -- сравнивает пары ключ-значение

# keys() -- список ключей
# values() -- список значений
# items() -- список кортежей (ключ, значение)

# print(*capitals) -- распаковка ключей

# sorted() -- список отсортированых ключей
# sorted(a.items(), key= lambda x: x[1]) -- список отсортированых значений

# get(поиск ключа, значение если ключа нет)
# update() - объединение словарей
#                 |, |= --объединение словарей
# setdefault()
# copy() -- создает поверхностную копию словаря


# del -- удалить элементы словаря по ключу. Если ключа нет -- ошибка
# pop(ключ, значение если ключа нет) -- удаляет элемент по ключу, возвращая его значение
# popitem() -- удаляет последний добавленный элемент,  возвращает (ключ, значение)
# clear() -- удаляет все элементы из словаря


# Decimal – десятичное число, для выполнения точных расчетов;
# Fraction – число, представляющее собой обыкновенную дробь, с заданным числителем и знаменателем;
# Complex – комплексное число.

# Сравнение float
# num = 0.1 + 0.1 + 0.1
# eps = 0.000000001           # точность сравнения
# if abs(num - 0.3) < eps:    # число num отличается от числа 0.3 менее чем 0.000000001
#     print('YES')
# else:
#     print('NO')


# from decimal import Decimal as D
# num1 = Decimal('5.2')

# num_tuple = num.as_tuple()

# print(num_tuple.sign) -- знак числа (0 для положительного числа и 1 для отрицательного числа)
# print(num_tuple.digits) -- цифры числа
# print(num_tuple.exponent) -- значение экспоненты (количество цифр после точки, умноженное на −1)

# getcontext()
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0,
# flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

# getcontext().prec = 3      # устанавливаем точность в 3 знака во время вычислений (включая целую часть)
# num.quantize(Decimal('1.000')) -- округление до 3 цифр в дробной части

# ROUND_CEILING – округление в направлении бесконечности (Infinity);
# ROUND_FLOOR – округляет в направлении минус бесконечности (- Infinity);
# ROUND_DOWN – округление в направлении нуля;
# ROUND_HALF_EVEN – округление до ближайшего четного числа, число 6.5 округлится не до 7, а до 6;
# ROUND_HALF_DOWN – округление до ближайшего нуля;
# ROUND_UP – округление от нуля;
# ROUND_05UP – округление от нуля (если последняя цифра после округления до нуля была бы 0 или 5, в противном случае к нулю).


# Fraction -- дробь

# from fractions import Fraction

# n1 = Fraction(числитель, знаменатель)
# n2 = Fraction('1/9')

# n1.numerator -- числитель
# n1.denominator -- знаменатель

# as_integer_ratio(n1) возвращает кортеж, состоящий из числителя и знаменателя

# Decimal (+, -, *, /) Fraction -- НЕЛЬЗЯ


# Комплексные числа

# complex(вещественная, мнимая)

# z1 = -3 + 2j              # создание на основе литерала
# z2 = complex(6, -8)       # z2 = 6 - 8j
# z5 = complex('3+4j')      # создание на основе строки

# x = z.real -- Действительная часть
# y = z.imag -- Мнимая часть

# .conjugate() -- сопряженное 3+4j 3-4j


# TURTLE

# from turtle import *
# n=int(input())

# showturtle()
# forward(n)
# backward(n)
# right() -- угол от текущего направления
# left()
# setheading() -- угол от начального направления
# penup() --  поднимает перо
# pendown() -- опускает
# circle(радиус) -- круг
# pensize() -- Изменение размера пера
# pencolor() -- Изменение цвета


# Именованные аргументы

# def matrix(n=1, m=None, x=0):
#         if m is None:
#                 m=n -- если m не указали


# def my_sum(*args): -- *args - создает кортеж
#         return sum(args)
# print(my_sum(1, 2, *[3, 4, 5], *(7, 8, 9), 10)) -- * распаковывает элементы перед тем как использовать

# def my_func(**kwargs): -- аргументы получаются в виде словаря, что позволяет сохранить имена аргументов в ключах

# def make_circle(x, y, radius, *, line_width=1, fill=True) -- line_width и fill могут быть переданы только как именованные аргументы
# после * -- строго именованные


# max(numbers, key=abs)        #  по модулю
# min(numbers, key=abs)       #  по модулю
# sorted(numbers, key=abs)     #  по модулю

# new_numbers = map(abs, map(int, numbers)) -- применить ко всем эл-м

# filter(функция, список) оставляет только элементы, для которых функция - True


# from functools import *
# def mult(x, y):
#     return x*y
# product = reduce(mult, numbers, 1)


# from operator import *
# a == b	eq(a, b)
# a != b	ne(a, b)
# a * b	        mul(a, b)
# -a	        neg(a)


# lambda список_параметров: выражение -- анонимные функции

# data.sort(key=lambda x: (len(x), x)) -- сортирует по одному признаку и если признак одинаковый по второму


# all(iterable) -- все True ?
# со словарем проверяет ключи
# any() -- хотябы один элемент True ?

# result = all(map(lambda x: True if x > 10 else False, numbers)) -- в соответствии с неким условием

# enumerate(iterable, start) -- кортеж из индекса элемента и самого элемента

# zip(*iterables)


# Работа с файлами

# open() --  создает файловый объект и связывает его с файлом на диске
# close() -- закрытие файла
# файловая_переменная = open(имя_файла, режим_доступа)

#         'r' - не может быть изменен  -- дефолтное значение в опене
#         'w' - создать или изменить данные файла. (существующие данные стираются)
#         'a' - добавление данных в конец файла
#         'r+' - частичная перезапись содержимого файла
#         'x' - Создать новый файл. Если файл существует, произойдет ошибка

# test_file = open('C:\\Users\\temp\\test.txt', 'w') -- "\" нужно экранировать
# test_file = open(r'C:\Users\temp\test.txt', 'w') -- "r" сырая строка. экранировать не нужно
#         / - для Windows

# file = open('info.txt', 'r', encoding='utf-8') - Указание кодировки при открытии файла

# file1.encoding - проверка кодировки
# file2.closed - True если закрыт
# file.mode	возвращает режим доступа с помощью которого был открыт файл
# file.name	возвращает имя файла

# read(количество символов) – читает все содержимое файла;
# readline() – читает одну строку из файла;
# readlines() – читает все содержимое файла и возвращает список строк.

# 't'	Текстовый режим (значение по умолчанию) (rt или rb)
# 'b'	Бинарный режим

# file.seek(0) -- переместить курсор в начало строки (считает байты)
# file.tell() -- получает текущую позицию курсора в байтах

# with open('languages.txt', 'r', encoding='utf-8') as file: -- менеджер контекста
#     for line in file:
#         print(line)
#                           # автоматическое закрытие файла


# Считывание CSV

# def read_csv():
#         with open('data.csv', encoding='utf-8') as csv:
#                 l=[line.strip() for line in csv]
#                 keys=l[0].split(',')
#                 values=l[1:]
#                 res=[]
#                 # print(*keys)
#                 # print(values[0], sep='\n')
#                 for vsl in values:
#                         lib={}
#                         for i in range(len(keys)):
#                                 lib[keys[i]]=vsl.split(',')[i]
#                         res.append(lib)
#                 # return res
#                 for x in res:
#                         print(x)
# read_csv()


# write() – записывает переданную строку в файл;
# writelines() – записывает переданный список строк в файл.
# print('Джoн Локк', file=переменная) - записывает и автоматически переносит на следующую строку


# Транслитерация
# d = { 'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya' }

# with open('cyrillic.txt', encoding='utf-8') as wrd:
#         txt=wrd.read()
#         res=''
#         for i in txt:
#                 res+=d.get(i, i)
# with open('transliteration.txt', 'w', encoding='utf-8')as result:
#         print(res, file=result)


# Исключения

# try:
#         выражение
# except название ошибки :
#         тело что делать если ошибка
# что делать если все ок


# ООП

# class first_class:
#         '''Название класса'''
#         color = 'red'
#         circle = 2

# a = first_class() #-- создание объекта принадлежащего классу
# b = first_class()


# a.color = 'blue' #-- присваивание свойства объекту или классу
# setattr(first_class, 'prop', 1) #-- присваивание свойства классу

# .__dict__ #-- свойства объекта или класса
# .__doc__ -- название класса

# getattr(first_class, 'искомый атрибут', значение если нет атрибута ) -- искать атрибут

# del first_class.type
# delattr(first_class, атрибут)

# hasattr(first_class, искомый атрибут) - True если атрибут есть в классе
# если атрибут есть у класса, но нет у объекта -- то все равно True


# def set_coords(self): -- self ссылка на экземпляр класса

# Points.set_coords(pt) -- когда вызываем через класс обязательно нужно подставить объект
# pt.set_coords()

# def set_coords(self, x, y):
#                 self.x = x -- создаем локальное свойство
#                 self.y = y

# class Points:
#         color = 'red'
#         circle = 2
#         def set_coords(self, x, y): # добавить сойства объекту
#                 self.x = x
#                 self.y = y
#         def get_coords(self):   # вызвать свойства объектов
#                 return(self.x, self.y)


# def __init__(self, a=0, b=0): -- вызывается сразу
# чтобы при создании заводить параметры

# def __del__ (self): -- автоматический сборщик мусора
# удаляет объект если он уже не используется

# isinstance(элемент, класс) -- является ли объект элементом класса


# class Point:
#     def __new__(cls, *args, **kwargs): # cls -- ссылается на сам класс
#         return super().__new__(cls)
#     def __init__(self, x=0, y=0): # self -- ссылается на экземпляр класса (объект)
#         self.x, self.y = x, y


# class DataBase:
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None: # Если объекта нет то создается объект
#             cls.__instance = super().__new__(cls)
#         return cls.__instance # Если есть просто дает ссылку на существующий

#     def __init__(self, name, pasw):
#         self.name, self.pasw = name, pasw

#     def __del__(self):
#         DataBase.__instance = None # Если объект не используется -- автоматически удаляется. флаг обнуляется

#     def func(self):
#         pass


# class  Vector:
#     MIN_C = 0
#     MAX_C = 100

#     @classmethod #  Работает исключительно с атрибутами класса, но не может обращаться к локальным атрибутам экземпляра
#     def valid(cls, arg):
#         return cls.MIN_C <= arg <= cls.MAX_C

#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.valid(x) and Vector.valid(y):
#             self.x, self.y  = x, y

#     @staticmethod # вспомагательная функция, которая не имеет доступа к даным класса
#     def norma(x, y):
#         return x**2 + y**2


# if бла бла бла:
#     то блок кода
# else:
#     raise ValueError('Текст ошибки')

# attr -- public
# _attr -- protected -  внутри класса или в дочерних классах
# __attr -- private - только внутри класса

# dir(объект) -- все свойства объекта класса


# old = property(get_old, set_old) -- заключаем в одно свойство 2 функции
# a.old -- без записи данных - getter
# a.old = 35 -- с записью данных - setter

# @property               # a.old -- без записи данных - getter
# def old(self):
#     return self.__old

# @old.setter             # a.old = 35 -- с записью данных - setter
# def old(self, old):
#     self.__old = old

# @old.deleter              # del a.old -- вызывается deleter
# def old(self):
#     del self.__old


# class A:
#         @classmethod
#         def valid_coord(cls, coord):
#                 if type(coord) != int:
#                         raise TypeError ('Текст ошибки')

#         def __set_name__(self, owner, name): # создает переменную с именем _name
#                 self.name = '_'+name         # вызывается автоматически

#         def __get__(self, instance, owner):
#                 return instance.__dict__[self.name]
#                 # return getattr(instance, self.name)

#         def __set__(self, instance, value):            # срабатывает в момент присваивания значения переменной
#                 self.valid_coord(value)
#                 instance.__dict__[self.name] = value
#                 # setattr(instance, self.name, value)

#         def __del__(self):
#                 pass


# class Point3D:
#         x = A()
#         y = A()
#         z = A()

#         def __init__(self, x, y, z)
#                 self.x, self.y, self.z = x, y, z


# МАГИЧЕСКИЕ МЕТОДЫ

# def __getattribute__(self, item): -- вызывается автоматически когда обращается к атрибуту класса
#         if item == 'x':
#                 raise ValueError('Доступ запрещен')
#         else:
#                 return object.__getattribute__(self, item)


# def __setattr__(self, key, value): --вызывается автоматически при присваивании
# if key == 'z':
#         raise ValueError('Недопустимое имя атрибута')
# else:
#         object.__setattr__(self, key, value)

# def __getattr__(self, item): -- вызывается при обращении к несуществующему атрибуту
#         return False

# def __delattr__(self, item): -- вызывается при удалении атрибута
#         object.__delattr__(self, item)


# class Counter:
#         def __init__(self, deff):
#                 self.__counter = 0
#         def __call__(self, *args, **kwargs):
#                 self.__counter += 1
#                 return self.__counter

# c = Counter() -- вызов класса
# c() -- вызов объекта этого класса и выполнение __call__


# @Counter -- декоратор подставляет функцию в класс
# def some():
#         pass


# class Cat:
#         def __init__(self, name):
#                 self.name = name
#         def __repr__(self):
#                 return f'{self.__class__}: {self.name}' #- при вызове объекта в консоли
#         def __str__(self):
#                 return f'{self.name}' #- при печати объекта

# cat = Cat('Vasya')
# print(cat)


# class Point:
#         def __init__(self, *args):
#                 self.__coords = args
#         def __len__(self):
#                 return len(self.__coords)
#         def __abs__(self):
#                 return list(map(abs, self.__coords))
# p = Point(1, -2, -5)
# print(len(p))
# print(abs(p))


# class Clock:
#         __DAY = 86400

#         def __init__(self, seconds: int): # seconds: int просто указание, не проверка
#                 if not isinstance(seconds, int):
#                         raise TypeError('Секунды должны быть целым чтслом')
#                 self.seconds = seconds % self.__DAY

#         def get_time(self):
#                 s = self.seconds % 60
#                 m = (self.seconds // 60) % 60
#                 h = (self.seconds // 3600) % 24
#                 return f'{self.__get_formated(h)}: {self.__get_formated(m)}: {self.__get_formated(s)}'
#         @classmethod
#         def __get_formated(cls, x):
#                 return str(x).rjust(2, '0')

#         def __add__(self, other):
#                 if not isinstance(other, (int, Clock)):
#                         raise ArithmeticError('Не целое число')
#                 sc = other
#                 if isinstance(other, Clock):
#                         sc = other.seconds
#                 return Clock(self.seconds + sc)
#         # c1 = c1 + 100
#         # c3 = c1 + c2

#
#         def __radd__(self, other): # для 100 + с1
#                 return self + other
#         def __iadd__(self, other): # для c1 += 100
#                 if not isinstance(other, (int, Clock)):
#                         raise ArithmeticError('Не целое число')
#                 sc = other
#                 if isinstance(other, Clock):
#                         sc = other.seconds
#                 self.seconds += sc
#                 return self

# __add__ -- x + y
# __sub__ -- x - y
# __mul__ -- x * y
# __truediv__ -- x / y
# __floordiv__ -- x // y
# __mod__ -- x % y


# __eq__() –- ==
# __ne__() –- !=
# __lt__() –- <
# __le__() –- <=
# __gt__() –- >
# __ge__() –- >=


# class Point:
#         def __init__(self, x, y):
#                 self.x, self.y = x, y
#         def __eq__(self, other): #-- hash перестает работать
#                 return self.x == other.x and self.y == other.y
#         def __hash__(self): # Сделали свой hash
#                 return hash((self.x, self.y))

# p1 = Point(1, 2)
# p2 = Point(1, 2)
# # print(p1 == p2)
# # print(hash(p1), hash(p2), sep='\n')

# d = {}
# d[p1] = 1
# d[p2] = 2
# print(d) # в словаре один ключ, т.к. хэши одинаковые


# class Point:
#         def __init__(self, x, y):
#                 self.x, self.y = x, y

#         def __len__(self): # переопределяет bool
#                 return self.x**2 + self.y**2
#         def __bool__(self):
#                 return self.x == self.y

# p = Point(1, 2)
# print(bool(p)) # по дефолту всегда True


# class Students:
#         def __init__(self, name, marks):
#                 self.name = name
#                 self.marks = list(marks)

#         def __getitem__(self, item):
#                 if 0 < item < len(self.marks):
#                         return self.marks[item]
#                 else:
#                         raise IndexError('Неверный индекс')
#         def __setitem__(self, key, value):
#                 if not isinstance(key, int) or key < 0:
#                         raise TypeError('Должно быть число')
#                 self.marks[key] = value

#         def __delitem__(self, key):
#                 if not isinstance(key, int) or key < 0:
#                         raise TypeError('Должно быть число')
#                 del self.marks[key]

# s1 = Students('Сергей', [1, 2, 3, 4, 5])
# s1[2] #== s1.marks[2]

# s1[2] = 6 #== s1.marks[2] = 6

# del s1[2] # удаление


# class FRange:
#         def __init__(self, start=0.0, stop=0.0, step=0.0):
#                 self.start = start
#                 self.stop = stop
#                 self.step = step

#         def __iter__(self):
#                 self.value = self.start - self.step
#                 return self

#         def __next__(self):
#                 if self.value + self.step < self.stop:
#                         self.value += self.step
#                         return self.value
#                 else:
#                         raise StopIteration


# class FRange2D:
#         def __init__(self, start=0.0, stop=0.0, step=0.0, rows=5):
#                 self.rows = rows
#                 self.fr = FRange(start, stop, step)
#         def __iter__(self):
#                 self.value = 0
#                 return self
#         def __next__(self):
#                 if self.value < self.rows:
#                         self.value+=1
#                         return iter(self.fr)
#                 else:
#                         raise StopIteration

# fr = FRange2D(0, 2, 0.5, 4)
# for row in fr:
#         for x in row:
#                 print(x, end = ' ')
#         print()


# class Geom: # Родительский
#         name = 'Geom'
#         def set_coords(self, x1, y1, x2, y2):
#                 self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
#                 #self.draw() - так нельзя


# class Line(Geom):  # Line наследует Geom (Дочерний)
#         def draw(self):
#                 print('Рисование линии')


# class Rect(Geom):  # Rect наследует Geom (Дочерний)
#         def draw(self):
#                 print('Рисование прямоугольника')


# # g = Geom()
# l = Line()
# r = Rect()
# # g.set_coords(0, 0, 0, 0)
# l.set_coords(1, 2, 3, 4)
# r.set_coords(5, 6, 7, 8)
# # print(g.__dict__)
# print(l.__dict__)
# print(r.__dict__)


# object -- глобальный общий класс
# issubclass(дочерний, базовый) -- только с классами


# class Geom:
#         name = 'Geom'
#         def __init__(self, x1, y1, x2, y2):
#                 print(f'Инициализатор Geom для {self.__class__}')
#                 self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

# class Line(Geom):
#         def draw(self):
#                 print('Рисование линии')


# class Rect(Geom):
#         def __init__(self, x1, y1, x2, y2, fill = None):
#                 super().__init__(x1, y1, x2, y2) # Ссылка на объект посредник
#                 print('Инициализатор Rect')
#                 self.fill = fill
#         def draw(self):
#                 print('Рисование прямоугольника')


# l = Line(0, 0, 0, 0)
# r = Rect(1, 2, 3, 4)
# print(r.__dict__)


# class GenericView:
#         def __init__(self, methods=('GET',)):
#                 self.methods = methods

#         def get(self, request):
#                 return f"url: {request['url']}"


# class DetailView(GenericView):
#         def render_request(self, request, method):
#                 if method not in self.methods:
#                         raise TypeError('данный запрос не может быть выполнен')
#                 elif not 'url' in request:
#                         raise TypeError('request не содержит обязательного ключа url')
#                 else:
#                         return self.__getattribute__(method.lower())(request)


# class Singleton:
#         _instance = None
#         _instance_base = None
#         def __new__(cls, *args, **kwargs):
#                 if cls == Singleton:
#                         if cls._instance_base is None:
#                                 cls._instance_base = object.__new__(cls)
#                         return cls._instance_base
#                 if cls._instance is None: # Если объекта нет то создается объект
#                         cls._instance = super().__new__(cls)
#                 return cls._instance # Иначе возвращает уже существующий


# # В каждом классе можно создать только один объект
# class Game(Singleton):
#         def __init__(self, name):
#                 if 'name' not in self.__dict__:
#                         self.name = name

# class Game2(Singleton):
#         def __init__(self, name):
#                 if 'name' not in self.__dict__:
#                         self.name = name


# callable(v) -- вызываемые функции


# class Geom:
#         name = 'Geom'
#         def __init__(self, x1, y1, x2, y2):
#                 self.__x1 = x1
#                 self.__y1 = y1
#                 self.__x2 = x2
#                 self.__y2 = y2

# class Rect(Geom):
#         def __init__(self, x1, y1, x2, y2, fill = 'red'):
#                 super().__init__(x1, y1, x2, y2)
#                 self.__fill = fill

#         # def get_coords(self): -- выдаст ошибку
#         #         return (self.__x1, self.__y1, self.__x2, self.__y2)

# r = Rect(1, 2, 3, 4)
# print(r.__dict__)
# # {'_Geom__x1': 1, '_Geom__y1': 2, '_Geom__x2': 3, '_Geom__y2': 4, '_Rect__fill': 'red'}


# class Geom:
#         def get_pr(self):
#                 raise NotImplementedError('В дочернем классе должен быть свой get_pr')
#                 # обстрактный метод


# class Rectangle(Geom):
#         def __init__(self, w, h):
#                 self.w = w
#                 self.h = h
#         def get_pr(self):
#                 return 2 * (self.w + self.h)

# class Square(Geom):
#         def __init__(self, a):
#                 self.a = a
#         def get_pr(self):
#                 return 4 * self.a


# class Goods:
#         def __init__(self, name, weight, price):
#                 print('init Goods')
#                 super().__init__()
#                 self.name = name
#                 self.weight = weight
#                 self.price = price
#         def print_info(self):
#                 print(f'{self.name}, {self.weight}, {self.price}')

# class MixinLog:
#         ID = 0
#         def __init__(self):
#                 self.ID += 1
#                 self.id = self.ID
#         def save_sell_log(self):
#                 print(f'{self.id}: товар был продан в 00:00')
#         def print_info(self):
#                 print(f'print_info MixinLog')


# class NoteBook(Goods, MixinLog): # первым ставить класс с инициализатором
#         pass                     # остальные классы без параметров в инит!!

# n = NoteBook('Mac', 1.5, 30000)
# n.print_info() # вызывается из класса Goods
# MixinLog.print_info(n) # вызывается из класса MixinLog
# # либо переопределить в дочернем
# print(n.__dict__)
# print(NoteBook.__mro__) # список классов которые обходит дочерний класс


# import timeit # модуль измеряющий скорость работы


# class Point:
#         def __init__(self, x, y):
#                 self.x, self.y = x, y
#         def su(self):
#                 return self.x + self.y

# class Point2D:
#         __slots__ = ('x', 'y') # не дает создать другие локальные атрибуты объекта
#         # из-за slots не существует dict
#         def __init__(self, x, y):
#                 self.x, self.y = x, y
#         def su(self):
#                 return self.x + self.y

# pt = Point(1, 2)
# pt2 = Point2D(1, 2)

# print(pt.__sizeof__() + pt.__dict__.__sizeof__()) # 304
# print(pt2.__sizeof__()) # 32

# t1 = timeit.timeit(pt.su)
# t2 = timeit.timeit(pt2.su)
# print(t1, t2)


# # Ускоряет работу, уменьшает занимаемую памяь


# try:
#         print(2/0)
# except ZeroDivisionError as z:
#         print(z) -- в консоль выводится стандартное исключение
# else :
#         print('Не произошло исключений') - действия которые совершаются только если ошибок не произошел
# finally:
#         print('Работает ВСЕГДА в последнюю очередб') -- отрабатывает до return


# class ExceptionPrint(Exception): #класс исключение наследует от базового
#         def __init__(self, *args):
#                 self.message = args[0] if args else None
#         def __str__(self):
#                 return f'Ошибка : {self.message}'


# class DefenedVector:
#         def __init__(self, v):
#                 self.__v = v
#         def __enter__(self):
#                 self.__temp = self.__v[:]
#                 return self.__temp
#         def __exit__(self, exc_type, exc_val, exc_tb):
#                 if exc_type is None:
#                         self.__v[:] = self.__temp
#                 return False
#         # exc_tb(tb - Traceback), трассировка, или же сообщение проще об ошибке
#         # exc_type - это ясно что тип ошибки
#         # exc_val - value - значение(экземпляр исключения Exception)


# v1 = [1, 2, 3]
# v2 = [4, 5]

# try:
#         with DefenedVector(v1) as dv:
#                 for i, a in enumerate(dv):
#                         dv[i] += v2[i]
# except:
#         print('Ошибка')

# print(v1)


#  АВТОТЕСТЫ

# import requests
# result = requests.get(url)
# result.status_code
# result.encoding = 'utf-8'
# result.text
# result.json()
# result = requests.post(url, json=req_json)
# result = requests.put(url, json=req_json)
# result = requests.delete(url, json=req_json)


# PyTest
# Файл с тестом должен начинаться со слова 'test_'
# Функции с тестами должны начинаться с 'test_'
# conftest.py -- технический файл
# import pytest

# @pytest.fixture() #действия до
# def set_up():
#         print('Вход в систему выполнен')
# def  test_sending_mail_1(set_up):
#         print('Письмо отправлено')

# Консольные команды :
# Перейти в папку с тестами cd ./название папки
# pytest
# -s
# -v

# yield -- все что после него -- происходит после выполнения теста

# @pytest.fixture(scope='module') #действия до модуля
# def some():
#         print('Начало')
#         yield # весь модуль
#         print('Конец') # все что после модуля

# @pytest.mark.run(order=6) -- декоратор очередности


def test1(arr, value):
    for element in arr:
        if isinstance(arr.get(element), dict):
            test1(arr.get(element), value)
        else:
            if element == value:
                arr.get(value)
