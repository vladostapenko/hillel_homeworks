import json


with open('manager_sales.json') as file:
    data = json.load(file)


sales_sum = 0
best_manager = None


for record in data:
    manager = record['manager']
    sales = sum(car['price'] for car in record['cars'])

    if sales > sales_sum:
        sales_sum = sales
        best_manager = manager


if best_manager is not None:
    first_name = best_manager['first_name']
    last_name = best_manager['last_name']
    print(f"Найуспішніший менеджер - {first_name} {last_name}, сума продажів - {sales_sum}")
else:
    print("Неможливо знайти менеджера або данні про нього відсутні.")
