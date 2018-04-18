
class ProblemFive:
    
    def solve_v2(self):
        numbers_to_check = [11, 12, 13, 14, 16, 17, 18, 19, 20]

        # every number is divisible by 1 so we don't have to check it
        # any number divisible by 20 is also divisible by 10, 5, 4, and 2, so we don't have to check 10, 5, 4, or 2
        # any number divisible by 18 is also divisible by 9. so we don't have to check 9
        # any number divisible by 16 is also divisible by 8. so we don't have to check 8
        # any number divisible by 15 is also divisible by 5. we don't need to check 5 because we're checking 20. so we don't have to check 15
        # any number divisible by 14 is also divisible by 7. so we don't have to check 7
        # any number divisible by 12 is also divisible by 6. so we don't have to check 6
        # any number divisible by 9 is also divisible by 3. so we don't have to check 3
        
        # we'll start at the square of the largest of the numbers to check
        # the number we're searching for MUST be divisible by the largest number in the numbers to check, 
        # so we'll square it to start
        possible_number = 20 * 20
        is_divisible = False

        while not is_divisible:
            is_divisible = True

            for number in numbers_to_check:
                if possible_number % number != 0:
                    is_divisible = False
                    possible_number = possible_number + 1
                    break
        return possible_number

    def solve(self, min, max):
        possible_number = max * max
        is_divisible = False

        if min == 1:
            # every number is divisible by 1
            # and we'll check 2 by default
            min == 3

        while not is_divisible:
            is_divisible = True
            if possible_number % 2 != 0 or possible_number % 5 != 0:
                # if the number isn't divisible by 2 and 5 there's no point in continuing
                is_divisible = False
                possible_number = possible_number + 1
                continue

            for number in range(min, max + 1):
                if possible_number % number != 0:
                    is_divisible = False
                    possible_number = possible_number + 1
                    break
            
        return possible_number
