# import turtle
#
#
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)
#
#
# def draw_square(a, color=None):
#     if color:
#         turtle.color(color)
#         turtle.begin_fill()
#         for i in range(4):
#             move(a)
#         turtle.end_fill()
#     else:
#         for i in range(4):
#             move(a)
#
#
#
# draw_square(60, 'red')
# turtle.goto(150, 150)
# draw_square(120, 'blue')


# def repeat_please_n_times(n: int) -> None:
#     for i in range(n):
#         print("Just do it")


# def is_between(name, surname, middlename):
#     if surname <= name <= middlename or middlename <= name <= surname:
#         print('True')
#     else:
#         print('False')
#
#
# # считываем данные
# a, b, c = map(int, input().split())
#
# # вызываем функцию
# is_between(a, b, c)


# def count_letter(text, letter):
#     count = 0
#     for i in text:
#         if i == letter:
#             count += 1
#     print(count)


def print_initials(name: str, surname: str, middlename: str) -> None:
    print(f"{surname.title()} {name[0].upper()}.{middlename[0].upper()}.")
