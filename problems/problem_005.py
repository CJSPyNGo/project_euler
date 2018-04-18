
class ProblemFive:
    
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
