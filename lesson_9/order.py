# 15.10.2026
# Rozalia Manik (id postlink=792854)

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        # Присвоение через сеттер, чтобы проверка сработала и при создании товара
        self.price = price

    # --- Свойство name (Чтение и Запись) ---
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    # --- Свойство price (Чтение и Запись) ---
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        # Если цена отрицательная, заменяем её нулём
        if value < 0:
            self._price = 0.0
        else:
            self._price = float(value)


class Order:
    def __init__(self):
        # Внутренний список для хранения экземпляров товаров
        self.products = []

    def add_product(self, product: Product):
        """Добавляет товар в заказ."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Удаляет одно вхождение товара, если оно есть в заказе."""
        if product in self.products:
            self.products.remove(product)

    # --- Свойство total_price (Только для чтения) ---
    @property
    def total_price(self) -> float:
        """Каждый раз динамически вычисляет сумму текущих цен товаров."""
        return sum(item.price for item in self.products)


# --- Пример использования по условию задачи ---
if __name__ == "__main__":
    # Создаем заказ
    my_order = Order()
    
    # Создаем товары: книга за 10 и ручка за 2
    book = Product('Книга', 10)
    pen = Product('Ручка', 2)
    
    # Помещаем товары в заказ
    my_order.add_product(book)
    my_order.add_product(pen)
    
    # Выводим общую стоимость заказа
    print(my_order.total_price)
