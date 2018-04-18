class ProblemTwo:

    def sum_from_even_fib(self, max):
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
