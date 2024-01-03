import json
from datetime import datetime
from pprint import pprint
from random import randint

str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Елизавета",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg",
                "sharing": true,
                "use": null
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
"""

data = json.loads(str_json)
for item in data["response"]["items"]:
    del item["id"]
    item["likes"] = randint(100, 200)
    item['a'] = None
    item['now'] = datetime.now().strftime('%d/%m/%y')

new_json = json.dumps(data, indent=2)
print(new_json)

with open('my_json', 'w') as file:
    json.dump(data, file, indent=3)

with open('my_json', 'r') as file:
    data = json.load(file)
pprint(data)
print(type(data))
