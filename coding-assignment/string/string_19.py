"Remove all digits from a string"
def remove_digits(string):
    return ''.join([i for i in string if not i.isdigit()])

print(remove_digits("Hello123 World456"))
