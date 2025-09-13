import requests
from utils import json_read
import os
from dotenv import load_dotenv
load_dotenv('.env')

def transaction_amount():
    path = r'C:\Users\morka\PycharmProjects\Homework_2\data\operations.json'
    transactions_list = json_read(path)
    for dict in transactions_list:
        if 'operationAmount' in dict:
            if dict['operationAmount']['currency']['code'] == 'RUB':
                print(dict['operationAmount']['amount'])
            elif dict['operationAmount']['currency']['code'] == 'EUR' or 'USD':
                url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
                api_key = os.getenv('API_KEY')
                payload = {f'{{"to":"RUB", "from": {dict["operationAmount"]["currency"]["code"]}, "amount":{dict["operationAmount"]["amount"]}}}'}
                headers = {
                    "apikey": f'{api_key}'
                }
                response = requests.request("GET", url, headers=headers, data = payload)
                status_code = response.status_code
                result = response.text
                if status_code == 200:
                    print(result['result'])
                else:
                    print('Не удалось перевести валюту в рубли')
                    print(status_code)
        else:
            print('Нет информации о сумме транзакции')
