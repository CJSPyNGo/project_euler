import unittest
from .one import ProblemOne

class ProblemOneTests(unittest.TestCase):

    def setUp(self):
        self.one = ProblemOne()

    def test_10(self):
        s = self.one.sum_from_range(1, 10)
        self.assertEqual(s, 23)

    def test_1000(self):
        s = self.one.sum_from_range(1, 1000)
        self.assertEqual(s, 233168)

def main():
    unittest.main()

if __name__ == "__main__":
    main()