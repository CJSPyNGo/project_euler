from math import sqrt 
from itertools import count, islice

class SpynMath:
    def get_factors(self, number):
        factors = [] 
        possible_factor = 2

        while possible_factor <= number / 2:
            if number % possible_factor == 0:
                factors.append(possible_factor)

                other_factor = number / possible_factor
                factors.append(other_factor)
                if other_factor - possible_factor <= 1:
                    break

            possible_factor = possible_factor + 1
        
        return list(set(factors))

    def get_prime_factors(self, number):
        prime_factors = []
        factors = self.get_factors(number)
        for factor in factors:
            if self.is_prime(factor):
                prime_factors.append(factor)
        
        return prime_factors

    def is_prime(self, number):
        if number < 2:
            return False
        
        for n in islice(count(2), int(sqrt(number) - 1)):
            if not number % n:
                return False
        
        return True
    