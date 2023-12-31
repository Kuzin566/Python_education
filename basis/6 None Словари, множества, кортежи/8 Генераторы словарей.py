from pprint import pprint

# a = {i: i**2 for i in range(1, 11)}
# print(a)


# data = {
#     'Джефф Безос': '177',
#     'ИлоН МаСк': '126',
#     'бернар АрнО': '150',
#     'БиЛл ГеЙтС': '124',
# }
# new_data = {key.title(): int(value) for key, value in data.items()}
# print(new_data)


#
# users = [
#     [0, 'Bob', 'password'],
#     [1, 'code', 'python'],
#     [2, 'Stack', 'overflow'],
#     [3, 'username', '1234'],
#     [51, 'qwerty', '1234']
# ]
# new_users = {user[0]: user for user in users}
# pprint(new_users)
# print('*' * 15)
# pprint(new_users[3])
# pprint(new_users[51])

"""Перед вами словарь user
Напишите программу для создания нового словаря, которая извлекает указанные ключи из приведенного ниже словаря.
Сами значения ключей, которые нужно извлечь, поступают на вход программе в виде одной строки разделенные пробелом
В качестве ответа выведите на экран полученный словарь"""

# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17",
#     "employment": {
#         "title": "Central Hospitality Liaison",
#         "key_skill": "Organisation"
#     },
#     "subscription": {
#         "plan": "Essential",
#         "status": "Idle",
#         "payment_method": "Debit card",
#         "term": "Annual"
#     }
# }
#
# keys = list(map(str, input().split()))
# new_data = {key: user[key] for key in keys if key in user}
# print(new_data)


"""В вашем распоряжении имеется вложенный список people, 
в котором хранятся имена и телефоны. Ваша задача создать словарь при помощи генератора словарей, 
в котором в качестве ключей будут храниться номера телефонов, а значениями будут имена владельцев. 
Обязательно сохраните этот словарь в переменной phone_book.
Выводить ничего не нужно, только правильно заполните словарь в переменной phone_book"""
people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]
phone_book = {i[1]: i[0] for i in people}
print(phone_book)
