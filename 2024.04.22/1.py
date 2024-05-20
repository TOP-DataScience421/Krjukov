
enter = input("Введите пароль : ")

def strong_password(password: str) -> bool:
    """
    Проверка надежности пароля
    """
    
    lenghts = bool
    down = bool
    upp = bool
    count = 0
    symbols = "/.,!;:?*()№#- _"
    
    
    if len(password)>=8:
        lenghts = True
    
    for i in password:
        if i.islower():
            down = True
        if i.isupper():
            upp = True
        if i.isdigit():
            count += 1

    found = any(i in symbols for i in password)
        
    
    if lenghts == True and upp == True and down == True and count >= 2 and found == True:
        return True, print("True")
    else:
        return False , print("Folse")
    
strong_password(enter)

#Введите пароль : aP3:kD_l3
#True

#Введите пароль : sdsv43d2
#Folse