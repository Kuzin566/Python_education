cities = {
    "moscow": 495,
    "saint petersburg": 812,
    "penza": 8412
}
# print(cities)
# print(type(cities))

# cities = dict(moskva=495, piter=812, penza=8412)
# print(cities)
# print(type(cities))

# a = [['moskva', 495], ['piter', 812], ['penza', 8412]]
# cities = dict(a)
# print(cities)
# print(type(cities))

# q = dict.fromkeys(['a', 'b', 'c'], 50)
# print(q)

# del cities['penza']
# cities.__delitem__('moscow')
# print(cities)

# print(cities.setdefault(6, True))
# a = cities.pop('penza')
# print(a)
# print(cities)
#
# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# # print(sweet['name'])
# # print(sweet['calories'])
# # print(sweet['id'])
# sweet.pop('ppu')
# sweet.pop('type')
# print(sweet)

#
# user = {
#   "id": 1614,
#   "uid": "ed690244-94f3-41ac-82d8-cc2c63a18ed2",
#   "password": "Coc0f2A3in",
#   "first_name": "Lucien",
#   "last_name": "Langworth",
#   "username": "lucien.langworth",
#   "email": "lucien.langworth@email.com",
#   "gender": "Female",
#   "phone_number": "+371 296-827-8753 x737",
#   "social_insurance_number": "609088166",
#   "date_of_birth": "1993-10-14",
# }
#
# print('username' in user)
# print('u id' in user)
# print('pasword' not in user)
# print('phone_number' not in user)
#
#
# address = {}
# print('zip_code' in address)
# print('longitude' in address)
# print('post_code' in address)
# print('street_name' in address)
# print('number_house' in address)

# currencies = {'rub': 1}
# currency = str(input())
# print(currencies.get(currency, f'Нет данных по {currency}'))


# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
#
# keys = [key for key in account]
# print(keys)

# a = {1: "one", 2: "two"}
# b = {2: "dva", 3: "three"}
# c = {3: "tri", 4: "four"}
#
# result = a | b | c
# print(result)

# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
#
# d2.update(d1)
# print(d2)


# workers = {
#     'employer1': {'name': 'Jhon', 'salary': 7500},
#     'employer2': {'name': 'Emma', 'salary': 8000},
#     'employer3': {'name': 'Brad', 'salary': 500}
# }
# workers['employer3']['salary'] = 8500
# print(workers)


# s = input()
# d = {}
# for i in s.lower():
#      if i.isalpha():
#         d[i] = d.get(i, 0) + 1
# print(d)


supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
total = []
for i in supermarket:
    total.append(supermarket[i]['quantity'] * supermarket[i]['price'])
print(sum(total))
