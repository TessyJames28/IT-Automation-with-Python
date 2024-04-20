import re

# '.*' means that it matches any character repeated as many times as possible including zero
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
# Use character classes to avoid matching space
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

# The '+' is used to check for multiple occurrence for character that comes before it
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# The '?' is used to specify either zero or one occurrence of that character before it
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))