n = int(input())
i = 1
a = []
while i * i <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)
total = 0
for i in a:
    total += i
print(total)

# Дано натуральное число N. Определить, является ли оно простым. Натуральное число
# N называется простым, если у него есть только два делителя: единица и само число N.
# В качестве ответа выведите "Yes", если число простое,  "No" - в противном случае.

# Получаем все делители числа
n = int(input())
i = 1
a = []
while i * i <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1

# Если в списке не 2 делителя - значит чисто не простое
if len(a) != 2:
    print('No')
else:
    print('Yes')
