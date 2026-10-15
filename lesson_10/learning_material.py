# 15.10.2026
# Rozalia Manik (id postlink=792854)

class LearningMaterial:
    def __init__(self, title: str, author: str, duration_minutes: int):
        self.title = title
        self.author = author
        self.duration_minutes = duration_minutes

    def display_info(self) -> str:
        """Возвращает базовую информацию о материале через вертикальную черту."""
        return f"{self.title} | {self.author} | {self.duration_minutes}"

    def get_difficulty(self) -> str:
        """Возвращает сложность по умолчанию."""
        return "Средняя"


class VideoLesson(LearningMaterial):
    def __init__(self, title: str, author: str, duration_minutes: int, video_quality: str, subtitles_available: bool):
        super().__init__(title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available

    def get_difficulty(self) -> str:
        # Сложность видеоурока всегда Средняя
        return "Средняя"


class Article(LearningMaterial):
    def __init__(self, title: str, author: str, duration_minutes: int, word_count: int, reading_level: str):
        super().__init__(title, author, duration_minutes)
        self.word_count = word_count
        self.reading_level = reading_level

    def get_difficulty(self) -> str:
        # Вычисление сложности на основе количества слов
        if self.word_count < 1000:
            return "Лёгкая"
        elif 1000 <= self.word_count <= 3000:
            return "Средняя"
        else:
            return "Сложная"


class Quiz(LearningMaterial):
    def __init__(self, title: str, author: str, duration_minutes: int, questions_count: int, passing_score: int):
        super().__init__(title, author, duration_minutes)
        self.questions_count = questions_count
        self.passing_score = passing_score

    def get_difficulty(self) -> str:
        # Вычисление сложности на основе проходного процента
        if self.passing_score > 80:
            return "Высокая"
        else:
            return "Средняя"


# --- Пример использования по условию задачи ---
if __name__ == "__main__":
    # 1. Создаем видеоурок
    video = VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True)
    
    # 2. Создаем статью
    article = Article("Глубокое обучение", "Анна Петрова", 10, 1200, "advanced")
    
    # 3. Создаем тест
    quiz = Quiz("Проверка знаний", "Платформа", 20, 10, 75)

    # Выводим название и сложность каждого материала в заданном порядке
    print(f"{video.title}: {video.get_difficulty()}")
    print(f"{article.title}: {article.get_difficulty()}")
    print(f"{quiz.title}: {quiz.get_difficulty()}")
