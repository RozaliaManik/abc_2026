import requests
from bs4 import BeautifulSoup
from db import get_collection  # Импортируем подключение к MongoDB

# # 1. Исправили URL: добавили 'books.' в начало адреса!
URL = "https://toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print("Подключаемся к тестовому сайту...")
try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    print("Успешно подключились! Скачиваем HTML...")
except requests.exceptions.RequestException as e:
    print(f"❌ Ошибка сети: {e}")
    print("Проверьте, подключен ли интернет на компьютере!")
    exit()

# 2. Разбираем HTML-код страницы
soup = BeautifulSoup(response.text, "lxml")
new_game_words = []

print("Начинаем извлечение слов и подсказок...")

# Ищем карточки товаров на странице книги
book_cards = soup.select("article.product_pod")
print(f"Найдено карточек книг на странице: {len(book_cards)}")

for item in book_cards:
    try:
        # Берем название книги (из атрибута title ссылки)
        full_title = item.select_one("h3 a")["title"]
        
        # Разделяем название на отдельные слова
        words_list = full_title.split()
        if not words_list:
            continue
            
        # Исправлено: берем первое слово по индексу [0] и очищаем его от знаков
        word_text = words_list[0].strip(".,:-!?\"'()").upper()
        
        # Описание (подсказка) — цена книги
        price = item.select_one("p.price_color").get_text(strip=True)
        hint_text = f"Слово из названия книги стоимостью {price}"
        
        # Пропускаем слишком короткие слова или слова с цифрами
        if len(word_text) < 4 or not word_text.isalpha():
            continue
            
        new_game_words.append({
            "word": word_text,
            "category": "Книжный мир",
            "hint": hint_text,
            "difficulty": "средняя",
            "used": False,
            "guessed_count": 0
        })
    except (AttributeError, TypeError, KeyError, IndexError):
        continue

# 3. Автоматически отправляем данные в ваш Docker-контейнер MongoDB
if new_game_words:
    print(f"Парсер отфильтровал и собрал {len(new_game_words)} подходящих слов!")
    
    collection = get_collection()
    collection.delete_many({})  # Очищаем старую коллекцию перед записью
    
    result = collection.insert_many(new_game_words)
    print(f"🎉 ВСЕ СЛОВА УСПЕШНО ЗАПИСАНЫ В MONGODB! Добавлено записей: {len(result.inserted_ids)}")
else:
    print("❌ Не удалось извлечь слова. Проверьте структуру страницы.")

