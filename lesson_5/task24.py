# 22.09.2026
# Rozalia Manik (id postlink=792854)
#  Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

import os

file_path = os.path.join(os.path.dirname(__file__), "message.txt")
out_path = os.path.join(os.path.dirname(__file__), "message_encrypted.txt")

# создаём пример файла если нет
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Привет мир\n")
        f.write("Это тест шифра Цезаря\n")
        f.write("Кириллица работает\n")

alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_upper = alphabet_lower.upper()
alphabet_size = len(alphabet_lower)

def shift_char(ch, shift):
    if ch in alphabet_lower:
        idx = alphabet_lower.index(ch)
        new_idx = (idx - shift) % alphabet_size
        return alphabet_lower[new_idx]
    if ch in alphabet_upper:
        idx = alphabet_upper.index(ch)
        new_idx = (idx - shift) % alphabet_size
        return alphabet_upper[new_idx]
    return ch

encrypted_lines = []
with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        shift = i
        enc_line = "".join(shift_char(ch, shift) for ch in line.rstrip("\n"))
        encrypted_lines.append(enc_line)

with open(out_path, "w", encoding="utf-8") as f:
    for line in encrypted_lines:
        f.write(line + "\n")

print(f"Зашифровано в {out_path}")
for line in encrypted_lines:
    print(line)
