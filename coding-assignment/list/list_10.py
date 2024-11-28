"Write a Python program to count the number of vowels"
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
