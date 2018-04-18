import unittest
from .problem_005 import ProblemFive

class ProblemFiveTests(unittest.TestCase):
    def setUp(self):
        self.five = ProblemFive()

    def test_solve_example_5(self):
        result = self.five.solve(1, 5)
        self.assertEqual(result, 60)

    def test_solve_example_10(self):
        s = self.five.solve(1, 10)
        self.assertEqual(s, 2520)

    def test_solve_example_15(self):
        result = self.five.solve(1, 15)
        self.assertEqual(result, 360360)

    def test_solve (self):
        s = self.five.solve(1, 20)
        self.assertEqual(s, 232792560)

def main():
    unittest.main()

if __name__ == "__main__":
    main()