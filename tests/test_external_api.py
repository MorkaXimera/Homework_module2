import pytest
from src.external_api import get_transactions_list, get_transaction_amount
from unittest.mock import patch
import requests



def test_get_transaction_amount_no_operationAmount():
    assert get_transaction_amount([{}]) == 'Нет информации о сумме транзакции'

def test_get_transaction_amount_rub(transaction_dict_rub):
    assert get_transaction_amount(transaction_dict_rub) == "31957.58"


@patch('requests.request')
def test_get_transaction_amount_usd(mock_request, transaction_dict_usd):
    mock_request.return_value.text = {"result": 100.0}
    mock_request.return_value.status_code = 200
    assert get_transaction_amount (transaction_dict_usd) == 100.0


@patch('requests.request')
def test_get_transaction_amount_usd(mock_request, transaction_dict_usd):
    mock_request.return_value.text = {"result": 100.0}
    mock_request.return_value.status_code = 429
    assert get_transaction_amount (transaction_dict_usd) == 'Не удалось перевести валюту в рубли, ошибка 429'



