import unittest
from math import sqrt 
from itertools import count, islice

def get_largest_palindrome_product_from_range(min, max):
    palindromes = []
    for x in range(min, max + 1):
        for y in range(min, max + 1):
            product = x * y

            if is_palindrome(product) and product not in palindromes:
                palindromes.append(product)
    
    sorted_palindromes = sorted(palindromes)
    sorted_palindromes.reverse()
    return sorted_palindromes.pop(0)

def is_palindrome(number):
    number_as_string = str(number)
    list_of_characters = list(number_as_string)
    list_of_characters.reverse()
    reversed_number_as_string = ''.join(list_of_characters)

    if number_as_string == reversed_number_as_string:
        return True
    
    return False

class TestProblemFour(unittest.TestCase):
    def test_two_digit_numbers(self):
        s = get_largest_palindrome_product_from_range(10, 99)
        self.assertEqual(s, 9009)

    def test_three_digit_numbers (self):
        s = get_largest_palindrome_product_from_range(100, 999)
        self.assertEqual(s, 906609)

def main():
    unittest.main()

if __name__ == "__main__":
    main()