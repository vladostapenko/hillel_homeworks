#  Дано натуральне число N. Виведіть слово YES, якщо число N є точним ступенем двійки,
#  або слово NO інакше. 8 - YES, 3 - NO

required_number = int(input('Enter the number: '))
if required_number & (required_number - 1) == 0:
    print('YES')
else:
    print('NO')