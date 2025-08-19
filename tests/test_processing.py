from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(processing_coll: list, filtred_executed: list) -> list:
    assert filter_by_state(processing_coll) == filtred_executed


def test_filter_by_state_canceled(processing_coll: list, filtred_canceled: list) -> list:
    assert filter_by_state(processing_coll, state="CANCELED") == filtred_canceled


def test_filter_by_state_empty() -> list | str:
    assert filter_by_state("") == "Пустой список"


def test_filter_by_state_unknown(processing_coll: list) -> str:
    assert filter_by_state(processing_coll, state="UNKNOWN") == "Список не содержит указанных данных"


def test_sort_by_date_reverse(processing_coll: list, sorted_by_date_reverse: list) -> list:
    assert sort_by_date(processing_coll) == sorted_by_date_reverse


def test_sort_by_date(processing_coll: list, sorted_by_date: list) -> list:
    assert sort_by_date(processing_coll, reverse=False) == sorted_by_date


def test_sort_by_date_same_date(processing_coll_same_date: list, sorted_by_date_same_date: list) -> list:
    assert sort_by_date(processing_coll_same_date) == sorted_by_date_same_date


def test_sort_by_date_incorrect_date(processing_coll_incorrect_date: list) -> str:
    assert sort_by_date(processing_coll_incorrect_date) == "Ошибка ввода даты"
