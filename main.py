import re

from src.generators import get_currency_transactions, get_currency_transactions_json
from src.mask import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.readers import csv_reader, xlsx_reader
from src.search_and_count import process_bank_search
from src.utils import json_read
from src.widget import get_date


def use_app() -> None:
    """
    Функция основной логики проекта
    """
    # Программа приветствует пользователя
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
        "\nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
    )

    # Выбор типа файла
    while True:
        menu_number = input("Введите номер пункта: ")
        if menu_number in ("1", "2", "3"):
            if menu_number == "1":
                print("Для обработки выбран JSON-файл")
            elif menu_number == "2":
                print("Для обработки выбран CSV-файл")
            elif menu_number == "3":
                print("Для обработки выбран XLSX-файл")
            break
        else:
            print("Неверный ввод данных")

    # Чтение выбранного файла
    if menu_number == "1":
        user_transactions = list(json_read(path="C:/Users/morka/PycharmProjects/Homework_2/data/operations.json"))
    elif menu_number == "2":
        user_transactions = csv_reader(
            csv_file_path="C:/Users/morka/PycharmProjects/files_for_homework_2/transactions.csv"
        )
    else:
        user_transactions = xlsx_reader(
            excel_file_path="C:/Users/morka/PycharmProjects/files_for_homework_2/transactions_excel.xlsx"
        )

    # Выбор статуса операции
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию. "
        "\nДоступные для фильтровки статусы: EXECUTED(1), CANCELED(2), PENDING(3)"
    )
    while True:
        user_status_number = str(input("Введите статус: "))
        if user_status_number in ("1", "2", "3"):
            if user_status_number == "1":
                user_status_name = "EXECUTED"
                print('Операции отфильтрованы по статусу "EXECUTED"')
            elif user_status_number == "2":
                user_status_name = "CANCELED"
                print('Операции отфильтрованы по статусу "CANCELED"')
            else:
                user_status_name = "PENDING"
                print('Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f'Статус операции "{user_status_number}" недоступен')

    # Фильтрация по статусу операции
    filter_by_state_list = filter_by_state(user_transactions, user_status_name)

    # Уточнение выборки
    print("Отсортировать операции по дате? Да/Нет")
    while True:
        user_data = input("Введите ответ: ")
        user_data_up = user_data.upper()
        if user_data_up in ("ДА", "НЕТ"):
            break
        else:
            print("Ошибка ввода")

    # Сортировка по дате
    if user_data_up == "ДА":
        print("Отсортировать по возрастанию(1) или по убыванию(2)?")
        while True:
            user_sort = input("Введите ответ: ")
            if user_sort in ("1", "2"):
                if user_sort == "1":
                    filtred_by_state_and_date_list = sort_by_date(filter_by_state_list, reverse=False)
                elif user_sort == "2":
                    filtred_by_state_and_date_list = sort_by_date(filter_by_state_list)
                break
            else:
                print("Ошибка ввода")
    else:
        filtred_by_state_and_date_list = filter_by_state_list

    # Сортировка по валюте
    print("Выводить только рублевые транзакции? Да/Нет")
    while True:
        user_rub = input("Введите ответ: ")
        user_rub_up = user_rub.upper()
        if user_rub_up in ("ДА", "НЕТ"):
            break
        else:
            print("Ошибка ввода")

    if menu_number == "2" or menu_number == "3":
        if user_rub_up == "ДА":
            filtred_by_currency_list = get_currency_transactions(filtred_by_state_and_date_list)
        elif user_rub_up == "НЕТ":
            filtred_by_currency_list = filtred_by_state_and_date_list
    else:
        filtred_by_currency_list = get_currency_transactions_json(filtred_by_state_and_date_list)

    # Сортировка по слову в описании
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        user_filter = input("Введите ответ: ")
        user_filter_up = user_filter.upper()
        if user_filter_up in ("ДА", "НЕТ"):
            if user_filter_up == "ДА":
                search = input("Введите слово для поиска: ")
                final_transactions_list = process_bank_search(filtred_by_currency_list, search)
            else:
                final_transactions_list = filtred_by_currency_list
            break
        else:
            print("Ошибка ввода")

    # Вывод ответа
    print("Распечатываю итоговый список транзакций...")
    if len(final_transactions_list) > 0:
        print(f"Всего банковских операций в выборке: {len(final_transactions_list)}")
        for transaction in final_transactions_list:
            print(f"{get_date(transaction['date'])} {transaction['description']}")
            if transaction["description"] == "Открытие вклада":
                account = transaction["to"][5:]
                print(f"{get_mask_account(account)}")
            if transaction["description"] == "Перевод с карты на карту":
                card_out_str = transaction["from"]
                card_in_str = transaction["to"]
                card_out_name = "".join(re.findall("\\D+", card_out_str))
                card_in_name = "".join(re.findall("\\D+", card_in_str))
                card_out_number = "".join(re.findall("\\d+", card_out_str))
                card_in_number = "".join(re.findall("\\d+", card_in_str))
                print(
                    f"{card_out_name} {get_mask_card_number(card_out_number)} -> "
                    f"{card_in_name} {get_mask_card_number(card_in_number)}"
                )
            if transaction["description"] == "Перевод организации":
                card_out_str = transaction["from"]
                account_in = transaction["to"][5:]
                card_out_name = "".join(re.findall("\\D+", card_out_str))
                card_out_number = "".join(re.findall("\\d+", card_out_str))
                if card_out_name == "Счет ":
                    print(f"Счет {get_mask_account(transaction['from'][5:])} -> Счет {get_mask_account(account_in)}")
                else:
                    print(
                        f"{card_out_name} {get_mask_card_number(card_out_number)} -> "
                        f"Счет {get_mask_account(account_in)}"
                    )
            if transaction["description"] == "Перевод со счета на счет":
                print(
                    f"Счет {get_mask_account(transaction['from'][5:])} -> "
                    f"Счет {get_mask_account(transaction['to'][5:])}"
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации")


use_app()
