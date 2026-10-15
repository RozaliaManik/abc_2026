# 18.09.2026
# Rozalia Manik (id postlink=792854)
# Модифицирование программы таким образом, чтобы она выводила
# приветствие "Hello", которое только что записали в файл text.txt

# f = open("text.txt", "w+t")
# f.write("Hello\n")
# # Ваше решение.
# f.close()

import os

file_path = os.path.join(os.path.dirname(__file__), "text.txt")

f = open(file_path, "w+t", encoding="utf-8")
f.write("Hello\n")
f.flush()
f.seek(0)
content = f.read()
f.close()

print(content.strip())
