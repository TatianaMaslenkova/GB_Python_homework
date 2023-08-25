import csv

"""
Создайте класс студента. Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
(Допустим, что у каждого ученика по каждому предмету на одну оценку приходится один результат теста. Тогда код 
срабатывает корректно и для каждого ученика создаётся отдельный csv файл с красивым представлением в формате, который 
обсуждался на семинаре. Но если на 1 оценку приходится 2 результата теста, код срабатывает неправильно. Уточните, 
пожалуйста, как это исправить. Мне кажется, что решение проблемы в первой части метода save_data_to_journal, а именно 
в работе со словарями оценок и результатов теста. Не могу понять как прописать в коде, что если, например, мы не вносим 
оценку по предмету, но вносим рез-т теста, это должно прописаться отдельной строкой, где поле с оценкой будет пустым, 
а с рез-ом теста - заполненным. Несколько раз переписывала код, но безуспешно... Может, вы свежим взглядом заметите
где именно нужно внести исправление. Помогите, пожалуйста, если сможете. Заранее благодарю.)
"""


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
        if subject not in self.subjects:
            raise ValueError(f'Предмета {subject} нет в списке!')
        if grade < 2 or grade > 5:
            raise ValueError('Оценка должна быть от 2 до 5!')
        self.subject_grades[subject].append(grade)

    def add_test_score(self, test_res, subject):
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
        names = []
        subjects = []
        grades = []
        tests = []
        for key in self.subject_grades.keys():
            values = self.subject_grades.get(key)
            for value in values:
                if value:
                    names.append(self.name)
                    subjects.append(key)
                    grades.append(value)
        for k in self.test_scores.keys():
            values = self.test_scores.get(k)
            for val in values:
                if val:
                    tests.append(val)

        res_line = []
        for name, subject, grade, test in zip(names, subjects, grades, tests):
            line = [name, subject, grade, test]
            res_line.append(line)

        with open(f'{self.name}_beaut_csv.csv', "w", newline='', encoding="UTF-8") as csv_w_file:
            csv_writer = csv.writer(csv_w_file, dialect="excel-tab", delimiter='|', quoting=csv.QUOTE_MINIMAL)
            header = ['full_name', 'subject', 'grade', 'test_score']
            csv_writer.writerow(header)
            for line in res_line:
                csv_writer.writerow(line)


student1 = Student("Петров Петр Петрович")

student1.add_grade(5, 'Математика')
student1.add_grade(4, 'Литература')
student1.add_grade(5, 'ОБЖ')
student1.add_grade(3, 'Руcский язык')
student1.add_grade(5, 'Физика')
student1.add_grade(4, 'Английский язык')
student1.add_grade(5, 'Биология')
student1.add_grade(4, 'Химия')
student1.add_grade(4, 'Математика')
student1.add_test_score(80, 'Математика')
student1.add_test_score(70, 'Литература')
student1.add_test_score(75, 'Руcский язык')
student1.add_test_score(70, 'Английский язык')
student1.add_test_score(85, 'Химия')
student1.add_test_score(100, 'ОБЖ')
student1.add_test_score(65, 'Физика')
student1.add_test_score(55, 'Биология')
# student1.add_test_score(100, 'Руcский язык')
student1.add_test_score(100, 'Математика')
# student1.add_test_score(88, 'Физика')

student1.save_data_to_journal()  # запись в журнал

student2 = Student("Яковлев Яков Яковлевич")

student2.add_grade(4, 'Математика')
student2.add_grade(3, 'Литература')
student2.add_grade(5, 'ОБЖ')
student2.add_grade(5, 'Руcский язык')
student2.add_grade(5, 'Физика')
student2.add_grade(3, 'Физика')
student2.add_grade(4, 'Биология')
student2.add_grade(4, 'Химия')
student2.add_grade(5, 'Математика')
student2.add_test_score(90, 'Математика')
student2.add_test_score(50, 'Литература')
student2.add_test_score(90, 'Руcский язык')
student2.add_test_score(70, 'Химия')
student2.add_test_score(90, 'ОБЖ')
student2.add_test_score(70, 'Физика')
student2.add_test_score(45, 'Биология')
student2.add_test_score(90, 'Математика')
student2.add_test_score(60, 'Физика')

student2.save_data_to_journal()  # запись в журнал

print(student1.all_subjects_average_grade())
print(student1.subject_average_test_score('Математика'))

print(student2.all_subjects_average_grade())
print(student2.subject_average_test_score('Физика'))

# student3 = Student("Иванов1 Иван2 Иванович3")  # невалидные ФИО
# student4 = Student("Иванов иван иванович") # невалидные ФИО
# student1.add_grade(10, 'Биология')   # невалидная оценка
# student1.add_test_score(105, 'Физика')  # невалидные баллы
# student1.add_test_score(5, 'История')   # невалидный предмет
