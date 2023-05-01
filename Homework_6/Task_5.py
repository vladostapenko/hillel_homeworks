# Напишіть функцію to_dict(lst), яка приймає аргумент у вигляді списку і повертає словник, в якому кожен елемент списку
# є ключем і значенням. Передбачається, що елементи списку відповідатимуть правилам завдання ключів у словниках.


def to_dict(lst):
    # keys = lst[:]
    # values = lst[:]
    # my_dict = dict(zip(keys, values))
    my_dict = dict(zip(lst, lst))
    return my_dict


print(to_dict([1, 2, 3, 4, 'test']))
