"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла
"""

s = "/Users/marina/work/python/course/hw/task1.py"

def get_file_path_name_ext(s):
    path, filename_with_ext = s.rsplit('/', 1)
    filename, ext = filename_with_ext.split('.', 1)

    return (path, filename, ext)

print(get_file_path_name_ext(s))