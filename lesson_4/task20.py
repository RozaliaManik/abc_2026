# 18.09.2026
# Rozalia Manik (id postlink=792854)
# Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

import os

file_path = os.path.join(os.path.dirname(__file__), "inverted_sort.txt")

# создать файл с исходным содержимым, если его нет
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
""")

# читаем все строки
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# обратный порядок
reversed_lines = lines[::-1]

# дописываем в тот же файл
with open(file_path, "a", encoding="utf-8") as f:
    f.writelines(reversed_lines)

print(f"Обратные строки дописаны в {file_path}")
