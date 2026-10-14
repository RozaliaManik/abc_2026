# 11.09.2026
# Rozalia Manik (id postlink=792854)
# Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = float(input("Введите любое число: "))
B = float(input("Введите любое число: "))
C = float(input("Введите любое число: "))

AC = abs(A - C)
BC = abs(B - C)

print(AC)
print(BC)
print(AC + BC)