import numpy as np

"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с
выводом подробной информации. Поднимайте исключения внутри основного кода.
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
        return f'Матрицы разных размеров, поэтому операция не может быть выполнена!\n'


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        try:
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                               len(other.matrix[0]))
            else:
                result = np.array_equal(self.matrix, other.matrix)
                if result:
                    return True
                return False
        except MatrixCompatibilityError as e:
            return e

    def __add__(self, other):
        try:
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                               len(other.matrix[0]))
            else:
                res_matrix = np.add(self.matrix, other.matrix)
                return Matrix(res_matrix)
        except MatrixCompatibilityError as e:
            return e

    def __mul__(self, other):
        try:
            if len(self.matrix[0]) == len(other.matrix):
                res_matrix = np.matmul(self.matrix, other.matrix)
                return Matrix(res_matrix)
            else:
                raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                               len(other.matrix[0]))
        except MatrixCompatibilityError as e:
            return e

    def __str__(self):
        matrix = ''
        for i in range(len(self.matrix)):
            matrix += str(self.matrix[i]) + '\n'
        return matrix


m1 = np.random.randint(1, 10, (3, 3))
matrix1 = Matrix(m1)
m2 = np.random.randint(1, 10, (3, 2))
matrix2 = Matrix(m2)
m3 = m2
matrix3 = Matrix(m3)
m4 = np.random.randint(1, 10, (3, 3))
matrix4 = Matrix(m4)
m5 = np.random.randint(1, 10, (2, 3))
matrix5 = Matrix(m5)
print(f'matrix1:\n{matrix1}')
print(f'matrix2:\n{matrix2}')
print(f'matrix3:\n{matrix3}')
print(f'matrix4:\n{matrix4}')
print(f'Cравнение матриц 1 и 2: {matrix1 == matrix2}')
print(f'Cравнение матриц 2 и 3: {matrix2 == matrix3}\n')
print(f'Сложение матриц 1 и 4:\n{matrix1 + matrix4}')
print(f'Сложение матриц 2 и 4:\n{matrix2 + matrix4}')
print(f'Умножение матриц 1 и 2:\n{matrix1 * matrix2}')
print(f'Умножение матриц 1 и 4:\n{matrix1 * matrix4}')
print(f'Умножение матриц 1 и 5:\n{matrix1 * matrix5}')
