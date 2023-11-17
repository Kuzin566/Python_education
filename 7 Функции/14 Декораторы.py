# def header(func):
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h1>')
#
#     return inner
#
#
# def table(func):
#     def inner(*args, **kwargs):
#         print('<table>')
#         func(*args, **kwargs)
#         print('</table>')
#
#     return inner
#
#
# @table  # say = table(header(say))
# @header  # say = header(say)
# def say(name, surname, age):
#     print('hello', name, surname, age)
#
#
# say('Vasya', 'Ivanov', 30)

"""Напишите декоратор text_decor, который оборачивает 
вызов декорированной функции фразами «Hello» и «Goodbye!»: фраза «Hello» печатается до вызова, 
фраза «Goodbye!» - после"""

#
# def text_decor(func):
#     def inner(*args):
#         print('Hello')
#         func(*args)
#         print('Goodbye!')
#
#     return inner
#
#
# @text_decor
# def simple_func():
#     print('I just simple python func')
#
#
# simple_func()

"""Напишите декоратор repeater, который дважды вызывает декорированную функцию"""

#
# def repeater(func):
#     def inner(*args):
#         func(*args)
#         func(*args)
#
#     return inner


"""Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции"""

#
# def double_it(func):
#     def inner(*args):
#         return func(*args) * 2
#
#     return inner
#
#
# @double_it
# def multiply(num1, num2):
#     return num1 * num2
#
#
# res = multiply(9, 4)  # произведение 9*4=36, но декоратор double_it удваивает это значение
# print(res)
