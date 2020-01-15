# Problem 1
# sum35(max value) -> sum of values under max which are multiples of 3 or 5

def sum35(max):
    sum = 0
    for i in range(max):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum
