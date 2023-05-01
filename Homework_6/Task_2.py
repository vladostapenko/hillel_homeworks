# Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площа квадрата та діагональ квадрата.

import math


def square(x):
    perimeter = x * 4
    area = x ** 2
    diagonal = x * (math.sqrt(2))
    return perimeter, area, diagonal


print(square(5))