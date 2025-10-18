from re import search

from src.search_and_count import process_bank_search, process_bank_operations

def test_process_bank_search_right_information(transactions_coll, search = 'Перевод организации'):
	assert process_bank_search (transactions_coll, search) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_process_bank_search_no_search(transactions_coll):
	assert process_bank_search(transactions_coll) == []


def test_process_bank_search_error (transactions_coll, search = 'abc'):
	assert process_bank_search(transactions_coll, search) == []


def test_process_bank_search_no_transactions():
	assert process_bank_search(search='abc') == []


def test_process_bank_operations_right_information(transactions_coll,categories_coll):
	assert process_bank_operations(transactions_coll,categories_coll) == {'Перевод организации':2, 'Перевод со счета на счет': 2, "Перевод с карты на карту": 1}


def test_process_bank_operations_no_data(categories_coll):
	assert process_bank_operations(categories = categories_coll) == {}


def test_process_bank_operations_no_cat(transactions_coll):
	assert process_bank_operations(data = transactions_coll) == {}
