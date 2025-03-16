from fuzzy_set import FuzzySet
from fuzzy_relation import FuzzyRelation
from matrix_operations import matrix_convolution, transpose_matrix
from logic_operations import modus_ponens, modus_tollens
import numpy as np

# Пример использования
temp_levels = ["низкая", "средняя", "высокая"]
humidity_levels = ["низкая", "средняя", "высокая"]

temperature_set = FuzzySet("Температура", temp_levels, [0.8, 0.5, 0.1])
humidity_set = FuzzySet("Влажность", humidity_levels, [0.7, 0.6, 0.3])

# Создаем и отображаем матрицу отношений
relation = FuzzyRelation(temperature_set, humidity_set)
relation.plot_relation_matrix()

# Пример свёртки матриц
matrix1 = np.array([
    [0.7, 0.6, 0.3],
    [0.5, 0.5, 0.3],
    [0.1, 0.1, 0.1]
])
matrix2 = matrix1
matrix_result = matrix_convolution(matrix1, matrix2)

# Транспонирование матрицы
transposed_matrix = transpose_matrix(relation.relation_matrix)

# Применение логических операций
temperatures = [0.8, 0.5, 0.1]
humidity_levels = [0.7, 0.6, 0.3]

for temp, humidity in zip(temperatures, humidity_levels):
    print(f"Температура: {temp}, Влажность: {humidity}")
    print("Modus Ponens:", modus_ponens(temp, humidity))
    print("Modus Tollens:", modus_tollens(temp, humidity))
    print("-" * 40)
