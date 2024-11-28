"Check if a string is a valid email"
import re

def is_valid_email(string):
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", string))

print(is_valid_email("test@example.com"))
print(is_valid_email("invalid-email"))
