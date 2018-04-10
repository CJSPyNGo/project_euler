import unittest

def sum_from_even_fib(max):
    even_numbers = [] 
    
    previous_number = 1
    current_number = 2
    while current_number < max:
        original_number = previous_number
        if current_number % 2 == 0:
            even_numbers.append(current_number)
        previous_number = current_number
        current_number = original_number + current_number
    
    sum = 0
    for number in even_numbers:
        sum = sum + number

    return sum

class TestProblemTwo(unittest.TestCase):

    def test_10(self):
        s = sum_from_even_fib(10)
        self.assertEqual(s, 10)

    def test_4000000(self):
        s = sum_from_even_fib(4000000)
        self.assertEqual(s, 4613732)

def main():
    unittest.main()

if __name__ == "__main__":
    main()