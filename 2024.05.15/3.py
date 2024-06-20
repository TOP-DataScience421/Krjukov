from utils import load_file
import os
import importlib.util

#/home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data/conf.py

def ask_for_file():
    "запрашивает у пользователя путь к потерянному файлу и копирует этот файл с помощью функции load_file."

    source_path = input("Введите путь к файлу:  ")

    if os.path.exists(source_path):
        load_file(source_path)
        file_name, file_ext = os.path.splitext(os.path.basename(source_path))
        spec = importlib.util.spec_from_file_location(file_name, source_path)
        module = importlib.util.module_from_spec(spec)
    else:
        print("Введите корректнрый путь")
        source_path = input("Введите путь к файлу:  ")
        ask_for_file()

    return module, print(module.__dict__)

ask_for_file()

"""
Введите путь к файлу:  /home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data/conf.py
Файл 'conf.py' успешно скопирован в 'копия_conf.py' в том же каталоге.
{'__name__': 'conf', '__doc__': None, '__package__': '', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x747b3945bf40>, '__spec__': ModuleSpec(name='conf', loader=<_frozen_importlib_external.SourceFileLoader object at 0x747b3945bf40>, origin='/home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data/conf.py'), '__file__': '/home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data/conf.py', '__cached__': '/home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data/__pycache__/conf.cpython-310.pyc'}
"""