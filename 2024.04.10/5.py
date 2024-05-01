text = input("Введите текс телаграммы: ")

count = 0

free_symbol = " .,!@#$%^&*()_-><?/"

for symbol in text:
    if symbol not in free_symbol:
        count += 1

penny = 30*count

ruble = penny // 100
penny_finaly = penny - ruble*100

print(f"Стоимость телеграммы : {ruble} рублей, {penny_finaly} копеек")

# Введите текс телаграммы: грузите апельсины бочках братья карамазовы
# Стоимость телеграммы : 11 рублей, 40 копеек