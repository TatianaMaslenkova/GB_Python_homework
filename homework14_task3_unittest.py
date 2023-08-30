import numpy as np
import unittest
from homework14_task3_code import Matrix
from homework14_task3_code import MatrixCompatibilityError


class TestCaseMatrix(unittest.TestCase):
    def setUp(self):
        self.m1 = Matrix(np.random.randint(1, 10, (3, 3)))
        self.m2 = Matrix(np.random.randint(1, 10, (3, 3)))
        self.m3 = Matrix(np.random.randint(1, 10, (3, 2)))
        self.m4 = Matrix(np.random.randint(1, 2, (3, 3)))
        self.m5 = Matrix(np.random.randint(1, 2, (3, 3)))
        self.m6 = Matrix(np.random.randint(2, 3, (3, 3)))
        self.m7 = Matrix(np.random.randint(1, 2, (3, 2)))

    def test_11(self):
        self.assertTrue(self.m4 == self.m5)

    def test_22(self):
        self.assertFalse(self.m1 == self.m2)

    def test_33(self):
        with self.assertRaises(MatrixCompatibilityError):
            Matrix.__eq__(self.m1 == self.m3)

    def test_44(self):
        res_matrix = Matrix.__add__(self.m4, self.m5)
        self.assertEqual(res_matrix.__str__(), '[2 2 2]\n[2 2 2]\n[2 2 2]\n')

    def test_55(self):
        res_matrix = Matrix.__mul__(self.m6, self.m7)
        self.assertEqual(res_matrix.__str__(), '[6 6]\n[6 6]\n[6 6]\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)
