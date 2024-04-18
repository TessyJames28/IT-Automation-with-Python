def is_palindrome(word):
    reverse = word[::-1]

    if word.lower() == reverse.lower():
        return True
    return False
    
print(is_palindrome("Maname"))

numbers = [(1, 2, 3) for _ in range(5)]
print(numbers)

result = tuple(i for i in range(1,11) if i % 2 == 0)
print(result)

wip = "I am watching"
wip = wip.split()
print(wip)
now = "".join(wip)
print(now)

dic = {"a": [3], "b": 5, "c": 4}
print(len(dic))
print(dic.get("c", "default"))
dic["a"].append(8)
print(dic)