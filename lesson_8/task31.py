# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.
#
# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.
#
# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = float(celsius)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = float(value)

    @property
    def fahrenheit(self):
        # Округляем до 1 знака после запятой для красоты
        return round(self._celsius * 9/5 + 32, 1)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (float(value) - 32) * 5/9

    @property
    def kelvin(self):
        # Округляем до 1 знака после запятой
        return round(self._celsius + 273.15, 1)

    @kelvin.setter
    def kelvin(self, value):
        self._celsius = float(value) - 273.15

if __name__ == "__main__":
    # Создаем объект с начальной температурой 25°C
    t = Temperature(25)
    
    print("--- Исходная температура ---")
    print(f"Цельсий:    {t.celsius}°C")
    print(f"Фаренгейт:  {t.fahrenheit}°F")
    print(f"Кельвин:    {t.kelvin} K")
    print("-" * 28)

    # Меняем значение через Фаренгейты
    t.fahrenheit = 32
    
    print("\n--- После установки 32°F ---")
    print(f"Цельсий:    {t.celsius}°C")
    print(f"Фаренгейт:  {t.fahrenheit}°F")
    print(f"Кельвин:    {t.kelvin} K")

