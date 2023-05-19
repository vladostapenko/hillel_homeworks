# Створити декоратор який вимірює час виконання функції
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконана за {execution_time} секунд")
        return result
    return wrapper


@measure_time
def my_function():
    time.sleep(4)


my_function()
