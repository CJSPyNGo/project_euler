import unittest
from math import sqrt 
from itertools import count, islice

def get_largest_prime_factor(number):
    factors = [] 
    possible_factor = 2

    while possible_factor < number / 2:
        if number % possible_factor == 0:
            if is_prime(possible_factor):
                factors.append(possible_factor)
            
            other_factor = number / possible_factor
            if is_prime(other_factor):
                factors.append(other_factor)
            
            if other_factor - possible_factor <= 1:
                break 

        possible_factor = possible_factor + 1
    
    sorted_factors = sorted(factors)
    sorted_factors.reverse()
    return sorted_factors.pop(0)

def is_prime(number):
    if number < 2:
        return False
    
    for n in islice(count(2), int(sqrt(number) - 1)):
        if not number % n:
            return False
    
    return True


class TestProblemThree(unittest.TestCase):

    def test_13195(self):
        s = get_largest_prime_factor(13195)
        self.assertEqual(s, 29)

    def test_600851475143 (self):
        s = get_largest_prime_factor(600851475143)
        self.assertEqual(s, 6857)

def main():
    unittest.main()

if __name__ == "__main__":
    main()