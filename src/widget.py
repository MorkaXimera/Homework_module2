from mask import get_mask_account, get_mask_card_number

def mask_account_card (discription):
    '''Функция возвращает маску номера счета или карты'''
    insert_data = discription.split(' ')
    if insert_data[0] == 'Счет':
        masked_account = get_mask_account (insert_data[-1])
    else:
        masked_account = get_mask_card_number (insert_data[-1])

    return (masked_account)

print (mask_account_card('Счет 64686473678894779589'))