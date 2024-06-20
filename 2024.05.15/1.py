from pathlib import Path

test = r"/home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data"
test_two = r"/home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data/22"

def list_files( directory: str) -> tuple:
    
    if not Path(directory).exists():
        return print(None)
    
    file = Path(directory).iterdir()

    finaly_touple = ()

    for item in file:
        if item.suffix :
            finaly_touple += (item.name, )

    print(f"Содержимое католога: {test} \n",finaly_touple)

list_files(test)
#Содержимое католога: /home/vsevolod/Рабочий стол/Krjukov/2024.05.15/data 
# ('conf.py', 'E3ln1.txt', 'vars.py', '7MD9i.chm', 'F1jws.jpg', 'r62Bf.txt', 'questions.quiz', 'le1UO.txt', 'xcD1a.zip', 'q40Kv.docx')
# Включает все кроме папок и файлов без расширения

list_files(test_two)
#None