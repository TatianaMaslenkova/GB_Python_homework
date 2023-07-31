"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
путь, имя файла, расширение файла.
"""


def path_to_tuple(path):
    text = path.split("\\")
    path = "\\".join(text[:len(text) - 1:])
    file_name = text[len(text) - 1:len(text)]
    name, extension = file_name[0].split('.')
    result = path, name, extension
    return result


absolute_path = "C:\\Users\\sevas\\PycharmProjects\\Project_python\\homework5_task1.py"
print(f'Абсолютный путь до файла: {absolute_path}')
print(f'Кортеж (путь, имя файла, расширение файла): {path_to_tuple(absolute_path)}')
