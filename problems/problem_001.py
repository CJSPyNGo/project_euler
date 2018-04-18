
class ProblemOne:

    def sum_from_range(self, min, max):
        sum = 0
        for x in range(min, max):
            if x % 3 == 0 or x % 5 == 0:
                sum = sum + x
        return sum