# factors of n 
n = 28 
factors = [i for i in range(1, n + 1) if n % i == 0]
print(factors)  # Output: [1, 2, 4, 7, 14, 28]