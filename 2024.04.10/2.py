
summ = 0

while True:
    try:
        number = int(input('Введите число: '))
        summ += number
    except ValueError:
        print(summ)
        break
        
# Введите число: 6
# Введите число: 3
# Введите число: -5
# Введите число: 1
# Введите число: 10
# Введите число: -1
# Введите число: 8
# Введите число: o
# 22

# плохо понял задачу , симпровизировал , условия выхода ввод отличный отстроки , для 
# корректного подсчета как в ТЗ суммирует положительные и отрицательные числа



