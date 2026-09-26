# Python Functions

# Function without parameters
def greet():
    print("Welcome to Python DSA")


greet()


# Function with parameters
def add(a, b):
    return a + b


print("Sum:", add(10, 20))


# Find largest number
def largest(a, b, c):
    return max(a, b, c)


print("Largest:", largest(10, 25, 15))


# Check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(10))
print(check_even_odd(7))


# Factorial using a function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print("Factorial:", factorial(5))