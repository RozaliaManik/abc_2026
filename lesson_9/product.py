# 15.10.2026
# Rozalia Manik (id postlink=792854)

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        # Присваиваем цену через сеттер, чтобы проверка сработала и при создании товара
        self.price = price

    # --- Свойство name (Чтение и Запись) ---
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    # --- Свойство price (Чтение и Запись с валидацией) ---
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        # Если цена отрицательная, устанавливаем её в 0
        if value < 0:
            self._price = 0.0
        else:
            self._price = float(value)


# --- Пример использования по условию задачи ---
if __name__ == "__main__":
    # Создаем Product('Book', 10)
    product = Product('Book', 10)
    
    # Выводим первоначальную цену
    print(product.price)
    
    # Присваиваем цене -5
    product.price = -5
    
    # Выводим цену снова, чтобы убедиться в автоматической замене на 0
    print(product.price)
