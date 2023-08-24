import numpy as np

"""
Создайте класс Матрица. Добавьте методы для: - вывода на печать, сравнения, сложения, *умножения матриц
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return f'Матрицы разных размеров, поэтому сравнить невозможно\n'
        else:
            result = np.array_equal(self.matrix, other.matrix)
            if result:
                return True
            return False

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return f'Матрицы разных размеров, поэтому сложить невозможно\n'
        else:
            res_matrix = np.add(self.matrix, other.matrix)
            return Matrix(res_matrix)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            return f'Матрицы нельзя перемножить\n'
        else:
            res_matrix = np.matmul(self.matrix, other.matrix)
            return Matrix(res_matrix)

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
