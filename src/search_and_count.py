import re
from collections import Counter


def process_bank_search(data:list[dict] = [], search:str = '')->list[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и
    строку поиска, и возвращает список словарей, у которых в описании есть данная строка
    """
    found_transactions = []
    search_str = str(search)
    pattern = (fr'\b{search_str}\b')
    for transaction_dict in data:
        try:
            match_transaction = re.findall(pattern, transaction_dict['description'], flags=re.I)
            if any(match_transaction):
                found_transactions.append(transaction_dict)
            else:
                continue
        except KeyError:
            print ('Описание транзакции отсутствует')

    return (found_transactions)


def process_bank_operations(data:list[dict] = [], categories:list = [])->dict:
    '''
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — названия категорий,
    а значения — количество операций в каждой категории.
    '''
    transaction_description_list = []
    for transaction_dict in data:
        try:
            if transaction_dict['description'] in categories:
                transaction_description_list.append(transaction_dict['description'])
            else:
                continue
        except KeyError:
            print('Описание транзакции отсутствует')
    number_of_categories = dict(Counter(transaction_description_list))
    return (number_of_categories)

def process_bank_search(data:list[dict] = [], search:str = '')->list[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и
    строку поиска, и возвращает список словарей, у которых в описании есть данная строка
    """
    found_transactions = []
    search_str = str(search)
    pattern = (fr'\b{search_str}\b')
    for transaction_dict in data:
        try:
            match_transaction = re.findall(pattern, transaction_dict['description'], flags=re.I)
            if any(match_transaction):
                found_transactions.append(transaction_dict)
            else:
                continue
        except KeyError:
            print ('Описание транзакции отсутствует')

    return (found_transactions)
