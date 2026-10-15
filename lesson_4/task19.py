# 18.09.2026
# Rozalia Manik (id postlink=792854)
# Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
#              "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
#              "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
# .....

import csv
import os

algoritm = [
    "C4.5",
    "k - means",
    "Метод опорных векторов",
    "Apriori",
    "EM",
    "PageRank",
    "AdaBoost",
    "kNN",
    "Наивный байесовский классификатор",
    "CART"
]

output_dir = os.path.dirname(__file__)
csv_path = os.path.join(output_dir, "algoritm.csv")

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "значение"])
    for i, val in enumerate(algoritm, start=1):
        writer.writerow([f"{i})", val])

print(f"CSV создан: {csv_path}")
