from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions_coll: list, filtred_by_currency_usd: list) -> list:
    assert list(filter_by_currency(transactions_coll, "USD")) == filtred_by_currency_usd


def test_filter_by_currency_notype(transactions_coll: list, filtred_by_currency_usd: list) -> list:
    assert list(filter_by_currency(transactions_coll)) == filtred_by_currency_usd


def test_filter_by_currency_no_operations(transactions_coll: list) -> list:
    assert list(filter_by_currency(transactions_coll, "EUR")) == []


def test_filter_by_currency_no_list() -> list:
    transactions = []
    assert list(filter_by_currency(transactions)) == []


def test_transaction_descriptions(transactions_coll: list, description_call: list) -> list:
    assert list(transaction_descriptions(transactions_coll)) == description_call


def test_transaction_descriptions_usd(filtred_by_currency_usd: list, description_call_usd: list) -> list:
    assert list(transaction_descriptions(filtred_by_currency_usd)) == description_call_usd


def test_transaction_descriptions_no_list():
    transactions = []
    assert list(transaction_descriptions(transactions)) == []


def test_card_number_generator() ->str:
    generator = card_number_generator()
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"


def test_card_number_generator_max() -> str:
    generator = card_number_generator(9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"
