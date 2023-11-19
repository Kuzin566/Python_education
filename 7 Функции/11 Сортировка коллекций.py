# sort метод списка и он изменяет список
#
# sorted() сортирует все итерабельные аргументы, передаваевый агрумент не меняет, но возвращает отсортированный список


# heroes = {
#     'Spider-Man': 80,
#     'Batman': 65,
#     'Superman': 85,
#     'Wonder Woman': 70,
#     'Flash': 70,
#     'Iron Man': 65,
#     'Thor': 90,
#     'Aquaman': 65,
#     'Captain America': 65,
#     'Hulk': 87,
# }
#
# for k, v in sorted(heroes.items(),
#                    key=lambda item: (item[1], item[0])):
#     print(k, v)


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
#
# for k in sorted(subject_marks, key=lambda i: (-i[1], i[0])):
#     print(k[0], k[1])

#
# orders = [i.split(': ') for i in iter(input, 'конец')]
# orders = {i[0]: i[1] for i in orders}
# for key in sorted(orders.items(), key=lambda i: int(i[1]), reverse=True):
#     print(key[0])


n = int(input())
names = []
for i in range(n):
    names.append(str(input()))
dict_names = {}
for name in names:
    if name in dict_names:
        dict_names[name] += 1
    else:
        dict_names[name] = 1

z = sorted(dict_names.items(), key=lambda x: x[1], reverse=True)

print(f"{z[0][0]}, {z[0][1]}")
print(f"{z[len(z) - 1][0]}, {z[len(z) - 1][1]}")
