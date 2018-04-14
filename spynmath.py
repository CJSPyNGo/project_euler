
def get_factors(number):
    factors = [] 
    possible_factor = 2

    while possible_factor <= number / 2:
        if number % possible_factor == 0:
            factors.append(possible_factor)

        possible_factor = possible_factor + 1
    
    return list(set(factors))