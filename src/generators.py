from typing import Any, Dict, Generator


def filter_by_currency(transactions: list | str, type: str = "USD") -> Generator[Dict[str, Any], None, None]:
    """
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == type:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    """
    Функция возвращает описание каждой операции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 1, stop: int = 10000000000000000) -> Generator:
    """
    Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    zero_number = "0000000000000000"
    new_card_list = list(zero_number)
    for i in range(start, stop):
        new_chars = list(str(i))
        new_card_list = new_card_list[: -len(new_chars)]
        new_card_list = new_card_list + new_chars
        new_card_number = "".join(new_card_list)
        new_card_number_spaced = " ".join(new_card_number[i: i + 4] for i in range(0, len(new_card_number), 4))
        yield new_card_number_spaced


def get_currency_transactions(transactions: list, type: str = "RUB") -> list:
    """
    Функция принимает на вход список транзакций и возвращает отфильтрованный по выбранной валюте
    """
    filtred_by_currency_list = []
    for transaction in transactions:
        try:
            if transaction["currency_code"] == type:
                filtred_by_currency_list.append(transaction)
            else:
                continue
        except KeyError:
            continue

    return filtred_by_currency_list


def get_currency_transactions_json(transactions: list, type: str = "RUB") -> list:
    """
    Функция принимает на вход список транзакций из json файла и возвращает отфильтрованный по выбранной валюте
    """
    filtred_by_currency_list = []
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == type:
                filtred_by_currency_list.append(transaction)
            else:
                continue
        except KeyError:
            continue
    return filtred_by_currency_list
