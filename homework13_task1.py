"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с
выводом подробной информации. Поднимайте исключения внутри основного кода.
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого
треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
"""


class BasedExep(Exception):
    pass


class SideValueError(BasedExep):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return f'Треугольника со сторонами a = {self.side1}, b = {self.side2}, c = {self.side3} не существует!'


class TriangleExistence:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_sides(self):
        try:
            if self.a == self.b == self.c:
                return f'Равносторонний треугольник'
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return f'Равнобедренный треугольник'
            elif self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
                raise SideValueError(a, b, c)
            else:
                return f'Разносторонний треугольник'
        except SideValueError as e:
            return e


if __name__ == '__main__':
    a = float(input('Определим существование треугольника. Введите сторону a: '))
    b = float(input('Введите сторону b: '))
    c = float(input('Введите сторону c: '))
    t = TriangleExistence(a, b, c)
    print(t.check_sides())
