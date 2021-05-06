import numpy as np

def multiplicar(matrix, filtro):
    rowsMatrix, colsMatrix = matrix.shape
    rowsFilter, colsFilter = filtro.shape
    result = 0.0
    for row in range(rowsMatrix):
        for col in range(colsMatrix):
            result += matrix[row, col] * filtro[row, col]
    return result

def padding(padding, matrix):
    paddedMatrix = np.zeros((matrix.shape[0]+padding*2, matrix.shape[1]+padding*2))
    paddedMatrix[ padding : paddedMatrix.shape[0]-padding, padding : paddedMatrix.shape[1] - padding] = matrix
    return paddedMatrix

matrix = np.array( [[1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [0, 0, 1, 16, 17, 18],
                    [0, 1, 0, 7, 23, 24],
                    [1, 7, 6, 5, 4, 3] ])

filterMatrix = np.array([[1, 1, 1],
                        [0, 0, 0],
                        [2,  10, 3]])


rowsMatrix, colsMatrix = matrix.shape
rowsFilter, colsFilter = filterMatrix.shape
x = rowsMatrix - rowsFilter + 1
y = colsMatrix - colsFilter + 1

output = np.zeros((x,y))

for row in range(x):
    for col in range(y):
        output[row,col] = multiplicar(matrix[row : row + rowsFilter, col:col + colsFilter], filterMatrix)

#print(output)
#print(padding(2, matrix))