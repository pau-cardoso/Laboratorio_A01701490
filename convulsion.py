import numpy as np

def multiplicar(matrix, filtro):
    colMatrix = len(matrix[0])
    rowMatrix = len(matrix)
    colFilter = len(filtro[0])
    rowFilter = len(filtro)
    result = 0.0
    for row in matrix:
        for col in matrix[row]:
            result += matrix[row, col] * filtro[row, col]
    return result

matrix = [  [1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12],
            [0, 0, 1, 16, 17, 18],
            [0, 1, 0, 7, 23, 24],
            [1, 7, 6, 5, 4, 3] ]

filterMatrix = [[1, 1, 1],
                [0, 0, 0],
                [2, 10, 3]]

convultion = []

colsMatrix = len(matrix[0])
rowsMatrix = len(matrix)
colsFilter = len(filterMatrix[0])
rowsFilter = len(filterMatrix)

for row in range(rowsMatrix):
    for col in range(colsMatrix):
        
        multiplicar(matrix[row : row + rowsFilter, col:col + colsFilter], filterMatrix)

