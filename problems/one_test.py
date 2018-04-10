import 1
import unittest

class TestStringMethods(unittest.TestCase):

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