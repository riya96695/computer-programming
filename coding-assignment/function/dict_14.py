"Write a function that returns the factorial of a number iteratively."
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
