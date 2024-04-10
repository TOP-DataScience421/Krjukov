

number = int(input("Введите трехзначное число: "))

one = number // 100
two = (number % 100) // 10
free = (number % 100) % 10

summ = one + two + free
composition = one * two * free

print(f"Cумма цифр: {summ} \nПроизведение цифр: {composition}")

#Введите трехзначное число: 333
#Cумма цифр: 9 
#Произведение цифр: 27