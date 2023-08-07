import random
__all__ = ["beat_queens", "good_position"]
"""
3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различные случайные  варианты и выведите 4 успешных расстановки.
"""

NEED_GOOD_POSITIONS = 4


def beat_queens(pos):
    n = len(pos)
    beat = False
    for i in range(n):
        for j in range(i + 1, n):
            if pos[i][0] == pos[j][0] or pos[i][1] == pos[j][1] or abs(pos[i][0] - pos[j][0]) == abs(
                    pos[i][1] - pos[j][1]):
                beat = True
    if beat:
        return False  # Ферзи бьют друг друга
    else:
        return True  # Ферзи не бьют друг друга


def good_position(needed_good_num):
    position = []
    x_position = [1, 2, 3, 4, 5, 6, 7, 8]
    y_position = [1, 2, 3, 4, 5, 6, 7, 8]
    count = 1
    iteration_number = 0
    while count <= needed_good_num:
        iteration_number += 1
        random.shuffle(x_position)
        random.shuffle(y_position)
        for k in range(8):
            position.append([x_position[k], y_position[k]])

        if beat_queens(position):
            print(f'Итерация № {iteration_number}: {position}')
            count += 1
        position.clear()


if __name__ == '__main__':
    print(beat_queens(
        [[5, 3], [1, 2], [4, 1], [8, 4], [2, 5], [7, 6], [3, 7], [6, 8]]))  # True - ферзи не бьют друг друга
    print(
        beat_queens([[1, 6], [2, 3], [3, 3], [5, 4], [8, 7], [6, 2], [3, 8], [4, 5]]))  # False - ферзи бьют друг друга
    print("Варианты успешных расстановок 8 ферзей: ")
    good_position(NEED_GOOD_POSITIONS)
