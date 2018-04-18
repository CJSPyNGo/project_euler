
from project_euler.spynmath import SpynMath

class ProblemThree:
    
    def get_largest_prime_factor(self, number):
        math = SpynMath()
        factors = math.get_prime_factors(number)
        
        sorted_factors = sorted(factors)
        sorted_factors.reverse()
        return sorted_factors.pop(0)
