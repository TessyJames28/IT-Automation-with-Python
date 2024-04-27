import re

# Splitting per the symbols without capturing the symbols
re.split(r"[.?!]", "One sentence. Another one? And the last one!")

# split and capture the symbols using capturing parenthensis
re.split(r"([.?!])", "One sentence. Another one? And the last one!")

# Replace matches using 'sub'
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")

# Replaces one word with another by grouping
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

# Lookahead: The (?=Passed) is a positive lookahead assertion. (?=Passed) asserts that the text immediately following the hyphen must be "Passed".
r"(Test\d)-(?=Passed)" 
# “Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed” the output would be:
# Test1, Test2, Test4