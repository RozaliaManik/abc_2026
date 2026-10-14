# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        rows = [line.strip() for line in f if line.strip()]
    # списковое включение для парсинга строк
    matrix = [[int(x) for x in row.split()] for row in rows]
    # проверка одинаковой длины строк без циклов
    lengths = [len(r) for r in matrix]
    if len(set(lengths)) != 1:
        return False
    return matrix

# пример использования
if __name__ == "__main__":
    import os
    test_path = os.path.join(os.path.dirname(__file__), "matrix.txt")
    # создаем тестовый файл если нет
    if not os.path.exists(test_path):
        with open(test_path, "w", encoding="utf-8") as f:
            f.write("11 12 13 14 15 16\n21 22 23 24 25 26\n31 32 33 34 35 36\n")
    print(load_matrix(test_path))
