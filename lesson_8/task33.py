# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.
#
# Пример использования
# product = Product("Book", 10)
# print(product.price)  # 10
# product.price = -5
# print(product.price)  # 0

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

if __name__ == "__main__":
    print("--- Создание товара ---")
    product = Product("Book", 10)
    print(f"Товар: {product.name}")
    print(f"Исходная цена: {product.price} руб.")
    print("-" * 25)

    print("\n--- Изменение цены на отрицательную (-5) ---")
    product.price = -5
    print(f"Новая цена: {product.price} руб. (автоматический сброс)")
    print("-" * 25)

