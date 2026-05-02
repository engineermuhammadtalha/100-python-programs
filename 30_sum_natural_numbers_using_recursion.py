# sum using recursion
def sum_rec(n):
    return 0 if n == 0 else n + sum_rec(n - 1)
print(sum_rec(10))  # Output: 55 