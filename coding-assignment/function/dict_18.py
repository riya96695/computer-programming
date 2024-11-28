"Write a function to check if a string is an anagram of another string."
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
