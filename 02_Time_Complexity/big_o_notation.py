# Big O Notation Examples

# 1. O(1) - Constant Time
def constant_time(arr):
    print("First element:", arr[0])


# 2. O(n) - Linear Time
def linear_time(arr):
    for num in arr:
        print(num)


# 3. O(n^2) - Quadratic Time
def quadratic_time(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# 4. O(log n) - Logarithmic Time
def logarithmic_time(n):
    while n > 1:
        print(n)
        n //= 2


numbers = [10, 20, 30, 40]

print("O(1):")
constant_time(numbers)

print("\nO(n):")
linear_time(numbers)

print("\nO(n^2):")
quadratic_time(numbers)

print("\nO(log n):")
logarithmic_time(16)
