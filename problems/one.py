import unittest

def sum_from_range(min, max):
    sum = 0
    for x in range(min, max):
        if x % 3 == 0 or x % 5 == 0:
            sum = sum + x
    return sum

class TestProblemOne(unittest.TestCase):

    def test_10(self):
        s = sum_from_range(1, 10)
        self.assertEqual(s, 23)

    def test_1000(self):
        s = sum_from_range(1, 1000)
        self.assertEqual(s, 233168)

def main():
    unittest.main()

if __name__ == "__main__":
    main()