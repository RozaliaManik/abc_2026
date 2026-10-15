# 15.10.2026
# Rozalia Manik (id postlink=792854)

class User:
    def __init__(self, email: str, password: str):
        # Переменная под email изначально пустая для корректной работы сеттера
        self._email = ""
        # Вызываем сеттер для проверки email при создании объекта
        self.email = email
        # Вызываем сеттер для хеширования пароля при создании объекта
        self.password = password

    # --- Свойство email (Чтение и Запись) ---
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, new_email: str):
        if "@" not in str(new_email):
            raise ValueError("Некорректный формат адреса электронной почты (отсутствует '@').")
        self._email = str(new_email)

    # --- Свойство password (Только Запись) ---
    @property
    def password(self):
        # Попытка чтения вызывает AttributeError по условию
        raise AttributeError("Чтение пароля запрещено из соображений безопасности.")

    @password.setter
    def password(self, new_password: str):
        # Храним хеш пароля с помощью встроенной функции hash()
        self._password_hash = hash(str(new_password))

    # --- Метод проверки пароля ---
    def check_password(self, password: str) -> bool:
        """Сравнивает хеш переданного пароля с текущим хешем в системе."""
        return self._password_hash == hash(str(password))


# --- Пример использования по условию задачи ---
if __name__ == "__main__":
    # Создаем пользователя с адресом test@example.com и паролем secret
    user = User("test@example.com", "secret")
    
    # Выводим адрес
    print(user.email)
    
    # Выводим результаты проверки паролей secret и wrong
    print(user.check_password("secret"))
    print(user.check_password("wrong"))
