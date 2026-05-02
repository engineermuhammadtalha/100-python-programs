# fibonacci sequence (first n terms)
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

fibonacci_sequence(8)  # output: 0 1 1 2 3 5 8 13