# 11.10.2026
# Rozalia Manik (id postlink=792854)
# 1. Создайте виртуальное окружение через терминал в текущей папки нового проекта.
# Название окружению дайте по названию проекта. Переключитесь на созданное новое окружение.
#
# 2. Установите пакет pandas.
# Убедитесь что он установился и добавился в папку виртуального окружения.
#
# 3. Создайте файл test_package.py в него добавьте строки
# import pandas as pd
# pd.test()
# Убедитесь что пакет подключен.
#
# 4. Создайте свой пакет helpers со структурой
# helpers
#     __init__.py
#     io.py
#     crypt.py
#
# В модуль io.py разместите ранее написаный logger
# В модуль crypt.py добавьте функцию шифра цезаря.
#
# 5. Создайте новый файл test.py  Подключите в него функцию логера и шифрования.
# Проверьте их работу.

import os

project_dir = os.path.dirname(__file__)

# 1. Создание venv
# python -m venv venv
# venv\Scripts\activate   # Windows

# 2. Установка pandas
# pip install pandas

# 3. test_package.py
test_package_code = """import pandas as pd
print("pandas version:", pd.__version__)
"""

with open(os.path.join(project_dir, "test_package.py"), "w", encoding="utf-8") as f:
    f.write(test_package_code)

# 4. Пакет helpers
helpers_dir = os.path.join(project_dir, "helpers")
os.makedirs(helpers_dir, exist_ok=True)

with open(os.path.join(helpers_dir, "__init__.py"), "w", encoding="utf-8") as f:
    f.write("# helpers package\n")

io_code = """def logger(msg):
    print(f"[LOG] {msg}")
"""

with open(os.path.join(helpers_dir, "io.py"), "w", encoding="utf-8") as f:
    f.write(io_code)

crypt_code = """def caesar(text, shift):
    res = []
    for ch in text:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch)-ord('a')-shift)%26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch)-ord('A')-shift)%26 + ord('A')))
        else:
            res.append(ch)
    return ''.join(res)
"""

with open(os.path.join(helpers_dir, "crypt.py"), "w", encoding="utf-8") as f:
    f.write(crypt_code)

# 5. test.py
test_code = """from helpers.io import logger
from helpers.crypt import caesar

logger("Тест логгера")
print(caesar("Hello", 3))
"""

with open(os.path.join(project_dir, "test.py"), "w", encoding="utf-8") as f:
    f.write(test_code)

print("Структура проекта helpers создана. Выполните вручную: python -m venv venv, pip install pandas")
