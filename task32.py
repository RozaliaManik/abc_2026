# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.
#
# Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# # print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Некорректный email")
        self._email = value

    @property
    def password(self):
        raise AttributeError("Доступ к паролю запрещен!")

    @password.setter
    def password(self, value):
        # Храним только хэш пароля для безопасности
        self._password_hash = hash(value)

    def check_password(self, password):
        """Проверяет, соответствует ли переданный пароль хэшу"""
        return hash(password) == self._password_hash

if __name__ == "__main__":
    print("--- Создание пользователя ---")
    user = User("test@example.com", "secret")
    print(f"Email пользователя: {user.email}")
    print("-" * 30)

    print("\n--- Проверка паролей ---")
    
    # Тест 1: Правильный пароль
    pass1 = "secret"
    result1 = user.check_password(pass1)
    status1 = "✅ Доступ разрешен" if result1 else "❌ Неверный пароль"
    print(f"Ввод: '{pass1}' -> {status1}")

    # Тест 2: Неправильный пароль (исправлена опечатка в вызове метода)
    pass2 = "wrong"
    result2 = user.check_password(pass2)
    status2 = "✅ Доступ разрешен" if result2 else "❌ Неверный пароль"
    print(f"Ввод: '{pass2}'  -> {status2}")
    
    print("-" * 30)

