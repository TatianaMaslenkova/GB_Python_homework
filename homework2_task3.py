from fractions import Fraction

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму
и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
print('Вычислим сумму и произведение дробей.')
fraction1 = input("Введите первую дробь (вид: a/b): ").split("/")
fraction2 = input("Введите вторую дробь (вид: с/d): ").split("/")
a = int(fraction1[0])
b = int(fraction1[1])
c = int(fraction2[0])
d = int(fraction2[1])


def gcd_calculation(x, y):
    if x > y:
        smallest = y
    else:
        smallest = x
    for i in range(1, smallest + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd


# addition
common_denominator = b * d
fractions_addition = a * common_denominator / b + c * common_denominator / d
calculate_gcd = gcd_calculation(int(fractions_addition), common_denominator)
sum_of_fractions = f"{int(fractions_addition / calculate_gcd)}/{int(common_denominator / calculate_gcd)}"

# multiplication
numerator = a * c
denominator = b * d
calculate_gcd = gcd_calculation(numerator, denominator)
multiplication_of_fractions = f"{int(numerator / calculate_gcd)}/{int(denominator / calculate_gcd)}"

print(f"Результат сложения дробей: {a}/{b} + {c}/{d} = {sum_of_fractions}")
print(f"Результат умножения дробей: {a}/{b} * {c}/{d} = {multiplication_of_fractions}")

print("\nПроверка c помощью Fraction")
fraction1 = Fraction(a, b)
fraction2 = Fraction(c, d)
print(f"Сложение: {fraction1 + fraction2}")
print(f"Умножение: {fraction1 * fraction2}")
