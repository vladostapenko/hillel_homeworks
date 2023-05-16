# Знайти ідентифікатор групи, де знаходиться найбільша кількість жінок, народжених після 1977 року. Як відповідь
# необхідно вказати через пробыл ідентифікатор знайденої групи і скільки в ній було жінок, народжених після 1977 року.
# Файл group_people.json

import json


with open('group_people.json', 'r') as f:
    data = json.load(f)

max_female_quantity = 0
max_group_id = None


try:
    for group in data:
        quantity = 0

        for person in group['people']:
            if person['gender'] == 'Female' and person['year'] > 1977:
                quantity += 1

        if quantity > max_female_quantity:
            max_female_quantity = quantity
            max_group_id = group['id_group']

    print(f'В групі {max_group_id} знаходиться {max_female_quantity} жінок.')

except json.JSONDecodeError as error:
    print('Помилка в json документі!', error)


