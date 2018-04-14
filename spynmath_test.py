import unittest
from spynmath import get_factors

class TestSpynMath(unittest.TestCase):

    def test_get_factors_10(self):
        factors = get_factors(10)
        self.assertEqual(len(factors), 2)
        self.assertEquals(factors[0], 2)
        self.assertEquals(factors[1], 5)

    def test_get_factors_12(self):
        factors = get_factors(12)
        self.assertEqual(len(factors), 4)
        self.assertTrue(2 in factors)
        self.assertTrue(3 in factors)
        self.assertTrue(4 in factors)
        self.assertTrue(6 in factors)

    def test_get_factors_40(self):
        factors = get_factors(40)
        print(factors)
        self.assertEqual(len(factors), 6)
        self.assertTrue(2 in factors)
        self.assertTrue(4 in factors)
        self.assertTrue(5 in factors)
        self.assertTrue(8 in factors)
        self.assertTrue(10 in factors)
        self.assertTrue(20 in factors)

def main():
    unittest.main()

if __name__ == "__main__":
    main()