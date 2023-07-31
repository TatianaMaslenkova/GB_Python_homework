"""
Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


matrix = [[105, 8, 17, 359],
          [5, 57, 326, 90],
          [49, 185, 1, 19],
          [1789, 4, 11, 189],
          [432, 38, 9, 88]]

print(f'Исходная матрица:')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'{matrix[i][j]:>{5}}', end=",")
    print()

transposed_matrix = transpose_matrix(matrix)

print('Транспонированная матрица:')

for i in range(len(transposed_matrix)):
    for j in range(len(transposed_matrix[0])):
        print(f'{transposed_matrix[i][j]:>{5}}', end=",")
    print()
