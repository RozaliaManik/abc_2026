# 16.09.2026
# Rozalia Manik (id postlink=792854)
# Дан целочисленный массив размера N из 10 элементов.
# Преобразовать массив, увеличить каждый его элемент на единицу.

readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1'}
readers_magazines = {'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

both = readers_books & readers_magazines

print("Читатели книг:", readers_books)
print("Читатели газет:", readers_magazines)
print("Читают и книги и газеты:", both)
print("Список:")
for uid in sorted(both):
    print(uid)
