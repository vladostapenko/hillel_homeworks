import argparse
from Task_1 import quadratic_equation


def main():
    # Створення парсеру
    parser = argparse.ArgumentParser(description='Quadratic Equation Solver')
    parser.add_argument('-a', type=float, default=0, help='coefficient a (default: 0)')
    parser.add_argument('-b', type=float, required=True, help='coefficient b')
    parser.add_argument('-c', type=float, required=True, help='coefficient c')

    args = parser.parse_args()

    # Розрахунок корнів
    roots = quadratic_equation(args.a, args.b, args.c)
    if roots is None:
        print('No real roots')
    elif isinstance(roots, float):
        print('One root:', roots)
    else:
        print('Two roots:', roots[0], 'and', roots[1])


if __name__ == '__main__':
    main()

# Для запуску help ->  python main.py --help
# Для запуску програми ->  python main.py -a={} -b={} -c={}, де замість {} - числа


