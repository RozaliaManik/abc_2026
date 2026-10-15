# 15.10.2026
# Rozalia Manik (id postlink=792854)

class NotificationSender:
    def send(self, message: str, user):
        """Базовый метод для отправки уведомлений. Переопределяется наследниками."""
        pass


class EmailSender(NotificationSender):
    def send(self, message: str, user):
        # Email выводит весь текст сообщения
        print(f"Email для {user.name} | Образовательная платформа | {message}")


class SMSSender(NotificationSender):
    def send(self, message: str, user):
        # SMS обрезает сообщение до первых 50 символов
        short_message = message[:50]
        print(f"SMS для {user.name} | {short_message}")


class PushSender(NotificationSender):
    def send(self, message: str, user):
        # Push выводит весь текст с эмодзи шапочки выпускника
        print(f"Push для {user.name} | 🎓 {message}")


class User:
    def __init__(self, name: str, preferred_notifications: list):
        self.name = name
        # Хранит список объектов-отправителей (экземпляров классов выше)
        self.preferred_notifications = preferred_notifications


def notify_user(user: User, message: str):
    """Полиморфно вызывает метод send каждого выбранного пользователем отправителя."""
    for sender in user.preferred_notifications:
        sender.send(message, user)


# --- Пример использования по условию задачи ---
if __name__ == "__main__":
    # Создаем каналы уведомлений (email и push)
    email_channel = EmailSender()
    push_channel = PushSender()
    
    # Создаем пользователя Марию с её списком каналов
    maria = User("Мария", [email_channel, push_channel])
    
    # Текст уведомления
    notification_text = "Блок аналитики начинается с 27 октября!"
    
    # Рассылаем уведомления выбранными способами
    notify_user(maria, notification_text)
