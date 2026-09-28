# 09.09.2026
# Rozalia Manik (id postlink=792854)
# Наибольшее из чисел

# Задаем три числа (можете менять их для проверки)
x = 77
y = 9
z = 130

# Логика поиска наибольшего числа
if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

# Выводим ответ
print(f"Наибольшее число {largest}")
