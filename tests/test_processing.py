from src.processing import filter_by_state, sort_by_date

import pytest


def test_filter_by_state_executed(processing_coll, filtred_executed):
    assert filter_by_state(processing_coll) == filtred_executed



def test_filter_by_state_canceled(processing_coll, filtred_canceled):
    assert filter_by_state(processing_coll, state='CANCELED') == filtred_canceled


def test_filter_by_state_empty():
    assert filter_by_state ('') == 'Пустой список'


def test_filter_by_state_unknown(processing_coll):
    assert filter_by_state(processing_coll, state='UNKNOWN') == 'Список не содержит указанных данных'



def test_sort_by_date_reverse(processing_coll, sorted_by_date_reverse):
    assert sort_by_date(processing_coll) == sorted_by_date_reverse


def test_sort_by_date(processing_coll, sorted_by_date):
    assert sort_by_date(processing_coll, reverse=False) == sorted_by_date


def test_sort_by_date_same_date(processing_coll_same_date, sorted_by_date_same_date):
    assert sort_by_date(processing_coll_same_date) == sorted_by_date_same_date


def test_sort_by_date_incorrect_date(processing_coll_incorrect_date):
    assert sort_by_date (processing_coll_incorrect_date) == 'Ошибка ввода даты'