import unittest
from .spynmath import SpynMath

class SpynMathTests(unittest.TestCase):  
    
    def setUp(self):
        self.math = SpynMath()

    #region get_factors
    def test_get_factors_10(self):
        factors = self.math.get_factors(10)
        self.assertEqual(len(factors), 2)
        self.assertTrue(2 in factors)
        self.assertTrue(5 in factors)

    def test_get_factors_12(self):
        factors = self.math.get_factors(12)
        self.assertEqual(len(factors), 4)
        self.assertTrue(2 in factors)
        self.assertTrue(3 in factors)
        self.assertTrue(4 in factors)
        self.assertTrue(6 in factors)

    def test_get_factors_40(self):
        factors = self.math.get_factors(40)
        self.assertEqual(len(factors), 6)
        self.assertTrue(2 in factors)
        self.assertTrue(4 in factors)
        self.assertTrue(5 in factors)
        self.assertTrue(8 in factors)
        self.assertTrue(10 in factors)
        self.assertTrue(20 in factors)
    #endregion

    #region is_prime
    def test_is_prime_5(self):
        is_number_prime = self.math.is_prime(5)
        self.assertTrue(is_number_prime)

    def test_is_prime_4(self):
        is_number_prime = self.math.is_prime(4)
        self.assertFalse(is_number_prime)
    
    def test_is_prime_73(self):
        is_number_prime = self.math.is_prime(73)
        self.assertTrue(is_number_prime)

    def test_is_prime_100(self):
        is_number_prime = self.math.is_prime(100)
        self.assertFalse(is_number_prime)
    #endregion

    #region get_prime_factors
    def test_get_prime_factors_7(self):
        factors = self.math.get_prime_factors(7)
        print(factors)
        self.assertEqual(len(factors), 0)

    def test_get_prime_factors_10(self):
        factors = self.math.get_prime_factors(10)
        self.assertEqual(len(factors), 2)
        self.assertTrue(2 in factors)
        self.assertTrue(5 in factors)

    def test_get_prime_factors_12(self):
        factors = self.math.get_prime_factors(12)
        self.assertEqual(len(factors), 2)
        self.assertTrue(2 in factors)
        self.assertTrue(3 in factors)

    def test_get_prime_factors_21(self):
        factors = self.math.get_prime_factors(21)
        self.assertEqual(len(factors), 2)
        self.assertTrue(3 in factors)
        self.assertTrue(7 in factors)

    def test_get_prime_factors_40(self):
        factors = self.math.get_prime_factors(40)
        self.assertEqual(len(factors), 2)
        self.assertTrue(2 in factors)
        self.assertTrue(5 in factors)
    #endregion

    #region is_palindrome

    def test_is_palindrome_101(self):
        result = self.math.is_palindrome(101)
        self.assertTrue(result)

    def test_is_palindrome_10101(self):
        result = self.math.is_palindrome(10101)
        self.assertTrue(result)
    
    def test_is_palindrome_100(self):
        result = self.math.is_palindrome(100)
        self.assertFalse(result)

    #endregion
def main():
    unittest.main()

if __name__ == "__main__":
    main()