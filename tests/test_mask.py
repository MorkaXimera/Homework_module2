from src.mask import get_mask_account, get_mask_card_number
import pytest


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

    assert get_mask_card_number('70007922896063612') == 'Неверная длина номера карты'

    assert get_mask_card_number('7000a92289606362') == 'Номер карты должен содержать только цифры'

    assert get_mask_card_number('') == 'Неверная длина номера карты'

def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'

    assert get_mask_account('7365410843013587430') == 'Неверная длина номера счета'

    assert get_mask_account('7365410843013587430a') == 'Номер счета должен содержать только цифры'

    assert get_mask_account('') == 'Неверная длина номера счета'
