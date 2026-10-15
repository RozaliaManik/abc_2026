# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Числа превратить в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

import re

def numbers_to_letters(text):
    def repl(match):
        nums = match.group().split()
        letters = []
        for n in nums:
            try:
                val = int(n)
                # Если это ноль, просто пропускаем его и ничего не добавляем
                if val == 0:
                    continue
                elif 1 <= val <= 26:
                    letters.append(chr(ord('a') + val - 1))
                else:
                    letters.append(n)
            except ValueError:
                letters.append(n)
        return ''.join(letters)
    
    # заменяем последовательности цифр
    return re.sub(r'\d+(?:\s+\d+)*', repl, text)

if __name__ == "__main__":
    tests = [
        "8 5 12 12 15",
        "8 5 12 12 15 , 0 23 15 18 12 4 !"
    ]
    for t in tests:
        print(t, "=>", numbers_to_letters(t))
