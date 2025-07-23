from mask import get_mask_account, get_mask_card_number


def mask_account_card(discription: str) -> str:
    """Функция возвращает маску номера счета или карты"""
    insert_data = discription.split(" ")
    if insert_data[0] == "Счет":
        masked_account = get_mask_account(insert_data[-1])
    else:
        masked_account = get_mask_card_number(insert_data[-1])

    return masked_account


def get_date(date_str: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    only_date_str = date_str[:10]
    only_date_list = only_date_str.split("-")
    only_date_list.reverse()
    only_date = ".".join(only_date_list)
    return only_date
