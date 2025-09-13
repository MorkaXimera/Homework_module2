import requests
from src.utils import json_read
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_KEY")
HEADERS = {"apikey": API_TOKEN}


def get_transactions_list(transactions_path):
    transactions_list = json_read(transactions_path)
    return (transactions_list)


def get_transaction_amount(transactions_list):
    for dict in transactions_list:
        if 'operationAmount' in dict:
            if dict['operationAmount']['currency']['code'] == 'RUB':
                return(dict['operationAmount']['amount'])
            elif dict['operationAmount']['currency']['code'] == 'EUR' or 'USD':
                url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={dict["operationAmount"]["currency"]["code"]}USD&amount=5{dict["operationAmount"]["amount"]}'
                payload = []
                headers = HEADERS
                response = requests.request("GET", url, headers=headers, data=payload)
                status_code = response.status_code
                result = response.text
                if status_code == 200:
                    return (result['result'])
                else:
                    return(f'Не удалось перевести валюту в рубли, ошибка {status_code}')

        else:
            return('Нет информации о сумме транзакции')

transactions_list = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]
print (get_transactions_list('C:/Users/morka/PycharmProjects/Homework_2/data/vvv.json'))
print (get_transaction_amount([{}]))