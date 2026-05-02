#  Matrix multiplication (A m x p, B p x n)
A = [[1,2,3],[4,5,6]]
B = [[7,8],[9,10],[11,12]]
result = [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print(result)  # Output: [[58,64],[139,154]]
