class FuzzySet:
    """
    Класс для представления нечёткого множества.
    
    Атрибуты:
        name (str): Название множества.
        elements (list): Элементы множества.
        membership_values (list): Значения принадлежности элементов.
    """
    def __init__(self, name, elements, membership_values):
        self.name = name
        self.elements = elements
        self.membership_values = membership_values
