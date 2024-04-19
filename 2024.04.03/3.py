
year = int(input('Введите год: '))

year = 'Да' if (year % 4 == 0 and year % 100 != 0) else 'Нет'

print(year)


#Введите год: 2020
#Да