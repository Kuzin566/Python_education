# a = ['hello', 'hi', 'asds']
# print(all(a))
# print(any(a))

# c = 100
# condition_1 = c % 2 == 1
# condition_2 = c > 150
# condition_3 = c < 10
#
# print(all([condition_1, condition_2, condition_3]))
# print(any([condition_1, condition_2, condition_3]))

# a = [1, 2, 0]
# result = any(map(lambda x: x, a))
# print(result)


"""Программе на вход поступают слова, разделенные пробелом. Ваша задача проверить, во всех ли словах есть
английская буква A вне зависимости от регистра. В качестве ответа программа должна вывести True или False."""
#
# words = list(map(str, input().split()))
# result = [True if 'a' in i.lower() else False for i in words]
# print(all(result))


"""ОЮГХТ
Кто не помнит со школьных уроков английского эту запоминашку для написания английских слов, таких как например bought.
Вашей программе на вход будут поступать слова, разделенные пробелом. Программа должна вывести True , 
если встретилось хотя бы одно слово, заканчивающееся на ought. В противном случае нужно вывести False.
Регистр букв не имеет значения, значит интересующиеся нас  
слова могут заканчиваться как на ought, так и например на OUGHT"""
words = list(map(str, input().split()))
result = [True if i.lower().endswith('ought') else False for i in words]
print(any(result))
