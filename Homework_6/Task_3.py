#  Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000, і повертає True, якщо це просте число,
#  і False в іншому випадку.

# def is_prime(number):
#     if number < 2 or number > 1000: return False
#     if number == 2 or number == 3: return True
#     if number % 2 == 0 or number < 2: return False
#     for i in range(3, int(number ** 0.5) + 1, 2):
#         if number % i == 0:
#             return False
#
#     return True
#
# print(is_prime(5))


import math


def is_prime(number):
    if number < 2 or number > 1000:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


print(is_prime(31))
