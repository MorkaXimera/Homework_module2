from src.readers import xlsx_reader, csv_reader
import pytest
from unittest.mock import patch, Mock
import pandas as pd


def test_csv_reader_no_file():
    assert csv_reader() == []


def test_csv_reader_invalid_file():
    assert csv_reader("C:/Users/morka/PycharmProjects/Homework_2/tests/nofile.csv") == []


def test_csv_reader_not_path():
    assert csv_reader(123) == []


@patch('pandas.read_csv')
def test_csv_reader(mock_read_csv):
    mock_data = ([{'id': 4137938.0,
                                 'state': 'EXECUTED',
                                 'date': '2023-01-04T13:13:34Z',
                                 'amount': 15560.0,
                                 'currency_name': 'Real',
                                 'currency_code': 'BRL',
                                 'from': 'Discover 5243103907617572',
                                 'to': 'Счет 38164279390569873521',
                                 'description': 'Открытие вклада'}])
    mock_df = pd.DataFrame(mock_data)
    mock_read_csv.return_value = mock_df
    assert csv_reader("my_path.csv") == [{'id': 4137938.0,
                                 'state': 'EXECUTED',
                                 'date': '2023-01-04T13:13:34Z',
                                 'amount': 15560.0,
                                 'currency_name': 'Real',
                                 'currency_code': 'BRL',
                                 'from': 'Discover 5243103907617572',
                                 'to': 'Счет 38164279390569873521',
                                 'description': 'Открытие вклада'}]


def test_xlsx_reader_no_file():
    assert xlsx_reader() == []


def test_xlsx_reader_invalid_file():
    assert xlsx_reader("C:/Users/morka/PycharmProjects/Homework_2/tests/nofile.csv") == []


def test_xlsx_reader_not_path():
    assert xlsx_reader(123) == []


@patch('pandas.read_excel')
def test_xlsx_reader(mock_read_excel):
    mock_data = ([{'id': 4137938.0,
                       'state': 'EXECUTED',
                       'date': '2023-01-04T13:13:34Z',
                       'amount': 15560.0,
                       'currency_name': 'Real',
                       'currency_code': 'BRL',
                       'from': 'Discover 5243103907617572',
                       'to': 'Счет 38164279390569873521',
                       'description': 'Открытие вклада'}])
    mock_df = pd.DataFrame(mock_data)
    mock_read_excel.return_value = mock_df
    assert xlsx_reader("my_path.excel") == [{'id': 4137938.0,
                                                 'state': 'EXECUTED',
                                                 'date': '2023-01-04T13:13:34Z',
                                                 'amount': 15560.0,
                                                 'currency_name': 'Real',
                                                 'currency_code': 'BRL',
                                                 'from': 'Discover 5243103907617572',
                                                 'to': 'Счет 38164279390569873521',
                                                 'description': 'Открытие вклада'}]