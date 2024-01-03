# def hello_word():
#     print('asdasd')
#
#
# def keanu_reeves():
#     print("YOU'RE BREATHTAKING")
#
#
# def say_hello_world(name: str) -> None:
#     print(f"{name} говорит hello world!")
#
#
# def summa_n(t: int) -> None:
#     s = sum(range(1, t + 1))
#     print(f"Я знаю, что сумма чисел от 1 до {t} равна {s}")
#
#
# def exponentiation(n: int) -> None:
#     print(n ** 2, n ** 3)
#
#
# def sum_num(string: str | int) -> None:
#     print(sum([int(i) for i in string if i.isdigit()]))
#
#
# def get_body_mass_index(weight: int, height: int) -> None:
#     "Описание задачи"
#     index = weight / ((height / 100) ** 2)
#     if index < 18.5:
#         print("Недостаточная масса тела")
#     elif index > 25:
#         print("Избыточная масса тела")
#     else:
#         print("Норма")
#
#
# # assert 200 > 100
# # assert [100] * 4 < [100, 100, 100, 10000]
# # assert sum([1, 3, 5]) == sum([6, 3])
# # assert max(3, -1, 9) != -1
# # print('Проверки пройдены')
#
#
# value = 10
#
#
# def foo():
#     value = 5
#     global value
#     value += 1
#
#
# print(value)

#
# def replace(text: str, old: str, new: str = ''):
#     if old in text:
#         text = text.replace(old, new)
#     return text
#
# replace('Нет', 'т')


# def is_person_teenager(age: int) -> bool:
#     if 12 <= age <= 17:
#         return True
#     else:
#         return False
#
#
# def factorial(n:int)->int:
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def find_duplicate(x: list) -> list:
    y = []
    for i in range(len(x)):
        if x.count(x[i]) >= 2 and y.count(x[i]) < 1:
            y.append(x[i])
    return y
