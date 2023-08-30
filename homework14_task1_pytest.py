import pytest
from homework14_task1_code import check_sides


def test_1():
    assert check_sides(5, 6, 7) == 'Разносторонний треугольник', 'Ошибка тест 1'


def test_2():
    assert check_sides(5, 5, 7) == 'Равнобедренный треугольник', 'Ошибка тест 2'


def test_3():
    assert check_sides(5, 5, 5) == 'Равносторонний треугольник', 'Ошибка тест 3'


def test_4():
    assert check_sides(15, 5, 7) == 'Треугольника с такими сторонами не существует', 'Ошибка тест 4'


if __name__ == '__main__':
    pytest.main(['-v'])
