# 15.10.2026
# Rozalia Manik (id postlink=792854)

class Temperature:
    def __init__(self, celsius: float):
        # Храним температуру только в градусах Цельсия
        self._celsius = float(celsius)

    # --- Свойство Цельсий ---
    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        self._celsius = float(value)

    # --- Свойство Фаренгейт ---
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        # Вычисляем Цельсий на основе Фаренгейта
        self._celsius = (float(value) - 32) * 5 / 9

    # --- Свойство Кельвин ---
    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float):
        # Вычисляем Цельсий на основе Кельвина
        self._celsius = float(value) - 273.15


# --- Пример использования по условию задачи ---
if __name__ == "__main__":
    # Создаем температуру 25 °C
    t = Temperature(25)
    
    # Выводим значения Цельсия, Фаренгейта и Кельвина
    print(t.celsius)
    print(t.fahrenheit)
    print(t.kelvin)
    
    # Устанавливаем 32 °F
    t.fahrenheit = 32
    
    # Снова выводим Цельсии
    print(t.celsius)
