from pathlib import Path
import os

def search_context(words): 
    current_directory = Path.cwd()
    folder_path = current_directory / "data"
    
    file = Path(folder_path).iterdir()
    
    key = 0
    dict_finaly = {}
    
    for item in file:
        if item.suffix == ".txt":
            with open(item, "r") as f:
                for line_number, line in enumerate(f, start=1):
                    lines = line.lower()
                    
                    for word in words:
                        w = word.lower()
                        if w in lines:
                            key += 1
                            if key not in dict_finaly:
                                dict_finaly[key] = {'keyword': w, 'filename': key, 'lines': []}
                            dict_finaly[key]['lines'].append({'line_number': line_number, 'text': line.rstrip()})
    
    print(dict_finaly)
    
    for key, value in dict_finaly.items():  # Перебор пар ключ-значение из словаря
        print(key, value)

search_context(words=('мысль', 'мысли'))
