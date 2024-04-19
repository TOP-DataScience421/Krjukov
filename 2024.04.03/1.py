one = float(input("Введите первое число:  "))
two = float(input("Введите второе число:  "))
free = float(input("Введите третье число:  "))

ones = one if one >= 0 else 0

twos = two if two >= 0 else 0

frees = free if free >0 else 0

summ = ones + twos + frees

print(summ)

#Введите первое число:  4
#Введите второе число:  -22
#Введите третье число:  1.5
#5.5