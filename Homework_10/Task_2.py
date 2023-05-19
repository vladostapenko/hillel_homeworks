# Створити декоратор який кожен раз буде записувати у файл результат роботи якоїсь функції після її виклику
# (наприклад функція яка прораховує суму всіх переданих аргументів *args). Запис в файл формату
# ""Function launched at {час запуску} with result {результат роботи функції}
import datetime


def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Function launched at {current_time} with result {result}\n"

        with open("log.txt", "a") as file:
            file.write(log_message)

        return result

    return wrapper


@log_result
def sum_args(*args):
    result = sum(args)
    return result


sum_args(1, 2, 3, 4, 5)
sum_args(100, 200, 300)

