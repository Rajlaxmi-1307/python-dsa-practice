# Conditional Statements

num = int(input("Enter a number: "))

# Positive, negative or zero
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)