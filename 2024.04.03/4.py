
one = input('Введите первую координату: ')
two = input('Введите вторую координату: ')

horizontal = "abcdefgh"
vertical = "12345678"

all_list = []
coorinats = []
all = []
for num in horizontal:
    for har in vertical:
        coorinats.append(num + har)
        all.append(num + har)
    all_list.append(coorinats)
    coorinats = []

color_list = []

for index, line in enumerate(all_list): 
    if (index + 1) % 2 == 0:
        for ind, symbol in enumerate(line) : 
            if (ind+1) % 2 == 0:
                symbol = True
                color_list.append(symbol)
            else: 
                symbol = False
                color_list.append(symbol)

    else:
        for ind, symbol in enumerate(line) : 
            if (ind+1) % 2 != 0:
                symbol = True
                color_list.append(symbol)
            else: 
                symbol = False
                color_list.append(symbol)

def check(one,two):
    index_one = all.index(one)
    index_two = all.index(two)

    if color_list[index_one] == color_list[index_two]:
        print('Да')
    else:
        print('Нет')

check(one,two)
            
#Введите первую координату: a1
#Введите вторую координату: b2
#Да

