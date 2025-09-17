import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import json_read

load_dotenv()
API_TOKEN = os.getenv("API_KEY")
HEADERS = {"apikey": API_TOKEN}


def get_transactions_list(transactions_path: Any) -> Any:
    """
    Функция считывает информацию о транзакциях из объекта json
    """
    transactions_list = json_read(transactions_path)
    return transactions_list


def get_transaction_amount(transactions_list: list) -> Any:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции
    """
    for dict in transactions_list:
        if "operationAmount" in dict:
            if dict["operationAmount"]["currency"]["code"] == "RUB":
                return float(dict["operationAmount"]["amount"])
            elif dict["operationAmount"]["currency"]["code"] == "EUR" or "USD":
                url = (
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
                    f'{dict["operationAmount"]["currency"]["code"]}&amount={dict["operationAmount"]["amount"]}'
                )
                payload: list = []
                headers = HEADERS
                response = requests.request("GET", url, headers=headers, data=payload)
                status_code = response.status_code
                result = response.text
                if status_code == 200:
                    return float(result["result"])
                else:
                    return f"Не удалось перевести валюту в рубли, ошибка {status_code}"

        else:
            return "Нет информации о сумме транзакции"
