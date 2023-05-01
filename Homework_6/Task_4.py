# Напишіть функцію change_list, яка приймає список і змінює місця його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи.

def change_list(user_list):
    if len(user_list) < 2:
        print('You entered less than 2 characters!')
        return user_list
    temporary_variable = user_list[0]
    user_list[0] = user_list[-1]
    user_list[-1] = temporary_variable
    return user_list


print(change_list([1, 2, 3, 4, 5, 'test']))


