

def orth_triangle(*, cathetus1: float = 0 , cathetus2: float = 0 , hypotenuse : float = 0 ) -> float:
    """
    вычисляет третью сторону прямоугольного треугольника
    """
    
    if (hypotenuse < cathetus1 or hypotenuse < cathetus2) and hypotenuse != 0:
        return print("Гипотеноза не может быть меньше катетов")
    elif cathetus1 != 0 and cathetus2  != 0 and hypotenuse != 0: 
        return print("Все стороны треугольника известны, нечего вычислять") 
    else:
        
        if hypotenuse == 0:
            hypotenuse= (cathetus1**2 + cathetus2**2)**0.5
            return print("Гипотенуза = ",hypotenuse)
        elif cathetus1  == 0:
            cathetus1 = (hypotenuse**2 - cathetus2**2)**0.5
            return print("Катет 1 = ",cathetus1)
        elif cathetus2  == 0:
            cathetus2 = (hypotenuse**2 - cathetus1**2)**0.5
            return print("Катет 2 = ",cathetus2)


orth_triangle(cathetus1=3, hypotenuse=5)
#Катет 2 =  4.0
orth_triangle(cathetus1=8, cathetus2=15)
#Гипотенуза =  17.0
print(orth_triangle(cathetus2=9, hypotenuse=3))
#None

