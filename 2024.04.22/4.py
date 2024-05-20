

def countable_nouns(namber: int , words: tuple[str,str,str]) -> str :
    """
    Возвращает существительное русского языка, согласованное с числом
    """
    
    digit = [int(d) for d in str(namber)]
    exceptions = [11,12,13,14,15,16,17,18,19,20]
    
    if digit[-1] == 1:
        return print(words[0])
    elif 2 <= digit[-1] <= 4 and not namber in exceptions:
        return print(words[1])
    else :
        return print(words[2])


countable_nouns(1, ("год", "года", "лет"))
#год
countable_nouns(2, ("год", "года", "лет"))
#года
countable_nouns(10, ("год", "года", "лет"))
#лет
countable_nouns(12, ("год", "года", "лет"))
#лет
countable_nouns(22, ("год", "года", "лет"))
#