# 3x3 matrix
matrix1 = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
# 3x4 matrix
matrix2 = [[5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
# iterate through rows of X
for i in range(len(matrix1)):
   # iterate through columns of Y
   for j in range(len(matrix2[0])):
       # iterate through rows of Y
       for k in range(len(matrix2)):
           result[i][j] += matrix2[i][k] * matrix2[k][j]
for i in result:
   print(i)