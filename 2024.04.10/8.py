start_num = int(input("Введите число: "))

sum_num = 1
fibonaci_list = [1,1]

while len(fibonaci_list)< start_num :
    fibonaci_list.append(fibonaci_list[-1] + fibonaci_list[-2])

if start_num == 1 :
    print("1")
else:
    print(" ".join(list(map(str, fibonaci_list))))

# Введите число: 1
# 1

# Введите число: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597