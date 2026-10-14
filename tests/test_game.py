import pytest

# Простая функция для тестирования логики подстановки букв
def check_letter_logic(secret, mask, letter):
    new_mask = list(mask)
    for ind, val in enumerate(secret):
        if val.upper() == letter.upper():
            new_mask[ind] = val
    return "".join(new_mask)

@pytest.mark.smoke
def test_correct_letter():
    """Тест: угадывание правильной буквы"""
    assert check_letter_logic("ГИТАРА", "******", "Т") == "**Т***"

def test_wrong_letter():
    """Тест: ввод неверной буквы"""
    assert check_letter_logic("ГИТАРА", "******", "Ю") == "******"

@pytest.mark.parametrize("secret, mask, letter, expected_mask", [
    ("ФЛАСК", "-----", "А", "--А--"),
    ("МАНГО", "-----", "М", "М----"),
    ("ДОКЕР", "-----", "Р", "----Р"),
])
def test_parametrized_letters(secret, mask, letter, expected_mask):
    """Параметризованный тест для разных слов"""
    assert check_letter_logic(secret, mask, letter) == expected_mask
