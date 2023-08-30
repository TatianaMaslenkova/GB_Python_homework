import unittest
from homework14_task2_code import Student


class TestCaseStudent(unittest.TestCase):

    def test_11(self):
        self.assertEqual(Student("Андреев Андрей Андреевич").name, 'Андреев Андрей Андреевич')

    def test_22(self):
        self.assertRaises(TypeError, Student.__init__, "Иванов1 Иван2 Иванович3")

    def test_33(self):
        self.assertRaises(TypeError, Student.__init__, "Иванов иван иванович")

    def test_44(self):
        self.assertRaises(ValueError, Student("Андреев Андрей Андреевич").add_grade, 10, 'Биология')

    def test_55(self):
        self.assertRaises(ValueError, Student("Васильев Василий Васильевич").add_test_score, 125, 'Физика')

    def test_66(self):
        self.assertRaises(ValueError, Student("Васильев Василий Васильевич").add_test_score, 5, 'История')


if __name__ == '__main__':
    unittest.main(verbosity=2)
