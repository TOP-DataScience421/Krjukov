from shutil import get_terminal_size
import shutil
import os

#1 Task

columns, lines = get_terminal_size()
width = columns - 3
width_start_end = (columns - 3)*"=" 
width_none = (columns - 3)*" " 

def important_message(messasge:str) -> str:
    
    messasge_finaly = ("#"+width_start_end+"#\n"+"#"+width_none+"#\n"+"#"+messasge.center(width)+"#\n"+"#"+width_none+"#\n"+"#"+width_start_end+"#\n")

    return print(messasge_finaly)

# Task 2

def load_file(source_path: str):

    current_directory = os.getcwd()

    # Получаем имя и расширение файла
    file_name, file_extension = os.path.splitext(os.path.basename(source_path))

    # Генерируем имя для копии файла с сохранением расширения
    destination_file = f"копия_{file_name}{file_extension}"
    destination_path = os.path.join(current_directory, destination_file)

    # Копирование файла в тот же каталог
    shutil.copy(source_path, destination_path)
    
    return destination_path ,print(f"Файл '{file_name}{file_extension}' успешно скопирован в '{destination_file}' в том же каталоге.")