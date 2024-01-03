# my_frozen = frozenset()
# print(my_frozen)


my_frozen = frozenset(int('7' * i) for i in range(1, 78))
print(len(my_frozen))
for i in my_frozen:
    print(i)
