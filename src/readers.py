import pandas as pd


def csv_reader(csv_file_path) -> list:
    '''
    Функция позволяет прочесть транзакции из файла в формате .csv и возвращает список словарей
    '''
    transaction_df = pd.read_csv(csv_file_path, sep=';')
    transaction_list = transaction_df.to_dict(orient='records')
    return transaction_list


def xlsx_reader(excel_file_path) -> list:
    '''
    Функция позволяет прочесть транзакции из файла в формате .xlsx и возвращает список словарей
    '''
    transaction_df = pd.read_excel(excel_file_path)
    transaction_list = transaction_df.to_dict(orient='records')
    return transaction_list
