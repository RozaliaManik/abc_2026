# 16.09.2026
# Rozalia Manik (id postlink=792854)
# База данных пользователя.
# Задан массив объектов пользователя

# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного),
# первой букве логина, и заданной группе

# Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

# #Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
# Пользователь: 'Piter' возраст 23 года , группа  "admin"
# Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan',  'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]

print("1. По возрасту")
print("2. По первой букве")
print("3. По группе")
try:
    sort_type = int(input("тип сортировки: "))
except:
    sort_type = 1

criteria = input("Ввидите критерии поиска: ")

result = []

if sort_type == 1:
    try:
        age_limit = int(criteria)
        filtered = [u for u in users if u['age'] > age_limit]
        filtered.sort(key=lambda x: x['age'])
        result = filtered
    except ValueError:
        pass
elif sort_type == 2:
    letter = criteria.strip().lower()
    filtered = [u for u in users if u['login'].lower().startswith(letter)]
    filtered.sort(key=lambda x: x['login'].lower())
    result = filtered
elif sort_type == 3:
    group_name = criteria.strip().lower()
    filtered = [u for u in users if u['group'].lower() == group_name]
    filtered.sort(key=lambda x: x['age'])
    result = filtered

if not result:
    print("Результатов не найдено")
else:
    for u in result:
        print(f"#Пользователь: '{u['login']}' возраст {u['age']} года , группа  \"{u['group']}\"")
