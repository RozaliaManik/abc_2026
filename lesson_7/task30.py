# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Напишите лямбду функцию которая возвращает максимальное число
# из 2 переданных чисел

max_two = lambda a, b: a if a > b else b
print("max_two:", max_two(5, 10))

# #todo: Для каждого значения из списка mass получите
# # список проверок(True или False) вхождений значений в диапазон от 1 до 130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
in_range = [1 <= x <= 130 for x in mass]
print("in_range:", in_range)

#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений
list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
odds = list(filter(lambda val: val % 2 != 0, list_))
print("odds:", odds)

#todo: Отсортируйте список по расширению ".mp3"
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
# сначала файлы с .mp3, затем остальные, сохраняем порядок
mp3_files = [f for f in files if f.endswith('.mp3')]
other_files = [f for f in files if not f.endswith('.mp3')]
sorted_files = mp3_files + other_files
print("sorted by .mp3:", sorted_files)
