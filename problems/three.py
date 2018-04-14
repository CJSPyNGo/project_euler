import unittest
from spynmath import SpynMath

def get_largest_prime_factor(number):
    math = SpynMath()
    factors = math.get_prime_factors(number)
    
    sorted_factors = sorted(factors)
    sorted_factors.reverse()
    return sorted_factors.pop(0)

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