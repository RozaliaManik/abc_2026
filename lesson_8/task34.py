# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.
#
# Пример использования
# book = Product("Book", 10)
# pen = Product("Pen", 2)
# order = Order()
# order.add_product(book)
# order.add_product(pen)
# print(f"Общая стоимость: {order.total_price}")  # 12

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value if value >= 0 else 0

class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)

    @property
    def total_price(self):
        return sum(p.price for p in self._products)

if __name__ == "__main__":
    # Создаем товары
    book = Product("Book", 10)
    pen = Product("Pen", 2)
    
    # Создаем заказ и добавляем товары
    order = Order()
    order.add_product(book)
    order.add_product(pen)
    
    print("--- Состав заказа ---")
    print(f"Добавлено: {book.name} ({book.price} руб.)")
    print(f"Добавлено: {pen.name} ({pen.price} руб.)")
    print(f"👉 Общая стоимость: {order.total_price} руб.")
    print("-" * 25)
    
    # Проверяем работу удаления товара
    print("\n--- Тест удаления товара ---")
    print(f"Удаляем из заказа: {pen.name}")
    order.remove_product(pen)
    print(f"👉 Общая стоимость после изменения: {order.total_price} руб.")
    print("-" * 25)