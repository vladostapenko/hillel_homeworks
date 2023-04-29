# Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c), якщо дискримінант від'ємний
# викликати виняток DiscriminantError і вивести відповідне повідомлення.

class DiscriminantError(Exception):
    pass


try:
    a = float(input('Enter value a: '))
    b = float(input('Enter value b: '))
    c = float(input('Enter value c: '))

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        raise DiscriminantError('Discriminant is less than 0')

    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b + discriminant**0.5) / (2*a)
        print(f'Roots are {x1} & {x2}')

except ValueError:
    print(f"Wrong data was entered")
# except DiscriminantError:                                 # для вывода текста в логах, вместо ошибки
#     print(f"Discriminant is less than 0")



