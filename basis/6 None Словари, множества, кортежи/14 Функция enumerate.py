# a = [10, 20, 30, 40]

# print(list(enumerate(a)))

# for para in enumerate(a):
#     print(para)

#
# for index, value in enumerate(a):
#     print(index, value)


# for index, value in enumerate(range(10), 100):
#     print(index, value)


"""Перед вами имеется список words
Ваша задача на основании создать список кортежей words_with_position,
# каждый элемент-кортеж должен содержать два значения: само слово и его порядковый номер в списке words"""
# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
#          'drop', 'produce', 'acquisition', 'cheap', 'strength',
#          'master', 'perception', 'noise', 'strange', 'am']
#
# words_with_position = [(value, index) for index, value in enumerate(words, 1)]
# print(words_with_position)


"""Перед вами кортеж english_words
При помощи enumerate обойдите слова этой коллекции и для каждого элемента выведите строку вида
Word № {number} = {word}"""
english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for index, word in enumerate(english_words, 1):
    print(f'Word № {index} = {word}')
