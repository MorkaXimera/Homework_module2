def get_mask_card_number(card_number: str) -> str:
    """
    Функция возвращает маску номера карты
    """
    card_number_list = list(str(card_number))
    new_char = "*"
    for i in range(6, 12):
        card_number_list[i] = new_char
    mask_number_str = "".join(card_number_list)
    mask_number = ""
    for i in range(len(mask_number_str) - 1, -1, -1):
        mask_number = card_number_list[i] + mask_number
        if (len(mask_number_str) - i) % 4 == 0 and i != 0:
            mask_number = " " + mask_number
    return mask_number


def get_mask_account(account: str) -> str:
    """
    Функция возвращает маску номера счёта
    """
    account_list = list(str(account))
    mask_list = account_list[-6:]
    mask_list[0] = "*"
    mask_list[1] = "*"
    mask_str = "".join(mask_list)
    return mask_str
