# 22.09.2026
# Rozalia Manik (id postlink=792854)
#  Добавление во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Главная страница"

@app.route("/about")
def about():
    return "О компании"

@app.route("/contacts")
def contacts():
    return "Контакты"

@app.route("/posts")
def posts():
    return "Список постов"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
