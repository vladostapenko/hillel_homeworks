from Task_1 import Human, SmallHouse


if __name__ == '__main__':
    Human.default_info()

    person = Human()
    person.info()

    house = SmallHouse()

    person.buy_house(house)  # Купую будинок без достатньої кількості грошей

    person.earn_money(120000)  # Збільшую кількість грошей

    person.buy_house(house, discount=0.1)  # Купую будинок зі знижкою

    person.info()  # Перевіряю оновлений стан Human
