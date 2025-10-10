import pandas as pd

from typing import Any


def csv_reader(csv_file_path : str ="no.csv") -> list[Any]:
    """
    Функция позволяет прочесть транзакции из файла в формате .csv и возвращает список словарей
    """
    correct_file_path = str(csv_file_path)
    try:
        transaction_df = pd.read_csv(correct_file_path, sep=";")
        transaction_list = transaction_df.to_dict(orient="records")
        return transaction_list
    except FileNotFoundError:
        return []


def xlsx_reader(excel_file_path : str ="no.xlsx") -> list[Any]:
    """
    Функция позволяет прочесть транзакции из файла в формате .xlsx и возвращает список словарей
    """
    correct_file_path = str(excel_file_path)
    try:
        transaction_df = pd.read_excel(correct_file_path)
        transaction_list = transaction_df.to_dict(orient="records")
        return transaction_list
    except FileNotFoundError:
        return []
