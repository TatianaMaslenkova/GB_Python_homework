from random import randint
import csv
from functools import wraps
import json
from math import sqrt

"""
Напишите следующие функции: 1. Нахождение корней квадратного уравнения. 2. Генерация csv файла с тремя случайными числами
в каждой строке. 100-1000 строк. 3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой
чисел из csv файла. 4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""


def create_csv_file(file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for _ in range(randint(100, 1000)):
            line = []
            for _ in range(3):
                x = 0
                while x == 0:
                    x = randint(-100, 100)
                line.append(x)
            csv_writer.writerow(line)


def read_csv_file(function):
    @wraps(function)
    def wrapper(file_name):
        results = []
        with open(file_name, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                a, b, c = map(int, row)
                results.append(function(a, b, c))
        return results

    return wrapper


def logging(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        with open('logging.json', 'a', encoding='utf-8') as json_file:
            dct = {'function_name': function.__name__, 'args': args, 'kwargs': kwargs, 'results': result}
            json.dump(dct, json_file, indent=2)
        return result

    return wrapper


@read_csv_file
@logging
def square_roots(a, b, c):
    d = ((b ** 2) - (4 * a * c))
    if d < 0:
        real_part = round(-b / (2 * a), 2)
        imaginary_part = round(sqrt(abs(d)) / (2 * a), 2)
        x1 = str(complex(real_part, imaginary_part))
        x2 = str(complex(real_part, -imaginary_part))
        return x1, x2
    elif d == 0:
        x1 = -b / 2 * a
        return round(x1, 2)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)


create_csv_file('numbers.csv')
square_roots('numbers.csv')
