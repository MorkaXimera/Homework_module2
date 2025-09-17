from typing import Any
from unittest.mock import patch

from src.external_api import get_transaction_amount


def test_get_transaction_amount_no_operationAmount() -> None:
    assert get_transaction_amount([{}]) == "Нет информации о сумме транзакции"


def test_get_transaction_amount_rub(transaction_dict_rub: list) -> None:
    assert get_transaction_amount(transaction_dict_rub) == 31957.58


@patch("requests.request")
def test_get_transaction_amount_usd(mock_request: Any, transaction_dict_usd: list) -> None:
    mock_request.return_value.text = {"result": 100.0}
    mock_request.return_value.status_code = 200
    assert get_transaction_amount(transaction_dict_usd) == 100.0


@patch("requests.request")
def test_get_transaction_amount_invalid_status_code(mock_request: Any, transaction_dict_usd: list) -> None:
    mock_request.return_value.text = {"result": 100.0}
    mock_request.return_value.status_code = 429
    assert get_transaction_amount(transaction_dict_usd) == "Не удалось перевести валюту в рубли, ошибка 429"
