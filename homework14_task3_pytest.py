import numpy as np
import pytest
from homework14_task3_code import Matrix
from homework14_task3_code import MatrixCompatibilityError


@pytest.fixture
def res1():
    m4 = Matrix(np.random.randint(1, 2, (3, 3)))
    m5 = Matrix(np.random.randint(1, 2, (3, 3)))
    return m4 == m5


@pytest.fixture
def res2():
    m1 = Matrix(np.random.randint(1, 10, (3, 3)))
    m2 = Matrix(np.random.randint(1, 10, (3, 3)))
    return m1 == m2


@pytest.fixture
def res3():
    m1 = Matrix(np.random.randint(1, 10, (3, 3)))
    m3 = Matrix(np.random.randint(1, 10, (3, 2)))
    return m1, m3


@pytest.fixture
def res4():
    m4 = Matrix(np.random.randint(1, 2, (3, 3)))
    m5 = Matrix(np.random.randint(1, 2, (3, 3)))
    res_matrix = Matrix.__add__(m4, m5)
    return res_matrix


@pytest.fixture
def res5():
    m6 = Matrix(np.random.randint(2, 3, (3, 3)))
    m7 = Matrix(np.random.randint(1, 2, (3, 2)))
    res_matrix = Matrix.__mul__(m6, m7)
    return res_matrix


def test_1(res1):
    assert res1, 'Ошибка тест 1'


def test_2(res2):
    assert not res2, 'Ошибка тест 2'


def test_3(res3):
    with pytest.raises(MatrixCompatibilityError,
                       match=r'Матрицы разных размеров, поэтому операция не может быть выполнена!'):
        Matrix.__eq__(res3[0], res3[1])


def test_4(res4):
    assert res4.__str__(), '[2 2 2]\n[2 2 2]\n[2 2 2]\n'


def test_5(res5):
    assert res5.__str__(), '[6 6]\n[6 6]\n[6 6]\n'


if __name__ == '__main__':
    pytest.main(['-v'])
