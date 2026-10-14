#from app import app

#if __name__ == '__main__':
#    app.run(debug=True)


from app import app

if __name__ == '__main__':
    # Переводим игру на порт 5001, чтобы обойти системную ошибку доступа!
    app.run(debug=True, port=5001)

