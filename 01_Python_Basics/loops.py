# Python Loops

# For loop
print("For Loop:")

for i in range(1, 6):
    print(i)

# While loop
print("While Loop:")

i = 1
while i <= 5:
    print(i)
    i += 1

# Sum of first N natural numbers
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)

# Multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)