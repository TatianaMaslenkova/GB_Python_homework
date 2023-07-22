"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex
используйте для проверки своего результата.
"""
num = int(input('Введите десятичное число: '))
hex_symbols = "0123456789abcdef"
hex_num = ""
DIVIDER = 16
check = hex(num)
print(f"Проверка через встроенную функцию hex(): {check}")
while num > 0:
    hex_num = hex_symbols[num % DIVIDER] + hex_num
    num //= DIVIDER
print(f"В шестнадцатеричном представлении: 0x{hex_num}")
