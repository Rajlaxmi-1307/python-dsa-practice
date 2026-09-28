# Space Complexity Examples

# O(1) - Constant Space
def constant_space(n):
    result = n * 2
    return result


# O(n) - Linear Space
def linear_space(n):
    numbers = []

    for i in range(n):
        numbers.append(i)

    return numbers


# O(n) - Recursive Space
def recursive_sum(n):
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


print("Constant Space:")
print(constant_space(5))

print("\nLinear Space:")
print(linear_space(5))

print("\nRecursive Sum:")
print(recursive_sum(5))


# Space Complexity:
# constant_space : O(1) auxiliary space
# linear_space   : O(n) auxiliary space
# recursive_sum  : O(n) call stack space