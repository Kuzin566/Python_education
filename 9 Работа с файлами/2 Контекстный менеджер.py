import os


# with os.scandir('.') as entries:
#     for entry in entries:
#         print(entry.name, '->', entry.stat().st_size, 'bytes')
#
#
# def find_lines_len_more_6(file_name: str) -> int:
#     count = 0
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for row in file:
#             if len(row.strip()) > 6:
#                 count += 1
#     return count

#
# def primer():
#     words = set()
#     with open('lorem.txt', 'r', encoding='utf-8') as file:
#         for row in file:
#             for word in row.split():
#                 words.add(word.strip().lower())
#     return len(words)
#
#
# print(primer())


def get_dict():
    list_words = []
    words = {}
    with open('lorem.txt', 'r', encoding='utf-8') as file:
        for row in file:
            for word in row.split():
                list_words.append(word.upper())
    for word in list_words:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1
    print(words)

get_dict()
