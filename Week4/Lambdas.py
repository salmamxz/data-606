
print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda functions

def square(n):
    return n*n

def percentage(n):
    return n/100

def multiplier(n, m):
    return n*m

def addition(a, b, c):
    return a + b + c

# A1a:
# I used lambda functions to rewrite the original functions in one line each.
# Lambda takes the parameters, performs the calculation and returns the result.

square = lambda n: n * n
percentage = lambda n: n / 100
multiplier = lambda n, m: n * m
addition = lambda a, b, c: a + b + c


print("\nQ1b\n")
# Q1b: Explain how this factorial lambda function works

factorial = lambda a: a * factorial(a-1) if (a > 1) else 1

# A1b:
# This lambda function calculates the factorial of a number using recursion.
# It multiplies the number by the factorial of the previous number.
# The function calls itself with a smaller number until a reaches 1 or less.
# When a is 1 or less, it returns 1. This is the base case that stops recursion.
# For example, factorial(4) calculates 4 * 3 * 2 * 1 and returns 24.


print("\nQ1c\n")
# Q1c: Use map and a lambda function to square all numbers in the list

list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

# A1c:
# I used map() with a lambda function to square every number in the list.
# The lambda takes each number n and multiplies it by itself.
# I used list() to convert the map result into a list and stored it in squared_numbers.

squared_numbers = list(map(lambda n: n * n, list_of_numbers))

print(squared_numbers)

# The output is [529, 119025, 2025, 5776, 7569, 16, 4, 0].
