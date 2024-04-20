import re

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

# Search for any character that's not a letter. You use ^ to indicate characters you don't want to match in a square bracket
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# Adding a space in the list of character we don't want to match. 
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# Match either one expression or another
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

# Match both expression using findall
print(re.findall(r"cat|dog", "I like both dogs and cats."))