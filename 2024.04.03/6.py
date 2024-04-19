
one = input('Введите первую координату: ')

two = input('Введите вторую координату: ')

horizontal = "abcdefgh"
vertical = "12345678"

num = int(one[-1])
har = one[0]

num_minus = num - 1
nem_sum = num + 1
num_itog = str(num_minus) + str(num) + str(nem_sum)

index_car = horizontal.index(har)
har_minus = horizontal[index_car - 1]
har_zero = horizontal[index_car]
har_sum = horizontal[index_car + 1]

har_itog = har_minus + har_zero + har_sum

combination = []
for var in har_itog:
    for intt in num_itog:
        combination.append(var + intt)

if two in combination: 
    print('да')
else:
    print('нет')

#Введите первую координату: g3
#Введите вторую координату: f2
#да

#Введите первую координату: c6
#Введите вторую координату: d4
#нет