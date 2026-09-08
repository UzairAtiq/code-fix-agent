def sum_range(n):
    total = 0
    for i in range(n):
        total += i
    return total

assert sum_range(5) == 15
