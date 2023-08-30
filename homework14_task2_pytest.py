import pytest
from homework14_task2_code import Student


def test_1():
    assert Student("Андреев Андрей Андреевич").name == 'Андреев Андрей Андреевич', 'Ошибка тест 1'


def test_2():
    with pytest.raises(TypeError):
        Student("Иванов1 Иван2 Иванович3")


def test_3():
    with pytest.raises(TypeError):
        Student("Иванов иван иванович")


def test_4():
    with pytest.raises(ValueError):
        Student("Андреев Андрей Андреевич").add_grade(10, 'Биология')


def test_5():
    with pytest.raises(ValueError):
        Student("Васильев Василий Васильевич").add_test_score(125, 'Физика')


def test_6():
    with pytest.raises(ValueError):
        Student("Васильев Василий Васильевич").add_test_score(5, 'История')


if __name__ == '__main__':
    pytest.main(['-v'])
