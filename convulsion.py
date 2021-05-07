import numpy as np
import argparse
import matplotlib.pyplot as plt
import cv2

def multiplicar(matrix, filtro):
    rows_matrix, cols_matrix = matrix.shape
    rows_filter, cols_filter = filtro.shape
    result = 0.0
    for row in range(rows_matrix):
        for col in range(cols_matrix):
            result += matrix[row, col] * filtro[row, col]
    return result

def padding(padding, matrix):
    # Si es una imagen RGB la convierte a una escala de grises
    if len(matrix.shape) == 3:
        matrix = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        print("Image Shape : {}".format(matrix.shape))

    padded_matrix = np.zeros((matrix.shape[0] + padding*2, matrix.shape[1] + padding*2))
    padded_matrix[padding : padded_matrix.shape[0]-padding, padding : padded_matrix.shape[1]-padding] = matrix
    
    plt.imshow(padded_matrix, cmap='gray')
    plt.title("Padded Image")
    plt.show()
    
    return padded_matrix


def convulsion(matrix, filtro):
    matrix = padding(5, matrix)
    rows_matrix, cols_matrix = matrix.shape
    rows_filter, cols_filter = filtro.shape
    x = rows_matrix - rows_filter + 1
    y = cols_matrix - cols_filter + 1

    output = np.zeros((x,y))

    for row in range(x):
        for col in range(y):
            output[row,col] = multiplicar(matrix[row : row + rows_filter, col:col + cols_filter], filtro)

    plt.imshow(output, cmap='gray')
    plt.title("Laplacian")
    plt.show()


filtro = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])


if __name__ == '__main__':
    image = cv2.imread("arcos.jpg")
    convulsion(image, filtro)

#print(output)
#print(padding(2, matrix))