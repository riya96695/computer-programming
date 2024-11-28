"Write a function that returns the length of a string without using len()."
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
