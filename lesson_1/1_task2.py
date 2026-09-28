# 09.09.2026
# Rozalia Manik (id postlink=792854)
# Преобразование переменных

# 1. Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"

age_num = int(age)
print(f"age в число: {age_num} (тип: {type(age_num)})")

# Переменную foo пробуем преобразовать безопасно, чтобы код не упал из-за букв
try:
    foo_num = int(foo)
except ValueError:
    print("foo нельзя преобразовать в число, так как строка содержит буквы 'abc'")


# 2. Преобразуйте переменную age в Boolean
age_str = "123abc"
age_bool = bool(age_str)
print(f"age_str в Boolean: {age_bool}") # Любая непустая строка — это True


# 3. Преобразуйте переменную flag в Boolean
flag = 1
flag_bool = bool(flag)
print(f"flag в Boolean: {flag_bool}") # Число 1 — это True


# 4. Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

print(f"str_one в Boolean: {bool(str_one)}") # Непустая строка -> True
print(f"str_two в Boolean: {bool(str_two)}") # Пустая строка -> False


# 5. Преобразуйте значение 0 и 1 в Boolean
zero_bool = bool(0)
one_bool = bool(1)
print(f"0 в Boolean: {zero_bool}") # 0 -> False
print(f"1 в Boolean: {one_bool}") # 1 -> True


# 6. Преобразуйте False в строку
false_val = False
false_str = str(false_val)
print(f"False в строку: '{false_str}' (тип: {type(false_str)})")