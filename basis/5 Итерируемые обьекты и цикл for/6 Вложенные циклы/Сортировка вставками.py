"""Программа получает на вход число n - количество элементов в списке,
и затем в следующей строке сам список.
Ваша задача отсортировать список по возрастанию при помощи сортировки вставками,
в случае если элементы соседние совпадают менять их ненужно.
В качестве ответа нужно вывести отсортированный список."""

n = int(input())
numbers = list(map(int, input().split()))