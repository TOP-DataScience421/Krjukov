ticket = input("Введите номер вашего билета: ")

mediana = int(len(ticket)/2)

half_one = ticket[0:mediana]
half_two = ticket[mediana:]

half_one_summ = eval("+".join(half_one))
half_two_summ = eval("+".join(half_two))

if half_one_summ == half_two_summ: 
    print("да")
else:
    print("нет")

# Введите номер вашего билета: 183534
# да
# Введите номер вашего билета: 401367
# нет