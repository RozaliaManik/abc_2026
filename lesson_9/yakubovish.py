# 15.10.2026
# Rozalia Manik (id postlink=792854)

import csv
import random
from datetime import datetime
# Импортируем словарь из модуля db, как указано в задании
from db import DICT_DEFENITION_WORD


class Yakubovich:

    def __init__(self):
        # Имя запрашивается сразу при инициализации
        self.name = input("Введите ваше имя: ").strip()
        self.word = ""
        self.mask = ""
        self.session = ""

    def _generate_key(self):
        # Генерируем уникальный ID для сессии (можно использовать timestamp или случайное число)
        return f"session-{int(datetime.now().timestamp())}-{random.randint(1000, 9999)}"

    def print_menu(self):
        while True:
            print("\n--- Меню ---")
            print("1 — Новая партия")
            print("2 — Загрузка партии")
            print("3 — Выход")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                # Выбираем случайное слово из словаря
                self.word = random.choice(list(DICT_DEFENITION_WORD.keys()))
                self.mask = "#" * len(self.word)
                self.session = self._generate_key()
                print(f"Загадано слово из {len(self.word)} букв. Подсказка: {DICT_DEFENITION_WORD[self.word]}")
                self.start_game()
            elif choice == "2":
                if self.load_game():
                    self.start_game()
            elif choice == "3":
                self.end_game()
                break
            else:
                print("Неверный ввод, попробуйте еще раз.")

    def start_game(self):
        while "#" in self.mask:
            print(f"Текущая маска: {list(self.mask)}")
            guess = input("Введите букву (или '2' для сохранения): ").strip().lower()

            if guess == "2":
                self.save_game()
                print("Игра сохранена. Продолжаем партию.")
                continue

            if not guess or len(guess) != 1:
                print("Пожалуйста, введите одну букву.")
                continue

            # Открываем все вхождения буквы
            new_mask = ""
            found = False
            for i, letter in enumerate(self.word):
                if letter == guess:
                    new_mask += letter
                    found = True
                else:
                    new_mask += self.mask[i]
            
            self.mask = new_mask

            if found:
                print(f"Отлично! Буква '{guess}' есть в слове.")
            else:
                print(f"Увы, буквы '{guess}' нет в слове.")

        # Если маска полностью открыта
        print(f"\nПоздравляем! Вы угадали слово: {self.word}")
        print(list(self.mask))

    def save_game(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        row = [date_str, self.session, self.name, self.word, self.mask]
        
        # Дописываем запись в файл save_game.csv с разделителем |
        with open("save_game.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter="|")
            writer.writerow(row)

    def load_game(self):
        try:
            player_saves = []
            # Читаем все сохранения из файла
            with open("save_game.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter="|")
                for row in reader:
                    if row and row[2] == self.name:
                        player_saves.append(row)
            
            if not player_saves:
                print("У вас нет сохраненных партий.")
                return False

            print("\nВаши сохранения:")
            for idx, save in enumerate(player_saves):
                # Выводим индекс, дату, маску и подсказку к слову
                print(f"{idx} — Дата: {save[0]} | Маска: {save[4]} (Сессия: {save[1]})")

            chosen_idx = input("Введите номер строки для загрузки: ").strip()
            if not chosen_idx.isdigit() or int(chosen_idx) >= len(player_saves):
                print("Некорректный номер.")
                return False

            # Восстанавливаем состояние игры из выбранной строки
            selected_save = player_saves[int(chosen_idx)]
            self.session = selected_save[1]
            self.word = selected_save[3]
            self.mask = selected_save[4]
            print(f"Игра успешно загружена! Подсказка: {DICT_DEFENITION_WORD[self.word]}")
            return True

        except FileNotFoundError:
            print("Файл сохранений save_game.csv еще не создан.")
            return False

    def end_game(self):
        print(f"Спасибо за игру, {self.name}! До новых встреч на Поле чудес!")


# Точка входа в скрипт
if __name__ == "__main__":
    game = Yakubovich()
    game.print_menu()