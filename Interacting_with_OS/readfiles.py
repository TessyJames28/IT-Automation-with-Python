file = open("exercise.py")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.read())
file.close()

with open("fib.py") as code:
    print(code.read())