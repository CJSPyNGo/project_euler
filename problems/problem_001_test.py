import unittest
from .problem_001 import ProblemOne

class ProblemOneTests(unittest.TestCase):

    def setUp(self):
        self.one = ProblemOne()

    def test_solve_with_example(self):
        s = self.one.solve(1, 10)
        self.assertEqual(s, 23)

    def test_sovle(self):
        s = self.one.solve(1, 1000)
        self.assertEqual(s, 233168)

def main():
    unittest.main()

if __name__ == "__main__":
    main()