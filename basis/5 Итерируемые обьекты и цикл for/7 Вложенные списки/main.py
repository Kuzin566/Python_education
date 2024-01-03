# a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=" ")
#     print()


# a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
# for i in range(len(a)):
#     s = 0
#     for j in range(len(a[i])):
#         s += a[i][j]
#     print(s)
#
#
# a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
# for j in range(4):
#     s = 0
#     for i in range(len(a)):
#         s += a[i][j]
#     print(s)

a = []
n = int(input('Введите размер квадратной матрицы: '))
for i in range(n):
    a.append([0] * n)
print(a)

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             a[i][j] = 10
#         elif i > j:
#             a[i][j] = 3
#         else:
#             a[i][j] = 5
# for i in a:
#     print(i)



# n = int(input('Введите количество строк матрицы: '))
# matrix = []
# for i in range(n):
#     matrix.append(
#         list(map(int, input(f"Введите элементы {i} строки: ").split()))
#     )
# print(matrix)
#
# print('------Вывод матрицы построчно------')
#
# for row in matrix:
#     print(row)
