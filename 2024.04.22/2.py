
length = int(input("Введите расстояние поездки в метрах: "))
time_expectation = input("Введите время ожидания в минутах: ")

def taxi_cost(*, length: int, time_expectation: int = 0) -> int | None :
    """
    Функция возвращает стоимость поездки или None, если вычисление невозможно.
    """ 
    if time_expectation.isdigit():
        time_expectation = int(time_expectation)
    else:
        time_expectation = 0
    
    if length < 0 or time_expectation < 0:
        return None, print(None)
    
    basic_coast = 80
    
    check = int(basic_coast + ((length/150) * 6) + int(time_expectation) * 3)
    
    return print(check)

taxi_cost(length=length, time_expectation=time_expectation)

#Введите расстояние поездки в метрах: 1500
#Введите время ожидания в минутах:
#140

#Введите расстояние поездки в метрах: 2560
#Введите время ожидания в минутах:
#182

#Введите расстояние поездки в метрах: 0
#Введите время ожидания в минутах: 5
#95   -- --- тут в описании задачи в ТЗ ответ неверный (базовая стоимость 80 + 5 * 3 = 95)

#Введите расстояние поездки в метрах: 42130
#Введите время ожидания в минутах: 8
#1789

#Введите расстояние поездки в метрах: -300
#Введите время ожидания в минутах:
#None

