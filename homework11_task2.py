import numpy as np

"""
Создайте класс Матрица. Добавьте методы для: - вывода на печать, сравнения, сложения, *умножения матриц
"""


class Matrix:
    def __init__(self, start, stop, size):
        self.start = start
        self.stop = stop
        self.size = size
        self.matrix = np.random.randint(start, stop, size)

    def __eq__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return f'Матрицы разных размеров, поэтому сравнить невозможно'
        else:
            result = np.array_equal(self.matrix, other.matrix)
            if result:
                return True
            return False

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return f'Матрицы разных размеров, поэтому сложить невозможно'
        else:
            res_matrix = np.add(self.matrix, other.matrix)
            return res_matrix

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            return f'Матрицы нельзя перемножить'
        else:
            res_matrix = np.matmul(self.matrix, other.matrix)
            return res_matrix

    def __str__(self):
        matrix = ''
        for i in range(len(self.matrix)):
            matrix += str(self.matrix[i]) + '\n'
        return matrix


matrix1 = Matrix(1, 10, (3, 3))
matrix2 = Matrix(1, 10, (3, 2))
matrix3 = matrix2
matrix4 = Matrix(1, 10, (3, 3))
matrix5 = Matrix(1, 10, (2, 3))
print(f'matrix1:\n{matrix1}')
print(f'matrix2:\n{matrix2}')
print(f'matrix3:\n{matrix3}')
print(f'matrix4:\n{matrix4}')
print(f'Cравнение матриц 1 и 2: {matrix1 == matrix2}')
print(f'Cравнение матриц 2 и 3: {matrix2 == matrix3}')
print(f'Сложение матриц 1 и 4:\n{matrix1 + matrix4}')
print(f'Сложение матриц 2 и 4:\n{matrix2 + matrix4}')
print(f'Умножение матриц 1 и 2:\n{matrix1 * matrix2}')
print(f'Умножение матриц 1 и 4:\n{matrix1 * matrix4}')
print(f'Умножение матриц 1 и 5:\n{matrix1 * matrix5}')
