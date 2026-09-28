# 16.09.2026
# Rozalia Manik (id postlink=792854)
# Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более!
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]

# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один

mass = [1,2,17,54,30,89,2,1,6,2]

from collections import defaultdict

positions = defaultdict(list)
for i, v in enumerate(mass):
    positions[v].append(i)

for v in sorted(positions):
    idxs = positions[v]
    if len(idxs) < 2:
        print(f"Для числа {v} нет минимального расстояния т.к элемент в массиве один.")
        continue
    min_dist = None
    best_pair = None
    for i in range(len(idxs)-1):
        d = idxs[i+1] - idxs[i]
        if min_dist is None or d < min_dist:
            min_dist = d
            best_pair = (idxs[i], idxs[i+1])
    print(f"Для числа {v} минимальное расстояние в массиве по индексам: {best_pair[0]} и {best_pair[1]}")
