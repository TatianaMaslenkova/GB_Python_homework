import os
import json
import csv
import pickle

"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию. Для каждого
объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер файлов в
ней с учётом всех вложенных файлов и директорий.
"""


def get_size(path):
    size = 0
    for dir_path, dir_names, file_names in os.walk(path):
        for file in file_names:
            file_path = os.path.join(dir_path, file)
            size += os.path.getsize(file_path)
    return size


def directory_walker(dir_path):
    result = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            result.append({"Name": name,
                           "Parent_directory": root,
                           "Object_type": 'File',
                           "Size_in_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            result.append({"Name": name,
                           "Parent_directory": root,
                           "Object_type": 'Directory',
                           "Size_in_bytes": get_size(full_path)})
    return result


directory = 'C:\\Users\\sevas\\PycharmProjects\\Dir_for_hw8'
walk_result = directory_walker(directory)
print(walk_result)

with open('homework8_task1.json', 'w', encoding='utf-8') as json_file:
    json.dump(walk_result, json_file, indent=5, ensure_ascii=False)

with open("homework8_task1.csv", 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=walk_result[0].keys(), delimiter='|')
    writer.writeheader()
    writer.writerows(walk_result)

with open("homework8_task1.pickle", 'wb') as pickle_file:
    pickle.dump(walk_result, pickle_file)
