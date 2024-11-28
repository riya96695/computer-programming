"Write a function that returns the GCD (Greatest Common Divisor) of two numbers."
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
