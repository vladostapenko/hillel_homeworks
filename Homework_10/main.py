from Task_1 import measure_time
from Task_2 import log_result


@measure_time
@log_result
def sum_args(*args):
    result = sum(args)
    return result


if __name__ == '__main__':
    sum_args(1, 2, 3, 4, 5)
    sum_args(10, 20, 30)
