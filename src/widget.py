from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(discription: str) -> str:
    """
    Функция возвращает маску номера счета или карты
    """
    if len(discription) != 0:
        insert_data = discription.split(" ")
        if insert_data[0].isalpha():
            if insert_data[0] == "Счет":
                masked_account = get_mask_account(insert_data[-1])
            else:
                masked_account = get_mask_card_number(insert_data[-1])
            return masked_account
        else:
            return ('Данные введены неверно')
    else:
        return ('Данные отсутствуют')


def get_date(date_str: str) -> str:
    """
    Функция возвращает дату в формате ДД.ММ.ГГГГ
    """
    if len(date_str) != 0:
        only_date_str = date_str[:10]
        if '-' in only_date_str:
            only_date_list = only_date_str.split("-")
            only_date_list.reverse()
            only_date = ".".join(only_date_list)
            return only_date
        else:
            return ('Ошибка ввода даты')
    else:
        return ('Данные отсутствуют')
