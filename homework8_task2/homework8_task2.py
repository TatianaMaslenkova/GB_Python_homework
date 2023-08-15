import json
import csv
import os
import pickle

__all__ = ['task_1', 'task_2', 'task_3', 'task_4', 'task_5', 'task_6', 'task_7']

"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов
"""


def task_1(txt_file, json_file):
    with open(txt_file, 'r', encoding='utf-8') as f, \
            open(json_file, "w", encoding='utf-8') as js_f:
        contents = f.readlines()
        my_dict = {}
        for el in contents:
            key, val = el.split("-")
            my_dict[key.title()] = float(val)
        json.dump(my_dict, js_f, separators=(',\n', ':'), ensure_ascii=False)


def task_2():
    # name = input("Введите имя:> ")
    # user_id = input("Введите id:> ")
    # level = int(input('Введите уровень доступа (1-7):> '))
    name = "Петр"
    user_id = "001"
    level = 3

    with open('task8_2.json', "r", encoding='utf-8') as f:
        result = json.load(f)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open('task8_2.json', "w", encoding='utf-8') as js_f:
        result.append(my_dct)
        json.dump(result, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)


def task_3():
    with open('task8_2.json', "r", encoding='utf-8') as js_f:
        new_res = json.load(js_f)
        lst = []
        keys = new_res[0].keys()
        lst.append(keys)
        for element in new_res:
            vals = element.values()
            lst.append(vals)

    with open('task8_2.csv', "w", newline='', encoding='utf-8') as cs_f:
        csv_writer = csv.writer(cs_f)
        for element in lst:
            csv_writer.writerow(element)


def task_4():
    with open('task8_2.csv', encoding="utf-8") as f:
        f_r = csv.reader(f)
        res = list(f_r)
        for i in range(1, len(res)):
            temp = res[i][1]
            res[i][1] = f"{temp.zfill(10)}"
            res[i][2] = res[i][2].title()

    with open('new_json.json', "w", encoding="utf-8") as j:
        json.dump(res, j)


def task_5():
    for el in os.listdir():
        if el.endswith(".json"):
            with open(el, "r", encoding="utf-8") as j:
                res = json.load(j)
            path = ''.join(el.split(".")[:-1]) + ".pickle"
            with open(path, "wb") as p:
                pickle.dump(res, p)


def task_6():
    with open('new_json.pickle', 'rb') as f:
        data = pickle.load(f)

    with open("new_c.csv", "w", encoding="utf-8") as c:
        writer = csv.writer(c)
        for row in data:
            writer.writerow(row)


def task_7():
    with open("new_c.csv", "r", encoding="utf-8") as c:
        rider = csv.reader(c)
        data = pickle.dumps(list(rider))
        print(pickle.loads(data))


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


if __name__ == '__main__':
    # task_1('task7_3.txt', 'task8_1.json')
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    print(get_size('C:\\Users\\sevas\\PycharmProjects\\Dir_for_hw8'))
    walk_result = directory_walker('C:\\Users\\sevas\\PycharmProjects\\Dir_for_hw8')
    print(walk_result)
