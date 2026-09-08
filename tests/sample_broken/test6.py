def find_max(numbers):
    max_num = 0
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

assert find_max([-5, -2, -10]) == -2
