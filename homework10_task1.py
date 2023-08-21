"""
Доработаем задания 5-6. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов) и
параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


class Factory:
    def __init__(self, animal_type, kind, name, age, **kwargs):
        self.animal_type = animal_type
        self.kind = kind
        self.name = name
        self.age = age
        for k, v in kwargs.items():
            if k == 'size':
                self.size = v
            if k == "color":
                self.color = v
            if k == "spec":
                self.spec = v

    def get_animal(self):
        if self.animal_type == "fish":
            return Fishes(self.kind, self.name, self.age, self.size)
        elif self.animal_type == "bird":
            return Birds(self.kind, self.name, self.age, self.color)
        elif self.animal_type == 'mammal':
            return Mammals(self.kind, self.name, self.age, self.spec)


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size

    def get_info(self):
        return f'Вид животного: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет, ' \
               f'размер: {self.get_specific()} см'


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color

    def get_info(self):
        return f'Вид животного: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет, ' \
               f'цвет: {self.get_specific()}'


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec

    def get_info(self):
        return f'Вид животного: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет, ' \
               f'специфическая характеристика: {self.get_specific()}'


a1 = Factory("fish", "карась", "Федя", 1, size=15)
print(a1.get_animal().get_info())
a2 = Factory("bird", "cиница", "Пеночка", 3, color="зеленый")
print(a2.get_animal().get_info())
a3 = Factory("mammal", "собака", "Дружок", 5, spec="короткошёрстный")
print(a3.get_animal().get_info())
