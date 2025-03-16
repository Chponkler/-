import numpy as np

def matrix_convolution(matrix1, matrix2):
    """
    Выполняет свёртку двух матриц с использованием минимума и максимума.
    
    Аргументы:
        matrix1 (np.ndarray): Первая матрица.
        matrix2 (np.ndarray): Вторая матрица.
    
    Возвращает:
        np.ndarray: Результат свёртки.
    """
    assert matrix1.shape[1] == matrix2.shape[0], "Размеры матриц не совпадают для свёртки."
    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    print("Выполнение свёртки матриц:")
    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            row = matrix1[i, :]
            column = matrix2[:, j]
            min_values = np.minimum(row, column)
            result[i, j] = np.max(min_values)
            print(f"Строка {i}, столбец {j}:")
            print(f"  Строка: {row}")
            print(f"  Столбец: {column}")
            print(f"  Минимальные значения: {min_values}")
            print(f"  Максимум из минимальных значений: {result[i, j]}")
    print("Результат свёртки матриц:")
    print(result)
    return result

def transpose_matrix(matrix):
    """
    Транспонирует матрицу.
    
    Аргументы:
        matrix (np.ndarray): Исходная матрица.
    
    Возвращает:
        np.ndarray: Транспонированная матрица.
    """
    transposed = matrix.T
    print("Транспонированная матрица:")
    print(transposed)
    return transposed
