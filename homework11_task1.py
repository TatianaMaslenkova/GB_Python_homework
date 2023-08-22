from datetime import datetime

"""
Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
"""

"""
Создайте класс Моя Строка, где: будут доступны все возможности str, дополнительно хранятся имя автора строки и время
создания (time.time)
"""


class MyStr(str):
    """
    Класс наследует все возможности класса str, в нём дополнительно хранятся
    имя автора строки и время создания.
    """

    def __new__(cls, value, author_name):
        """
        Метод создаёт экземпляр класса с доп. параметрами:
        value: Переданная строка
        author_name: имя автора-создателя
        creation_time = datetime.datetime.now() - время создания
        """
        my_srt = super().__new__(cls, value)
        my_srt.author_name = author_name
        # my_srt.creation_time = time.time()
        my_srt.creation_time = datetime.now()
        return my_srt


"""
Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, старые
данные из ранее созданных экземпляров сохраняются в пару списков-архивов, list-архивы также являются свойствами экземпляра
"""


class Archive:
    """
    Класс хранит число и строку, а также list-архивы предыдущих экземпляров класса.
    При создании нового экземпляра класса старые данные из ранее созданных экземпляров
    сохраняются в пару списков-архивов.
    """
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        """Метод содержит свойства экземпляра класса"""
        self.num = num
        self.new_str = new_str

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)

        Archive.last_num = num
        Archive.last_str = new_str

    def __str__(self):
        """Метод выводит читаемое описание экземпляра класса при выводе в консоль."""
        res = f'номер: {self.num}, строка: {self.new_str}, архив: {list(zip(self.nums_archive, self.strs_archive))} '
        return res

    def __repr__(self):
        """Метод выводит описание экземпляра класса для разработчиков."""
        return f'Archive({self.num = },{self.new_str = })'


"""
Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади Должны работать все шесть операций сравнения
"""


class Rectangle:
    """
    Класс хранит стороны прямоугольника, вычисляет периметр и площадь.
    Класс также содержит методы сложения и вычитания экземпляров и 6 операций сравнения экземпляров.
    """

    def __init__(self, side_a, side_b=0):
        """Метод содержит свойства экземпляра класса"""
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        """Метод вычисляет периметр экземпляра"""
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        """Метод вычисляет площадь экземпляра"""
        return self.side_a * self.side_b

    def __add__(self, other):
        """Метод складывает периметры экземпляров"""
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """Метод вычитает периметры экземпляров"""
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        """Метод сравнивает площади экземпляров 'равно =='"""
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        """Метод сравнивает площади экземпляров 'не равно !='"""
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        """Метод сравнивает площади экземпляров 'больше >'"""
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        """Метод сравнивает площади экземпляров 'больше или равно >='"""
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        """Метод сравнивает площади экземпляров 'метод меньше <'"""
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        """Метод сравнивает площади экземпляров 'меньше или равно <='"""
        return self.get_area() <= other.get_area()

    def __str__(self):
        result = f'Прямоугольник со сторонами {self.side_a} и {self.side_b}\nПериметр: {self.get_perimeter():.2f}\n' \
                 f'Площадь: {self.get_area():.2f}'
        return result


if __name__ == '__main__':
    s = MyStr('Новая Строка Теста', 'Sergey')
    print(f'{s}\nавтор: {s.author_name}, время создания: {s.creation_time}')
    print(s.lower())
    # print(help(MyStr))
    arc1 = Archive(1, "Строка 1")
    print(arc1)
    print(arc1.__repr__())
    arc2 = Archive(2, "Текст 2")
    arc3 = Archive(3, "Symbols 3")
    print(arc3)
    rectangle1 = Rectangle(7.3)
    rectangle2 = Rectangle(5.6, 10.2)
    rectangle3 = Rectangle(7.1, 4.8)
    print(f'площадь 1 прямоугольника = {rectangle1.get_area():.2f}')
    print(f'площадь 2 прямоугольника = {rectangle2.get_area():.2f}')
    # print(rectangle1 == rectangle2)
    print(f'({rectangle1.get_area():.2f} = {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
    print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
    print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
    print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
    print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
    print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)
    print(rectangle3)
