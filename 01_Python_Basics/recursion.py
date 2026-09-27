# Python Recursion
# A function calling itself is called recursion.

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("Factorial:", factorial(5))


# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci Series:")

for i in range(7):
    print(fibonacci(i), end=" ")


# Sum of first N natural numbers
def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)


print("\nSum:", sum_n(5))


# Reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]


print("Reversed:", reverse_string("Python"))
