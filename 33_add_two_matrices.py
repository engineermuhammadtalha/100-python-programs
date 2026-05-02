# add two matrices (equal size)
A= [[1,2],[3,4]]
B= [[5,6],[7,8]]
c =[[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(c)  # Output: [[6, 8], [10, 12]]