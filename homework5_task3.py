"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fibonacci(num):
    f1, f2 = 0, 1
    for _ in range(number):
        yield f1
        f1, f2 = f2, f1 + f2


number = int(input("Введите количество членов последовательности Фибоначчи: "))
print(*(fibonacci(number)))
