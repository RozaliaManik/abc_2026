# 18.09.2026
# Rozalia Manik (id postlink=792854)
# Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки

# Содержимое файла config_default.txt
# Конфигурация приложения
# app_name    = ?
# version     = ?
# debug       = ?

# Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?

# Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?

# Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?

# Данные для подстановки
# config_values = {
#     'app_name': 'NextGen',
#     'version': '1.0.0',
#     'debug':  True,
#     'db_host': 'localhost',
#     'db_port': 5432,
#     'db_name': 'my_database',
#     'db_user': 'admin',
#     'db_password': 'secret123',
#     'api_key': 'ak_123456789',
#     'api_secret': 'sk_987654321',
#     'base_url': 'https://api.example.com',
#     'log_file': '/var/log/app.log',
#     'data_dir': '/opt/app/data',
#     'temp_dir': '/tmp/app',
#     'max_workers': 10,
#     'timeout': 30,
#     'retry_attempts': 3
# }

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True

# Настройки базы данных
# db_host     =  5432
# .....

import os
import re

config_default_path = os.path.join(os.path.dirname(__file__), "config_default.txt")
config_output_path = os.path.join(os.path.dirname(__file__), "config.txt")

config_default_content = """# Конфигурация приложения.
app_name    = ?
version     = ?
debug       = ?

# Настройки базы данных
db_host     = ?
db_port     = ?
db_name     = ?
db_user     = ?
db_password = ?

# Настройки API
api_key     = ?
api_secret  = ?
base_url    = ?

# Пути
log_file    = ?
data_dir    = ?
temp_dir    = ?
"""

# создать шаблон, если нет
if not os.path.exists(config_default_path):
    with open(config_default_path, "w", encoding="utf-8") as f:
        f.write(config_default_content)

config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

def format_value(v):
    if isinstance(v, str):
        # оставляем как в примере с кавычками
        return f'"{v}"'
    return str(v)

with open(config_default_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

out_lines = []
for line in lines:
    if "=" in line and "?" in line:
        # ключ до =
        key_part = line.split("=")[0].strip()
        key = key_part.split()[-1] if key_part else key_part
        if key in config_values:
            value_str = format_value(config_values[key])
            # сохраняем отступы
            new_line = re.sub(r'\?\s*$', f' {value_str}', line.rstrip("\n"))
            # если ? в середине
            if "?" in new_line:
                new_line = re.sub(r'\?', value_str, new_line)
            out_lines.append(new_line + "\n")
        else:
            out_lines.append(line)
    else:
        out_lines.append(line)

with open(config_output_path, "w", encoding="utf-8") as f:
    f.writelines(out_lines)

print(f"Конфиг создан: {config_output_path}")
