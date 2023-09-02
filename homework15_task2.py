import argparse
import logging
from math import sqrt

"""
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный. Используйте комплексные
числа для извлечения квадратного корня.
"""

logging.basicConfig(filename='Log/log_2.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        res = "Корней бесконечное множество"
        print(res)
        logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')
    elif a == 0 and b == 0:
        res = "Корней нет"
        print(res)
        logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')
    else:
        if a == 0:
            x = - c / b
            res = f"Один корень x = {round(x, 2)}"
            print(res)
            logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')

        if b == 0 and c == 0:
            res = 'Это уравнение имеет один корень x = 0'
            print(res)
            logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')

        if a != 0 and b == 0 and c != 0:
            if ((- c) / a) < 0:
                res = 'Корней нет'
                print(res)
                logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')
            elif ((-c) / a) > 0:
                solution = abs(c / a) ** 0.5
                x1 = solution
                x2 = -solution
                res = f"Два корня: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}"
                print(res)
                logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')

        if a != 0 and b != 0 and c == 0:
            res = f"Два корня: x1 = 0, x2 = {(round((-b / a), 2))}"
            print(res)
            logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')

        if a != 0 and b != 0 and c != 0:
            d = ((b ** 2) - (4 * a * c))
            if d < 0:
                real_part = round(-b / (2 * a), 2)
                imaginary_part = round(sqrt(abs(d)) / (2 * a), 2)
                x1 = complex(real_part, imaginary_part)
                x2 = complex(real_part, -imaginary_part)
                res = f"Два корня: x1 = {x1}, x2 = {x2}"
                print(res)
                logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')
            elif d == 0:
                sol = -b / 2 * a
                res = f"Один корень: x = {(round(sol, 2))}"
                print(res)
                logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')
            else:
                x1 = (-b + d ** 0.5) / (2 * a)
                x2 = (-b - d ** 0.5) / (2 * a)
                case1 = min(x1, x2)
                case2 = max(x1, x2)

                if case1 != case2:
                    res = f"Два корня: x1 = {(round(case1, 2))}, x2 = {(round(case2, 2))}"
                    print(res)
                    logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')
                else:
                    res = f"Один корень: x = {(round(case1, 2))}"
                    print(res)
                    logger.info(f'Введённые аргументы: a = {a}, b = {b}, c = {c}. Результат работы функции: {res}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Triangle existence')
    parser.add_argument('-a', metavar='a', type=float, help='enter a for ax^2+bx+c=0', default=1)
    parser.add_argument('-b', metavar='b', type=float, help='enter b for ax^2+bx+c=0', default=0)
    parser.add_argument('-c', metavar='c', type=float, help='enter c for ax^2+bx+c=0', default=0)
    args = parser.parse_args()
    quadratic_equation(args.a, args.b, args.c)  # вводим в терминал в формате $ python homework15_task2.py -a 5 -b 20 -c -10

    # a = float(input('Решим квадратное уравнение. Введите a: '))
    # b = float(input('Введите b: '))
    # c = float(input('Введите c: '))
    # quadratic_equation(a, b, c)
