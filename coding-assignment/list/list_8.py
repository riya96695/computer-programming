
"Write a Python program to find the length of a string without using the len() function."

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
