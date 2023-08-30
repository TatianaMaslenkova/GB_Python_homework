import csv
import doctest
from homework14_task2_code import Student


class NameValidator:

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять!')

    def __set__(self, instance, value):
        if not all(map(lambda val: val.isalpha(), value.split())):
            raise TypeError(f'Значение "{value}" должно содержать только буквы!')
        if not all(map(lambda val: val.istitle(), value.split())):
            raise TypeError(f'Значение "{value}" должно начинаться с заглавной буквы!')
        setattr(instance, self.param_name, value)


class Student:
    name = NameValidator()

    def __init__(self, name):
        """
        Initializes a new Student with a name and subjects loaded from a CSV file.
        >>> student1 = Student("Андреев Андрей Андреевич")
        >>> student1.name
        'Андреев Андрей Андреевич'
        >>> student2 = Student("Иванов1 Иван2 Иванович3")
        Traceback (most recent call last):
        ...
        TypeError: Значение "Иванов1 Иван2 Иванович3" должно содержать только буквы!
        >>> student3 = Student("Иванов иван иванович")
        Traceback (most recent call last):
        ...
        TypeError: Значение "Иванов иван иванович" должно начинаться с заглавной буквы!
        """
        self.name = name
        self.subject_grades: dict[str, list] = {}
        self.test_scores: dict[str, list] = {}
        self.subjects = []

        with open('subjects_list.csv', 'r', encoding='utf8') as csv_read:
            subjects = csv.reader(csv_read, delimiter="\n")
            for item in subjects:
                self.subject_grades[item[0]] = []
                self.test_scores[item[0]] = []
                self.subjects.append(''.join(item))

    def add_grade(self, grade, subject):
        """
        Method adds grade to the subject grades list.
        >>> student1 = Student("Андреев Андрей Андреевич")
        >>> student1.add_grade(10, 'Биология')
        Traceback (most recent call last):
        ...
        ValueError: Оценка должна быть от 2 до 5!
        """
        if subject not in self.subjects:
            raise ValueError(f'Предмета {subject} нет в списке!')
        if grade < 2 or grade > 5:
            raise ValueError('Оценка должна быть от 2 до 5!')
        self.subject_grades[subject].append(grade)

    def add_test_score(self, test_res, subject):
        """
        Method adds test score to the subject test scores list.
        >>> student4 = Student("Васильев Василий Васильевич")
        >>> student4.add_test_score(125, 'Физика')
        Traceback (most recent call last):
        ...
        ValueError: Результат теста должен быть от 0 до 100!
        >>> student4 = Student("Васильев Василий Васильевич")
        >>> student4.add_test_score(5, 'История')
        Traceback (most recent call last):
        ...
        ValueError: Предмета История нет в списке!
        """
        if subject not in self.subjects:
            raise ValueError(f'Предмета {subject} нет в списке!')
        if test_res < 0 or test_res > 100:
            raise ValueError('Результат теста должен быть от 0 до 100!')
        self.test_scores[subject].append(test_res)

    def subject_average_test_score(self, subject):
        if not len(self.test_scores[subject]):
            res = 0
        else:
            res = sum(self.test_scores[subject]) / len(self.test_scores[subject])
        return f'Средний балл ученика {self.name} по тестам по предмету {subject}: {res:.2f}'

    def all_subjects_average_grade(self):
        grades_list = []
        count = 0
        for grade in self.subject_grades.values():
            if grade:
                for el in grade:
                    grades_list.append(el)
                    count += 1
        if not grades_list:
            return 0
        return f'Общий средний балл ученика {self.name} по всем предметам: {sum(grades_list) / count:.2f}'

    def save_data_to_journal(self):
        dct = {}
        for subject in self.subjects:
            grades = self.subject_grades[subject]
            test = self.test_scores[subject]
            dct[subject] = f'grades:{grades}', f'test:{test}'
        with open(f'{self.name}.csv', "w", newline='', encoding="UTF-8") as csv_w_file:
            csv_writer = csv.writer(csv_w_file, dialect="excel-tab", delimiter='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(dct.keys())
            csv_writer.writerow(dct.values())


if __name__ == '__main__':
    doctest.testmod(verbose=True)
