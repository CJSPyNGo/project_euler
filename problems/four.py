from math import sqrt 
from itertools import count, islice

class ProblemFour:
    def get_largest_palindrome_product_from_range(self, min, max):
        palindromes = []
        for x in range(min, max + 1):
            for y in range(min, max + 1):
                product = x * y

                if self.is_palindrome(product) and product not in palindromes:
                    palindromes.append(product)
        
        sorted_palindromes = sorted(palindromes)
        sorted_palindromes.reverse()
        return sorted_palindromes.pop(0)

    def is_palindrome(self, number):
        number_as_string = str(number)
        list_of_characters = list(number_as_string)
        list_of_characters.reverse()
        reversed_number_as_string = ''.join(list_of_characters)

        if number_as_string == reversed_number_as_string:
            return True
        
        return False
