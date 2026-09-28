# 09.09.2026
# Rozalia Manik (id postlink=792854)
# Oбмен значений переменных местами

# todo: Данные две переменные:
age = 36.6
temperature = 25

print(f"До обмена: age = {age}, temperature = {temperature}")

# Меняем значения местами (Магия Python!)
age, temperature = temperature, age

print(f"После обмена: age = {age}, temperature = {temperature}")