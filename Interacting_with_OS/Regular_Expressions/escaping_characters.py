import re

# Use backslash '\' to escape special characters
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

# '\w' matches any alphanumeric characters including letters, numbers, and _ 
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))