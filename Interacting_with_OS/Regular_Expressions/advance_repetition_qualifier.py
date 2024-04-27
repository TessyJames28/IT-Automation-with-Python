import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# This finds all words with upto five characters
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# '\b' letter at the beginning and end of a pattern meaning we want full words
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")

# Search for words with a range of 5 - 10 characters
print(re.findall(r"\w{5,10}", "I really like strawberries"))

# Words with 5 characters or more
print(re.findall(r"\w{5,}", "I really like strawberries"))

# This means from 0 upto that amount of repetition
# we look for character thmat starts withm 's' follows by upto 20 numeric characters
print(re.search(r"s\w{,20}", "I really like strawberries"))

