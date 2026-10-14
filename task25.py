# 10.10.2026
# Rozalia Manik (id postlink=792854)

import random
import pickle  # Подключаем модуль для сериализации
import os

_dict = {'False': 'Логическое значение', 'None': 'Пустой'}
keys = list(_dict.keys())

# Переменные игры (изначально пустые, они заполнятся при старте новой игры или загрузке)
secret = ""
mask = []

def init_new_game():
    """ Инициализация новой игры """
    global secret, mask
    ind = random.randint(0, len(keys) - 1)
    secret = keys[ind]
    mask = ['*'] * len(secret)

def save_game():
    """ Сериализация: сохраняем состояние игры в файл """
    # Собираем все текущие данные игры в один словарь
    data_to_save = {
        'secret': secret,
        'mask': mask
    }
    # Открываем файл для записи в бинарном режиме ('wb')
    with open('savegame.pkl', 'wb') as f:
        pickle.dump(data_to_save, f)  # Сериализуем данные в файл
    print("\n[Игра успешно сохранена!]")

def load_game():
    """ Десериализация: загружаем состояние игры из файла """
    global secret, mask
    # Проверяем, существует ли вообще файл сохранения
    if os.path.exists('savegame.pkl'):
        # Открываем файл для чтения в бинарном режиме ('rb')
        with open('savegame.pkl', 'rb') as f:
            loaded_data = pickle.load(f)  # Десериализуем данные из файла
        
        # Восстанавливаем переменные
        secret = loaded_data['secret']
        mask = loaded_data['mask']
        print("\n[Игра успешно загружена!]")
        return True
    else:
        print("\n[Файл сохранения не найден. Начинаем новую игру.]")
        return False

def show_describe():
    """ Выводит описание слова """
    print("\nПодсказка:", _dict[secret])

def show_secret():
    """ Выводит слово с пробелами между буквами """
    print("Текущее слово:", " ".join(mask))

def get_letter():
    # Добавили подсказку для игрока, как сохранить игру
    letter = input("Введите букву (или 'save' для сохранения, 'exit' для выхода): ")
    return letter

def check_letter(letter):
    for ind, val in enumerate(secret):
        if val.upper() == letter.upper():
            mask[ind] = val

def start():
    global secret, mask
    
    # Спрашиваем игрока при запуске
    choice = input("Загрузить сохраненную игру? (y/n): ").strip().lower()
    if choice == 'y':
        # Если загрузка не удалась (нет файла), создаем новую игру
        if not load_game():
            init_new_game()
    else:
        init_new_game()

    # Главный цикл игры
    while "*" in mask:
        show_describe()
        show_secret()
        letter = get_letter()
        
        # Проверяем команды сохранения и выхода
        if letter.lower() == 'save':
            save_game()
            continue
        elif letter.lower() == 'exit':
            print("Выход из игры.")
            return

        check_letter(letter)
        
    print(f"\nПоздравляем! Слово отгадано: {secret}")
    # После победы удаляем файл сохранения, чтобы не начинать со старого места
    if os.path.exists('savegame.pkl'):
        os.remove('savegame.pkl')

# Запуск игры
start()



