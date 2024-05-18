
fruits = []

while True:
    fruit = input("Напиши фрукт: ")
    if fruit == "" :
        break

    fruits.append(fruit)

if len(fruits) == 1:
        print(' '.join(fruits))
else:
    fruits.insert(-1 , ' и ')
    last_three = " ".join(fruits[-3:])
    del fruits[-3:]
    fruits.append(last_three)
    string_fruit = ', '.join(fruits)
    print(string_fruit)


#Напиши фрукт: яблоко
#Напиши фрукт: 
#яблоко

#Напиши фрукт: яблоко
#Напиши фрукт: груша
#Напиши фрукт: 
#яблоко  и  груша

#Напиши фрукт: яблоко
#Напиши фрукт: груша
#Напиши фрукт: апельсин
#Напиши фрукт: 
#яблоко, груша  и  апельсин

#Напиши фрукт: яблоко 
#Напиши фрукт: груша
#Напиши фрукт: апельсин
#Напиши фрукт: лимон
#Напиши фрукт: 
#яблоко, груша, апельсин  и  лимон