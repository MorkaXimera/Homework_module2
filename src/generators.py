from typing import Any, Dict, Generator


def filter_by_currency(transactions: list, type: str = "USD") -> Generator[Dict[str, Any], None, None]:
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
        new_card_number_spaced = " ".join(new_card_number[i:i + 4] for i in range(0, len(new_card_number), 4))
        yield new_card_number_spaced
