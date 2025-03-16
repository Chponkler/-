def modus_ponens(temp, humidity, temp_threshold=0.5, hum_threshold=0.6):
    """
    Применяет правило Modus Ponens.
    
    Аргументы:
        temp (float): Значение температуры.
        humidity (float): Значение влажности.
        temp_threshold (float): Порог температуры.
        hum_threshold (float): Порог влажности.
    
    Возвращает:
        str: Результат применения правила.
    """
    if temp > temp_threshold:
        if humidity > hum_threshold:
            return "Q истинно: влажность выше порога"
        else:
            return "Противоречие: ожидается влажность > порога, но это не так"
    else:
        return "P ложно, Modus Ponens не применим"

def modus_tollens(temp, humidity, temp_threshold=0.5, hum_threshold=0.6):
    """
    Применяет правило Modus Tollens.
    
    Аргументы:
        temp (float): Значение температуры.
        humidity (float): Значение влажности.
        temp_threshold (float): Порог температуры.
        hum_threshold (float): Порог влажности.
    
    Возвращает:
        str: Результат применения правила.
    """
    if humidity <= hum_threshold:
        if temp <= temp_threshold:
            return "P ложно: температура ниже порога"
        else:
            return "Противоречие: ожидается температура <= порога, но это не так"
    else:
        return "Q истинно, Modus Tollens не применим"
