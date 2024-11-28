"Write a Python program to find the common elements in two lists."
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
