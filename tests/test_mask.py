import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896063612", "Неверная длина номера карты"),
        ("7000a92289606362", "Номер карты должен содержать только цифры"),
        ("", "Неверная длина номера карты"),
    ],
)
def test_get_mask_card_number(value: str, expected: str) -> str:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        ("7365410843013587430", "Неверная длина номера счета"),
        ("7365410843013587430a", "Номер счета должен содержать только цифры"),
        ("", "Неверная длина номера счета"),
    ],
)
def test_get_mask_account(value: str, expected: str) -> str:
    assert get_mask_account(value) == expected
