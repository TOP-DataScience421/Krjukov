

def numbers_strip( list_nambers: list[float],  number: int = 1, copy: bool = False):
    """
    удаляет n минимальных и n максимальных чисел из списка
    """
    numbers_min = min(list_nambers)
    numbers_max = max(list_nambers)    
    
    
    if copy == False:
        
        for i in list_nambers:
            if i == numbers_min or i == numbers_max:
                list_nambers.remove(i)
                
        number -= 1
        if number > 0:
            return numbers_strip (list_nambers,number)
        else:
            return list_nambers
        
    
    else:
        
        copy_list = list_nambers.copy()
        
        for i in copy_list:
            if i == numbers_min or i == numbers_max:
                copy_list.remove(i)
                
        number -= 1
        if number > 0:
            return numbers_strip (copy_list,number,copy=True)
        else:
            return copy_list
        
sample = [1, 2, 3, 4]
sample_stripped = numbers_strip(sample)
print(sample_stripped)
#Вывод [2, 3]
print(sample is sample_stripped)
#True

sample = [10, 20, 30, 40, 50]
sample_stripped = numbers_strip(sample, 2, copy=True)
print(sample_stripped)
#[30]
print(sample is sample_stripped)
#False