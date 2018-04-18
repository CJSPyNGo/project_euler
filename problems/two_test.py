import unittest
from .two import ProblemTwo

class ProblemTwoTests(unittest.TestCase):
    def setUp(self):
        self.two = ProblemTwo()

    def test_10(self):
        s = self.two.sum_from_even_fib(10)
        self.assertEqual(s, 10)

    def test_4000000(self):
        s = self.two.sum_from_even_fib(4000000)
        self.assertEqual(s, 4613732)

def main():
    unittest.main()

if __name__ == "__main__":
    main()