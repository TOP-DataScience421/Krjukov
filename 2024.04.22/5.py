
def central_tendency(num1: float, num2: float, *additions) -> dict:

    median = (2 + len(additions) + 1) / 2
    
    arithmetic = (num1 + num2 + sum(additions)) / (len(additions)+2)
    
    geometric = (num1 * num2 * eval('*'.join(map(str, additions))))**(1/(len(additions)+2))
    
    result = 0
    for i in additions:
        result += 1/i
    
    harmonic = (len(additions)+2) / ((1/num1) + (1/num2) + result)
    
    finally_dict = {
        'median' : median,
        'arithmetic': arithmetic,
        'geometric' : geometric,
        'harmonic' : harmonic,
    }
    
    return finally_dict
    
print(central_tendency(1, 2, 3, 4))
#{'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}

sample = [1, 2, 3, 4, 5]
print(central_tendency(*sample))
#{'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}