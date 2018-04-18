import unittest
from .problem_004 import ProblemFour

class ProblemFourTests(unittest.TestCase):
    def setUp(self):
        self.four = ProblemFour()

    def test_two_digit_numbers(self):
        s = self.four.get_largest_palindrome_product_from_range(10, 99)
        self.assertEqual(s, 9009)

    def test_three_digit_numbers (self):
        s = self.four.get_largest_palindrome_product_from_range(100, 999)
        self.assertEqual(s, 906609)

def main():
    unittest.main()

if __name__ == "__main__":
    main()