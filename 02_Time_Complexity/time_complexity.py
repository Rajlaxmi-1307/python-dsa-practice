# Time Complexity Examples

# O(1) - Constant Time
def get_first(arr):
    return arr[0]


# O(n) - Linear Time
def find_sum(arr):
    total = 0

    for num in arr:
        total += num

    return total


# O(n^2) - Quadratic Time
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# O(log n) - Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [10, 20, 30, 40, 50]

print("First element:", get_first(numbers))
print("Sum:", find_sum(numbers))

print("\nAll pairs:")
print_pairs(numbers)

print("\nBinary Search:")
print("Index:", binary_search(numbers, 40))


# Time Complexity:
# get_first      : O(1)
# find_sum       : O(n)
# print_pairs    : O(n^2)
# binary_search  : O(log n)