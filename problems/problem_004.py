from math import sqrt 
from itertools import count, islice
from project_euler.spynmath import SpynMath

class ProblemFour:
    def get_largest_palindrome_product_from_range(self, min, max):
        palindromes = []
        math = SpynMath()
        for x in range(min, max + 1):
            for y in range(min, max + 1):
                product = x * y

                if math.is_palindrome(product) and product not in palindromes:
                    palindromes.append(product)
        
        sorted_palindromes = sorted(palindromes)
        sorted_palindromes.reverse()
        return sorted_palindromes.pop(0)
