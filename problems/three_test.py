import unittest
from .three import ProblemThree

class TestProblemThree(unittest.TestCase):
    def setUp(self):
        self.three = ProblemThree()

    def test_13195(self):
        s = self.three.get_largest_prime_factor(13195)
        self.assertEqual(s, 29)

    def test_600851475143 (self):
        s = self.three.get_largest_prime_factor(600851475143)
        self.assertEqual(s, 6857)

def main():
    unittest.main()

if __name__ == "__main__":
    main()