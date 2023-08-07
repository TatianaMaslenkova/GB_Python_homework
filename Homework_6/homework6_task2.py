from sys import argv
from homework6_task1 import check_date

"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку
"""

string_date = argv[1]
print(check_date(string_date))
