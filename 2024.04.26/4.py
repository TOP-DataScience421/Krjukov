#Вывод не такой как в вашем ответе...Но по крайней мере работает вроде как декаратор - были сложности с  заданием

def repeat(func):
    """Выполняет входящую функцию указанное количество раз"""
    def wrapper( n: int = 2, *args, **kwargs):
        for _ in range(n):
            func(*args, **kwargs)
            
    return wrapper


@repeat
def testing_function():
    print('python')

testing_function(3)
#python
#python
#python
print("Далее вызов с аргументом по умолчанию")
testing_function()
#python
#python


