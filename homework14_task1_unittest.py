import unittest
from homework14_task1_code import check_sides


class TestCaseTriangle(unittest.TestCase):

    def test_11(self):
        self.assertEqual(check_sides(5, 6, 7), 'Разносторонний треугольник')

    def test_22(self):
        self.assertEqual(check_sides(5, 5, 7), 'Равнобедренный треугольник')

    def test_33(self):
        self.assertEqual(check_sides(5, 5, 5), 'Равносторонний треугольник')

    def test_44(self):
        self.assertEqual(check_sides(15, 5, 7), 'Треугольника с такими сторонами не существует')


if __name__ == '__main__':
    unittest.main(verbosity=2)
