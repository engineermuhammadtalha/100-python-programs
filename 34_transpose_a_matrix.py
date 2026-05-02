# transpose
mat = [[1,2,3],[4,5,6]]
transposed= list(map(list, zip(*mat)))
print(transposed)  # Output: [[1, 4], [2, 5], [3, 6]]