from random import randint, choices, randbytes, uniform
from string import ascii_lowercase
import os
from homework7_task1 import FILE_EXTENSIONS

__all__ = ["write_pair_nums", "write_random_name", "my_func", "func", "func_2", "func_3", "sort_func",
           "rename_all_files"]


def write_pair_nums(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        print(type(f))
        for _ in range(lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num} | {float_num:.2f}\n')


def write_random_name(count_names: int):
    vowels = 'аеиоуыэюя'
    count = 0
    str_names = ""
    while count != count_names:
        word = choices(alfabet, k=randint(4, 7))
        if any(item in vowels for item in word):
            str_names += ''.join(word).capitalize() + '\n'
            count += 1
    with open('task7_2.txt', 'a', encoding='utf-8') as f:
        f.write(str_names)


alfabet = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1)])


def my_func():
    with open('task7_1.txt', 'r', encoding='utf-8') as f_nums, \
            open('task7_2.txt', 'r', encoding='utf-8') as f_names:
        nums = f_nums.readlines()
        names = f_names.readlines()

    for_write = []
    long = max(len(nums), len(names))
    i = 0
    while len(nums) != len(names):
        if len(nums) > len(names):
            names.extend(names[:len(nums) - len(names)])
        else:
            nums.extend(nums[:len(names) - len(nums)])

    while i < long:
        name = names[i]
        num = nums[i]
        a, b = map(float, num.split('|'))
        mult = a * b

        if mult >= 0:
            for_write.append(f'{name.upper().rstrip()} - {round(mult)}\n')
        else:
            for_write.append(f'{name.lower().rstrip()} - {abs(mult)}\n')
        i += 1

    with open("task7_3.txt", 'w', encoding='utf-8') as f:
        f.writelines(for_write)


def func(ext, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096, files=42):
    for i in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        size = randint(min_rand_bytes, max_rand_bytes)
        with open(name, 'wb') as f:
            f.write(randbytes(size))


def func_2(files=10, **kwargs):
    dct = kwargs
    val = []
    for k, v in dct.items():
        val.append(v)
    for i in range(files):
        ext = str(*choices(val))
        func(ext, files=1, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096)


def func_3(new_dir):
    my_path = os.getcwd() + new_dir
    try:
        os.makedirs(my_path)
        os.chdir(my_path)
    except FileExistsError:
        os.chdir(my_path)
    func_2(1, a='.txt', b='.doc', c='.exe')
    os.chdir('..')


def sort_func(directory, file_extension):
    files_list = [file.split('.') for dirs, folders, files in os.walk(directory) for file in files]
    for (name, extension) in files_list:
        for k, v in file_extension.items():
            if extension in v:
                new_directory = os.path.join(os.getcwd(), directory, k)
                current_folder = os.path.join(directory, f'{name}.{extension}')
                new_folder = os.path.join(new_directory, f'{name}.{extension}')
                if os.path.isdir(new_directory):
                    os.replace(current_folder, new_folder)
                else:
                    os.makedirs(new_directory)
                    os.replace(current_folder, new_folder)


def rename_all_files(directory, final_name, num_amount, init_file_extension, final_file_extension, init_name):
    count = 1
    start, end = init_name
    for dirs, folders, files in os.walk(directory):
        for i, file in enumerate(files):
            if file.endswith(init_file_extension):
                init_name = os.path.join(dirs, file)
                new_name = (
                    f'{dirs}\\{file[start:end]}{final_name}{str(count).zfill(num_amount)}.{final_file_extension}')
                os.rename(init_name, new_name)
                count += 1

# write_pair_nums('task7_1.txt', 20)
# write_random_name(6)
# my_func()
# func('.txt')
# func_2(5, a='.txt', b='.doc', c='.exe')
# func_3('\\task6')
# sort_func('Dir_for_hw7_task1', FILE_EXTENSIONS)
# rename_all_files('Dir_for_hw7_task2', 'new_name', 3, 'jpg', 'super', [1, 3])
