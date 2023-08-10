import os

"""
Напишите функцию группового переименования файлов. Она должна: - принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер. - принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла. - принимать диапазон сохраняемого оригинального имени. Например, для
диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно
передано. Далее счётчик файлов и расширение.
"""


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


rename_all_files('Dir_for_hw7_task2', 'new_name', 3, 'jpg', 'super', [1, 3])
