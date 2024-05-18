word = input('Введите слово: ')

scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

count = 0

for char in word:
    char = char.upper() 
    for key, value in scores_letters.items():
        if char in value:
                count += key

print(count)

#Введите слово: синхрофазотрон
#29