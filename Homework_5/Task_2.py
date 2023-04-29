# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора
# (як мінімум + і -) та іншого числа, розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()
#  a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
#  b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)).
#     Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
#  c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError


class FormulaError(Exception):
    pass


formula = input('Enter your formula, presented as number, operator, number separated by space: ').split()

if len(formula) != 3:
    raise FormulaError('Entered formula is less than 3 characters!')

try:
    num1 = float(formula[0])
    num2 = float(formula[2])
except ValueError:
    raise FormulaError('Incorrect data, enter digit!')

if formula[1] not in ('+', '-', '*', '/'):
    raise FormulaError('You enter wrong operator, valid operators are +, -, *, /')

if formula[1] == '+':
    result = num1 + num2
elif formula[1] == '-':
    result = num1 - num2
elif formula[1] == '*':
    result = num1 * num2
elif formula[1] == '/':
    result = num1 / num2

print(f'Result is: {result}')
