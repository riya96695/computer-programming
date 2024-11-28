" Write a Python program to find the sum of digits of a number."

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


