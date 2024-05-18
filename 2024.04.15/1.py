
e_mail = input('Введите адресс электронной почты: ')

dog = e_mail.rfind('@')
end = e_mail.rfind('.')

if dog != -1 and end != -1 and dog<end:
    print('Да')
else:
    print('Нет ')

# Введите адресс электронной почты: sgd@ya.ru
# Да

# Введите адресс электронной почты: abcde@fghij 
# Нет 