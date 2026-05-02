# 34) Decimal to binary recursion
def dec_to_bin(n):
    if n == 0: return "0"
    def rec(x):
        return "" if x == 0 else rec(x//2) + str(x%2)
    return rec(n)
print(dec_to_bin(10))  # Output: 1010
