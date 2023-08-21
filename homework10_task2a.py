from math import sqrt

"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите
функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный. Используйте комплексные
числа для извлечения квадратного корня.
"""


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = b ** 2 - 4 * a * c

    def solution(self):

        if self.a == 0 and self.b == 0 and self.c == 0:
            return f'Корней бесконечное множество'
        elif self.a == 0 and self.b == 0:
            return f'Корней нет'
        else:
            if self.a == 0:
                x = - self.c / self.b
                return f'Один корень x = {round(x, 2)}'

            if self.b == 0 and self.c == 0:
                return f'Это уравнение имеет один корень x = 0'

            if self.a != 0 and self.b == 0 and self.c != 0:
                if ((- self.c) / self.a) < 0:
                    return f'Корней нет'
                elif ((-self.c) / self.a) > 0:
                    solution = abs(self.c / self.a) ** 0.5
                    x1 = solution
                    x2 = -solution
                    return f'Два корня: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}'

            if self.a != 0 and self.b != 0 and self.c == 0:
                return f'Два корня: x1 = 0, x2 = {(round((-self.b / self.a), 2))}'

            if self.a != 0 and self.b != 0 and self.c != 0:
                if self.d < 0:
                    real_part = round(-self.b / (2 * self.a), 2)
                    imaginary_part = round(sqrt(abs(self.d)) / (2 * self.a), 2)
                    x1 = complex(real_part, imaginary_part)
                    x2 = complex(real_part, -imaginary_part)
                    return f'Два корня: x1 = {x1}, x2 = {x2}'
                elif self.d == 0:
                    sol = -self.b / (2 * self.a)
                    return f'Один корень: x = {(round(sol, 2))}'
                else:
                    x1 = (-self.b + self.d ** 0.5) / (2 * self.a)
                    x2 = (-self.b - self.d ** 0.5) / (2 * self.a)
                    case1 = min(x1, x2)
                    case2 = max(x1, x2)

                    if case1 != case2:
                        return f'Два корня: x1 = {(round(case1, 2))}, x2 = {(round(case2, 2))}'
                    else:
                        return f'Один корень: x = {(round(case1, 2))}'


a = float(input('Решим квадратное уравнение. Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
equation = QuadraticEquation(a, b, c)
print(equation.solution())
