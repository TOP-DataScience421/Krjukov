
list_one = []
while True: 
    one_unteger = input("Введите число: ")
    if one_unteger.isdigit() == False:
        break   
    else:
        list_one.append(one_unteger)

list_two = []
while True:       
    two_unteger = input("Введите число: ")
    if two_unteger.isdigit() == False:
        break
    else:
        list_two.append(two_unteger)

str_one = "".join(list_one)
str_two = "".join(list_two)

result = str_one.find(str_two)
    
if result != -1 :
    print("Да")
else:
    print("Нет")

#Введите число: 1
#Введите число: 2
#Введите число: 3
#Введите число: 4
#Введите число: 
#Введите число: 1
#Введите число: 2
#Введите число: 

#Да

#Введите число: 1
#Введите число: 2
#Введите число: 3
#Введите число: 4
#Введите число: 
#Введите число: 2
#Введите число: 4
#Введите число: 

#Нет