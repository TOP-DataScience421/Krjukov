from typing import Callable

def math_function_resolver(function: Callable[[float], int|str], *args, res_to_str = False) -> list[int|str]:
    ''' вычисляет округлённые значения для различных математических функций'''
    
    list_result = []
    
    for i in args:
        if res_to_str == False:
            list_result.append(round(function(i)))
        else:
            list_result.append(str(round(function(i))))
    return(print(list_result))

math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
#[2, 3, 4, 4, 4, 5, 6, 6, 6]
math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
#[2, 1, 0, 0, 0, -1, -2, -2, -2]
math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
#['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']