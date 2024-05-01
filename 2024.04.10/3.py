
number = int(input("Введите число: "))
list_divider = []

for num in range(1,number + 1):
    if number % num == 0:
        list_divider.append(num)

print(sum(list_divider))

# Введите число: 50
# 93