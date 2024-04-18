def fibonacci(n):
    # Base cases: If n is 0 or 1, return n
    print(f"Fibonacci called with {n}")
    if n == 0:
        print("Returning 0")
        return 0
    elif n == 1:
        print("Returning 1")
        return 1

    # Recursive case: Return the sum of the previous two Fibonacci numbers
    
    result = fibonacci(n-1) + fibonacci(n-2)
    print(f"Returning {result} for Fibonacci of {n}")
    return result
    

print(fibonacci(5))

# print(2+2/((2+2)+(2**2)))

# print(100 * 0.15)
# print(4096 // 4097)
# print(4096 % 10000)
# print(6 % 5)

# n = 4
# if n*6 > n**2 or n%2 == 0:
#     print("Check")

# # while x % 2 == 0:
# #     x = x / 2

# greeting = 'Hello'
# index = 0
# while index < len(greeting):
#     print(greeting[index:index+1])
#     index += 1

# input = "Four score and seven years ago"
# for c in input:
#   if c.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(c)