# sort метод списка и он изменяет список
#
# sorted() сортирует все итерабельные аргументы, передаваевый агрумент не меняет, но возвращает отсортированный список


heroes = {
    'Spider-Man': 80,
    'Batman': 65,
    'Superman': 85,
    'Wonder Woman': 70,
    'Flash': 70,
    'Iron Man': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Captain America': 65,
    'Hulk': 87,
}

for k, v in sorted(heroes.items(),
                   key=lambda item: (item[1], item[0])):
    print(k, v)
