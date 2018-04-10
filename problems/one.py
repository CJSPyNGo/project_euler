def sum_from_range(min, max):
    sum = 0
    for x in range(min, max):
        if x % 3 == 0 or x % 5 == 0:
            sum = sum + x
            print(x)
    print("The sum is: %d" % sum)
    return sum