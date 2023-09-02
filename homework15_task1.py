import logging
import argparse

"""
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в
одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

logging.basicConfig(filename='Log/log_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        result = 'Ошибка! Длины сторон должны быть положительными!'
        print(result)
        logger.error(f'Введённые стороны: a = {a}, b = {b}, c = {c}. Результат: {result}')
    elif a > b + c or b > a + c or c > a + b:
        result = 'Треугольника с такими сторонами не существует'
        print(result)
        logger.info(f'Введённые стороны: a = {a}, b = {b}, c = {c}. Результат: {result}')
    else:
        if a == b == c:
            result = 'Равносторонний треугольник'
            print(result)
            logger.info(f'Введённые стороны: a = {a}, b = {b}, c = {c}. Результат: {result}')
        elif a == b or a == c or b == c:
            result = 'Равнобедренный треугольник'
            print(result)
            logger.info(f'Введённые стороны: a = {a}, b = {b}, c = {c}. Результат: {result}')
        else:
            result = 'Разносторонний треугольник'
            print(result)
            logger.info(f'Введённые стороны: a = {a}, b = {b}, c = {c}. Результат: {result}')


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Triangle existence')
    # parser.add_argument('-a', metavar='a', type=float, help='enter triangle side a', default=1)
    # parser.add_argument('-b', metavar='b', type=float, help='enter triangle side b', default=1)
    # parser.add_argument('-c', metavar='c', type=float, help='enter triangle side c', default=1)
    # args = parser.parse_args()
    # triangle(args.a, args.b, args.c) # вводим в терминал в формате $ python homework15_task1.py -a 9 -b 9 -c 8

    a = float(input('Определим существование треугольника. Введите сторону a: '))
    b = float(input('Введите сторону b: '))
    c = float(input('Введите сторону c: '))
    triangle(a, b, c)
