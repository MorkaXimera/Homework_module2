from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize ('value, expected', [
    ('Счет 73654108430135874305', '**4305'),
    ('Visa Platinum 7000792289606361', '7000 79** **** 6361'),
    ('Maestro 7000792289606361', '7000 79** **** 6361'),
    ('Счет', 'Неверная длина номера счета'),
    ('карта 70007922896063611', 'Неверная длина номера карты'),
    ('', 'Данные отсутствуют'),
    ('123456', 'Данные введены неверно'),
] )
def test_mask_account_card(value, expected):
    assert mask_account_card (value) == expected


def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
    assert get_date('') == 'Данные отсутствуют'
    assert get_date('abracadabra') == 'Ошибка ввода даты'



