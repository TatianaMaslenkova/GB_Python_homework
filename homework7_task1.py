import os

'''
Решить задачи, которые не успели решить на семинаре: Создайте функцию для сортировки файлов по директориям: видео, 
изображения, текст и т.п. Каждая группа включает файлы с несколькими расширениями. В исходной папке должны остаться 
только те файлы, которые не подошли для сортировки.
'''

FILE_EXTENSIONS = {'video': ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'mpeg', 'ram'],
                   'image': ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif'],
                   'text': ['txt', 'doc', 'docx', 'dotx', 'pdf', 'rtf', 'djvu'],
                   'audio': ['mp3', 'wav', 'wma', 'midi', 'ogg', 'aac'],
                   'web_page': ['html', 'htm', 'mht'],
                   'archive': ['zip', 'rar', '7z', 'gzip']}


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


sort_func('Dir_for_hw7_task1', FILE_EXTENSIONS)
