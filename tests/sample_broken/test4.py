def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n - 1)

assert factorial(5) == 120
