import numpy as np
import argparse
import matplotlib.pyplot as plt
import cv2

# Función que ayuda a la multiplicación y suma para la convulsión
def multiplicar(matrix, filtro):
    rows_matrix, cols_matrix = matrix.shape
    rows_filter, cols_filter = filtro.shape
    result = 0.0
    
    # Hace las operaciones necesarias para realizar la convulsion
    for row in range(rows_matrix):
        for col in range(cols_matrix):
            result += matrix[row, col] * filtro[row, col]
    
    return result


# Añade padding a una matriz o imagen según la cantidad introducida
def padding(padding, matrix):
    # Si es una imagen RGB la convierte a una escala de grises
    if len(matrix.shape) == 3:
        matrix = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        print("Image Shape : {}".format(matrix.shape))

    # Crea una matriz de la imagen con padding 
    padded_matrix = np.zeros((matrix.shape[0] + padding*2, matrix.shape[1] + padding*2))
    padded_matrix[padding : padded_matrix.shape[0]-padding, padding : padded_matrix.shape[1]-padding] = matrix
    
    # Grafica la imagen con padding
    plt.imshow(padded_matrix, cmap='gray')
    plt.title("Padded Image")
    plt.show()
    
    return padded_matrix

# Función que hace la convulsion de una imagen o matriz con un filtro
def convulsion(matrix, filtro):
    matrix = padding(5, matrix)
    rows_matrix, cols_matrix = matrix.shape
    rows_filter, cols_filter = filtro.shape
    x = rows_matrix - rows_filter + 1
    y = cols_matrix - cols_filter + 1

    output = np.zeros((x,y))

    # Hace las operaciones de la matriz de imagen con el filtro a convulcionar necesarias
    for row in range(x):
        for col in range(y):
            output[row,col] = multiplicar(matrix[row : row + rows_filter, col:col + cols_filter], filtro)

    # Grafica la imagen con el filtro Laplacian ya convolucionado
    plt.imshow(output, cmap='gray')
    plt.title("Laplacian")
    plt.show()

# Matriz del filtro Laplacian que se aplicara
filtro = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])

# Main para correr una prueba con la imagen 'arcos.jpg'
if __name__ == '__main__':
    image = cv2.imread("arcos.jpg")
    convulsion(image, filtro)