import numpy as np

"""
Создайте класс Матрица. Добавьте методы для: - вывода на печать, сравнения, сложения, *умножения матриц
"""


class BasedExep(Exception):
    pass


class MatrixCompatibilityError(BasedExep):
    def __init__(self, m1, n1, m2, n2):
        self.m1 = m1
        self.n1 = n1
        self.m1 = m2
        self.n2 = n2

    def __str__(self):
        return f'Матрицы разных размеров, поэтому операция не может быть выполнена!'


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                           len(other.matrix[0]))
        else:
            result = np.array_equal(self.matrix, other.matrix)
            if result:
                return True
            return False

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                           len(other.matrix[0]))
        else:
            res_matrix = np.add(self.matrix, other.matrix)
            return Matrix(res_matrix)

    def __mul__(self, other):
        if len(self.matrix[0]) == len(other.matrix):
            res_matrix = np.matmul(self.matrix, other.matrix)
            return Matrix(res_matrix)
        else:
            raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                           len(other.matrix[0]))

    def __str__(self):
        matrix = ''
        for i in range(len(self.matrix)):
            matrix += str(self.matrix[i]) + '\n'
        return matrix


if __name__ == '__main__':
    m1 = Matrix(np.random.randint(1, 2, (3, 3)))
    m2 = Matrix(np.random.randint(1, 2, (3, 3)))
    print(m1 == m2)
    m1 = Matrix(np.random.randint(1, 10, (3, 3)))
    m2 = Matrix(np.random.randint(1, 10, (3, 3)))
    print(m1 == m2)
    m1 = Matrix(np.random.randint(1, 2, (3, 3)))
    m2 = Matrix(np.random.randint(1, 2, (3, 3)))
    print(m1 + m2)
    m1 = Matrix(np.random.randint(2, 3, (3, 3)))
    m2 = Matrix(np.random.randint(1, 2, (3, 2)))
    print(m1 * m2)
    m1 = Matrix(np.random.randint(1, 10, (3, 3)))
    m2 = Matrix(np.random.randint(1, 10, (3, 2)))
    print(m1 == m2)
