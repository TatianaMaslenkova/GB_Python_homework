import doctest
from homework14_task1_code import check_sides


def check_sides(a, b, c):
    """
    Method compared triangles giving info on its type based on inputted sides a, b and c.
    >>> print(check_sides(5, 6, 7))
    Разносторонний треугольник
    >>> print(check_sides(5, 5, 7))
    Равнобедренный треугольник
    >>> print(check_sides(5, 5, 5))
    Равносторонний треугольник
    >>> print(check_sides(15, 5, 7))
    Треугольника с такими сторонами не существует
    """
    if a == b == c:
        return f'Равносторонний треугольник'
    elif a == b or a == c or b == c:
        return f'Равнобедренный треугольник'
    elif a > b + c or b > a + c or c > a + b:
        return f'Треугольника с такими сторонами не существует'
    else:
        return f'Разносторонний треугольник'


if __name__ == '__main__':
    doctest.testmod(verbose=True)
