import pytest
from typing import Any

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions_coll: list, filtred_by_currency_usd: list) -> None:
    assert list(filter_by_currency(transactions_coll, "USD")) == filtred_by_currency_usd


def test_filter_by_currency_notype(transactions_coll: list, filtred_by_currency_usd: list) -> None:
    assert list(filter_by_currency(transactions_coll)) == filtred_by_currency_usd


def test_filter_by_currency_no_operations(transactions_coll: list) -> None:
    assert list(filter_by_currency(transactions_coll, "EUR")) == []


def test_filter_by_currency_no_list() -> None:
    transactions: list[Any] = []
    assert list(filter_by_currency(transactions)) == []


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "Перевод организации",
        ),
        (
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
            "Перевод с карты на карту",
        ),
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            "Перевод организации",
        ),
    ],
)
def test_transaction_description(value: list, expected: str) -> None:
    assert next(transaction_descriptions(value)) == expected


def test_transaction_descriptions(transactions_coll: list, description_call: list) -> None:
    assert list(transaction_descriptions(transactions_coll)) == description_call


def test_transaction_descriptions_usd(filtred_by_currency_usd: list, description_call_usd: list) -> None:
    assert list(transaction_descriptions(filtred_by_currency_usd)) == description_call_usd


def test_transaction_descriptions_no_list() -> None:
    transactions: list = []
    assert list(transaction_descriptions(transactions)) == []


def test_card_number_generator() -> None:
    generator = card_number_generator()
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"


def test_card_number_generator_max() -> None:
    generator = card_number_generator(9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"
