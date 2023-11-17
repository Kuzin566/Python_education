def hello_word():
    print('asdasd')


def keanu_reeves():
    print("YOU'RE BREATHTAKING")


def say_hello_world(name: str) -> None:
    print(f"{name} говорит hello world!")


def summa_n(t: int) -> None:
    s = sum(range(1, t + 1))
    print(f"Я знаю, что сумма чисел от 1 до {t} равна {s}")


def exponentiation(n: int) -> None:
    print(n ** 2, n ** 3)


def sum_num(string: str | int) -> None:
    print(sum([int(i) for i in string if i.isdigit()]))


def get_body_mass_index(weight: int, height: int) -> None:
    "Описание задачи"
    index = weight / ((height / 100) ** 2)
    if index < 18.5:
        print("Недостаточная масса тела")
    elif index > 25:
        print("Избыточная масса тела")
    else:
        print("Норма")


# assert 200 > 100
# assert [100] * 4 < [100, 100, 100, 10000]
# assert sum([1, 3, 5]) == sum([6, 3])
# assert max(3, -1, 9) != -1
# print('Проверки пройдены')


value = 10


def foo():
    value = 5
    global value
    value += 1


print(value)

