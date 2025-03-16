import numpy as np
import matplotlib.pyplot as plt
from .fuzzy_set import FuzzySet

class FuzzyRelation:
    """
    Класс для представления отношений между двумя нечёткими множествами.
    
    Атрибуты:
        set1 (FuzzySet): Первое нечёткое множество.
        set2 (FuzzySet): Второе нечёткое множество.
        relation_matrix (np.ndarray): Матрица отношений.
    """
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2
        self.relation_matrix = self.build_relation_matrix()

    def build_relation_matrix(self):
        """
        Строит матрицу отношений на основе операции минимума.
        
        Возвращает:
            np.ndarray: Матрица отношений.
        """
        matrix = np.zeros((len(self.set1.membership_values), len(self.set2.membership_values)))
        print(f"Вычисление матрицы отношений для {self.set1.name} и {self.set2.name}:")
        for i, val1 in enumerate(self.set1.membership_values):
            for j, val2 in enumerate(self.set2.membership_values):
                matrix[i, j] = min(val1, val2)
                print(f"Ячейка [{i}, {j}] ({self.set1.elements[i]}, {self.set2.elements[j]}) -> "
                      f"min({val1}, {val2}) = {matrix[i, j]}")
        return matrix

    def plot_relation_matrix(self):
        """
        Визуализирует матрицу отношений с помощью тепловой карты.
        """
        plt.imshow(self.relation_matrix, cmap="viridis", interpolation="nearest")
        plt.colorbar(label="Membership Value")
        plt.xlabel(f"{self.set2.name} Levels")
        plt.ylabel(f"{self.set1.name} Levels")
        plt.title(f"Fuzzy Relation Matrix between {self.set1.name} and {self.set2.name}")
        for i in range(self.relation_matrix.shape[0]):
            for j in range(self.relation_matrix.shape[1]):
                plt.text(j, i, f"{self.relation_matrix[i, j]:.2f}", ha="center", va="center", color="white")
        plt.show()
