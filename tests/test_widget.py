import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 73654108430135874305", "**4305"),
        ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
        ("Maestro 7000792289606361", "7000 79** **** 6361"),
        ("Счет", "Неверная длина номера счета"),
        ("карта 70007922896063611", "Неверная длина номера карты"),
        ("", "Данные отсутствуют"),
        ("123456", "Данные введены неверно"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> str:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", "Данные отсутствуют"), ("abracadabra", "Ошибка ввода даты")],
)
def test_get_date(value: str, expected: str) -> str:
    assert get_date(value) == expected
