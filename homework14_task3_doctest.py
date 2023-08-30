import numpy as np
import doctest
from homework14_task3_code import Matrix


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
        """
        Method compares two matrices.
        >>> m1 = Matrix(np.random.randint(1, 2, (3, 3)))
        >>> m2 = Matrix(np.random.randint(1, 2, (3, 3)))
        >>> print(m1 == m2)
        True
        >>> m1 = Matrix(np.random.randint(1, 10, (3, 3)))
        >>> m2 = Matrix(np.random.randint(1, 10, (3, 3)))
        >>> print(m1 == m2)
        False
        >>> m1 = Matrix(np.random.randint(1, 10, (3, 3)))
        >>> m2 = Matrix(np.random.randint(1, 10, (3, 2)))
        >>> print(m1 == m2)
        Traceback (most recent call last):
        ...
        MatrixCompatibilityError: Матрицы разных размеров, поэтому операция не может быть выполнена!
        """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                           len(other.matrix[0]))
        else:
            result = np.array_equal(self.matrix, other.matrix)
            if result:
                return True
            return False

    def __add__(self, other):
        """
        Method adds two matrices.
        >>> m1 = Matrix(np.random.randint(1, 2, (3, 3)))
        >>> m2 = Matrix(np.random.randint(1, 2, (3, 3)))
        >>> print(m1 + m2)
        [2 2 2]
        [2 2 2]
        [2 2 2]
        <BLANKLINE>
        """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixCompatibilityError(len(self.matrix), len(other.matrix), len(self.matrix[0]),
                                           len(other.matrix[0]))
        else:
            res_matrix = np.add(self.matrix, other.matrix)
            return Matrix(res_matrix)

    def __mul__(self, other):
        """
        Method multiplies two matrices.
        >>> m1 = Matrix(np.random.randint(2, 3, (3, 3)))
        >>> m2 = Matrix(np.random.randint(1, 2, (3, 2)))
        >>> print(m1 * m2)
        [6 6]
        [6 6]
        [6 6]
        <BLANKLINE>
        """
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
    doctest.testmod(verbose=True)
