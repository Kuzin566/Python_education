from string import punctuation

# file = open('111.txt', 'a+', encoding='utf-8')
# # print(file.read())
# # file.seek(0)
# # print(file.readline())
# # print(file.readline())
# file.write('\nhello')
# file.seek(0)
#
# for row in file:
#     print(row)


# def file_read(file_name: str) -> None:
#     file = open(file_name, 'r', encoding='utf-8')
#     print(file.read())
#

# def file_n_lines(file_name: str, n: int) -> None:
#     file = open(file_name, 'r', encoding='utf-8')
#     rows = file.readlines()
#     for row in range(n):
#         print(rows[row].strip())
#
# file_n_lines('111.txt', 3)


# def create_file_with_numbers(n: int) -> None:
#     with open(f'range_{n}.txt', 'a') as file:
#         for number in range(1, n + 1):
#             file.write(f'{number}\n')
#
#
# create_file_with_numbers(5)
#
#
# def remove_punctuations(word):
#     for punct in punctuation:
#         if punct in word:
#             word = word.replace(punct, "")
#     return word
#
#
# def longest_word_in_file(file_name):
#     """return the longest word"""
#     file = open(file_name, "r", encoding="utf-8")
#     max_word = ""
#     for line in file:
#         words = line.split()
#         for word in words:
#             word_without_punct = remove_punctuations(word)
#             if len(word_without_punct) >= len(max_word):
#                 max_word = word_without_punct
#
#     return max_word


count = 0
sum_numbers = []
with open('numbers.txt', 'r') as file:
    for row in file:
        if len(row.strip()) == 3:
            count += 1
        if len(row.strip()) == 2:
            sum_numbers.append(int(row))

print(count)
print(sum(sum_numbers))