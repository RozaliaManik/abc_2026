# 11.10.2026
# Rozalia Manik (id postlink=792854)
# Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу. Она по-русски звучит: «Должен существовать один — и, желательно, только один — очевидный способ сделать это».
 
ciphertext = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

def caesar_decrypt(text, shift):
    res = []
    for ch in text:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
        else:
            res.append(ch)
    return ''.join(res)

print("Попытки расшифровки:")
# Дописываем полный цикл от 1 до 25
for s in range(1, 26):
    print(f"Сдвиг {s}: {caesar_decrypt(ciphertext, s)}")

