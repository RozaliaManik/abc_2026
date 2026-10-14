import random
from flask import render_template, request
from app import app
from db import get_collection  # Используем ваше готовое подключение к MongoDB!

# Глобальные переменные для хранения состояния веб-игры
secret_word = ""
current_mask = []
game_hint = ""

def init_web_game():
    """Загружает случайное слово из вашей рабочей MongoDB"""
    global secret_word, current_mask, game_hint
    try:
        collection = get_collection()
        words_from_db = list(collection.find())
        
        if not words_from_db:
            secret_word = "ФЛАСК"
            game_hint = "Дефолтное слово (база пуста)"
        else:
            random_word_doc = random.choice(words_from_db)
            secret_word = random_word_doc["word"].upper()
            game_hint = random_word_doc["hint"]
            
        current_mask = ["*"] * len(secret_word)
    except Exception:
        secret_word = "Парсер"
        game_hint = "Ошибка подключения к Docker БД, проверьте контейнер"
        current_mask = ["*"] * len(secret_word)

# Инициализируем игру при первом запуске сервера
init_web_game()

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Розалия'}
    return render_template('index.html', title='Главная', user=user)

@app.route('/about')
def about():
    return render_template('about.html', title='О нас')

@app.route('/page')
def page():
    global secret_word, current_mask, game_hint
    
    # Если игрок нажал кнопку "Играть заново"
    if request.args.get('restart'):
        init_web_game()
        
    # Получаем букву, которую ввели на сайте
    letter = request.args.get('letter', '').upper()
    
    if letter:
        # Проверяем букву в секретном слове
        for ind, val in enumerate(secret_word):
            if val == letter:
                current_mask[ind] = val
                
    is_won = "*" not in current_mask
    mask_str = " ".join(current_mask)
    
    # Вместо пустого файла page.html используем интерфейс Поля Чудес
    return render_template(
        'page.html', 
        hint=game_hint, 
        mask=mask_str, 
        is_won=is_won
    )
