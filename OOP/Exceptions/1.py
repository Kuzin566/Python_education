"""В момент Выполнения
до момента выполнения
Типы
Base Exception -> Exceptions-> и вот от этого уже класса идут подклассы"""

# print('hello')
# print('hello2')
# print('hello3')
# try:
#     int('hello')
# except ValueError:
#     print('Неправильное преобразование')
#     raise ValueError
# print('hello4')
# print('hello5')
# print('hello6')
#
# print(IndexError.__mro__)


# try:
#     assert 1 == 2, "Что-то пошло не так"
# except AssertionError as e:
#     print("Отловили AssertionError:", e)
# finally:
#     print("Досвидули")

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(str(e))
else:
    print(result)



def function_1():
    try:
        x = 1 / 0
        print('The end')
    except ZeroDivisionError:
        print("Can't divide by zero")
        raise ValueError("Oops, something went wrong")


def function_2():
    try:
        function_1()
    except ValueError as e:
        print("ValueError caught:", e)


function_2()

