
one = input('Введите количесвто миль: ')
two = input('Введите дробную часть числа миль: ')

number = float(one + "." + two)
constanta = 1.61

mile = round(number * constanta,1)

print(mile)

#Введите количесвто миль: 15
#Введите дробную часть числа миль: 7
#25.3