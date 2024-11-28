"Write a function to find the common elements in two lists."
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

