
one = input('Введите первую координату: ')
two = input('Введите вторую координату: ')

horizontal = "abcdefgh"
vertical = "12345678"

horizontal_list = []
coorinats = []

for num in horizontal:
    for har in vertical:
        coorinats.append(num + har)
    horizontal_list.append(coorinats)
    coorinats = []

vertical_list = []
coorinats = []

for num in vertical:
    for har in horizontal:
        coorinats.append(har+ num)
    vertical_list.append(coorinats)
    coorinats = []

# список всех возможных линий ходов ладьи
itog_list = horizontal_list + vertical_list

def check(one,two):
    flag = 0
    for combination in itog_list:
        if one in combination and two in combination:
            flag += 1
            if flag > 0:
                print("да")
                flag = 0
                break 
    else:
        print("нет")
            

check(one,two)

#Введите первую координату: d4
#Введите вторую координату: e4
#да

#Введите первую координату: a2
#Введите вторую координату: c4
#нет

