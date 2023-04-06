import os
import json

"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её 
и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
-   Для дочерних объектов указывайте родительскую директорию. 
-   Для каждого объекта укажите файл это или директория.
-   Для файлов сохраните его размер в байтах, а для директорий размер файлов 
в ней с учётом всех вложенных файлов и директорий.
"""

def walk():
    dic = {}
    for file in os.listdir("."):
        if os.path.isdir(file):
            dic[file] = {
                "type": "dir",
                "files": len(os.listdir(file))

            }
        else:
            dic[file] = {
                "type": "file",
                "size": os.path.getsize(file),
            }
    with open("files.json", "w+") as f:
        json.dump(dic, f, ensure_ascii=False)


if __name__ == "__main__":
    walk()