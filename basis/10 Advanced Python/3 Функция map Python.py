# a = [-1, 2, -3, 4, 5]
# b = list(map(abs, a))
# c = [abs(i) for i in a]
# print(b)
# print(c)


# def f(x):
#     return x**2
#
#
# a = [-1, 2, -3, 4, 5]
# b = list(map(f, a))
# c = [f(i) for i in a]
# print(b)
# print(c)


# a = ['hello', 'hi', 'good morning']
# b = list(map(str.upper, a))
# print(b)


# a = ['hello', 'hi', 'good morning']
# b = list(map(lambda x: x[::-1], a))
# c = [i[::-1] for i in a]
# print(b)
# print(c)

# a = [1, 2, 3, 4]
# b = list(map(lambda x: x**2, a))
# print(b)


# a = ['hello', 'hi', 'good morning']
# b = list(map(list, a))
# c = list(map(sorted, b))
# print(b)
# print(c)


"""Перед вами имеется список numbers, состоящий из целых чисел.
Ваша задача преобразовать каждый элемент списка numbers в строку и
сохранить полученный результат в новый список strings. Для преобразования используйте map
В качестве ответа выведите переменную strings"""
# numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609,
#            221, 311, 526,
#            254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121,
#            40, 278, 118, -462, -671, 78, -69, -568, -228, -445, -47, -565]

# strings = list(map(str, numbers))
# print(strings)


"""Перед вами имеется список numbers, состоящий из целых чисел. 
Ваша задача увеличить каждый элемент списка numbers втрое и сохранить 
полученный результат в новый список increase_3. Для преобразования используйте функцию map
В качестве ответа выведите переменную increase_3"""
# increase_3 = list(map(lambda x: x * 3, numbers))
# print(increase_3)


"""Напишите программу, которая возводит в квадрат и в куб каждое число из списка numbers
пользуясь при этом функциями map и lambda.

# В результате у вас должно получится два отдельных списка: в одном квадраты, в другом кубы.
#  Их необходимо вывести на экран."""
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# cub = list(map(lambda x: x ** 3, numbers))
# square = list(map(lambda x: x ** 2, numbers))
# print(square)
# print(cub)


# def from_hex_to_rgb(color: str) -> tuple:
#     red = int(color[1:3], 16)
#     green = int(color[3:5], 16)
#     blue = int(color[5:7], 16)
#     return red, green, blue
#
#
# colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
#           '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
#           '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
#           '#7CFC00', '#7FFF00', '#ADFF2F']
#
# for red, green, blue in map(from_hex_to_rgb, colors):
#     print(f"Red={red}, Green={green}, Blue={blue}")



def power(base: int, exp: int) -> int:
    return base ** exp


bases = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exponents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

result = list(map(power, bases, exponents))
print(result)
