
list_number = []
flag = True

while True :
    number = int(input('Введите число кратное семи: '))
    if number % 7 == 0 : 
        list_number.append(number)
    else:
        break
    
finaly_string = ""

for string in reversed(list_number):
    finaly_string += str(string) + ' '
    
print(finaly_string)

# Введите число кратное семи: 7
# Введите число кратное семи: 7
# Введите число кратное семи: 14
# Введите число кратное семи: 21
# Введите число кратное семи: 13
# 21 14 7 7