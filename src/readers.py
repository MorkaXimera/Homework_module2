import pandas as pd


def csv_reader(csv_file_path = 'no.csv') -> list:
    '''
    Функция позволяет прочесть транзакции из файла в формате .csv и возвращает список словарей
    '''
    try:
        transaction_df = pd.read_csv(csv_file_path, sep=';')
        transaction_list = transaction_df.to_dict(orient='records')
        return transaction_list
    except FileNotFoundError:
        return []


def xlsx_reader(excel_file_path = 'no.xlsx') -> list:
    '''
    Функция позволяет прочесть транзакции из файла в формате .xlsx и возвращает список словарей
    '''
    try:
        transaction_df = pd.read_excel(excel_file_path)
        transaction_list = transaction_df.to_dict(orient='records')
        return transaction_list
    except FileNotFoundError:
        return []


print(xlsx_reader('C:/Users/morka/PycharmProjects/files_for_homework_2/transactions_excel.xlsx'))