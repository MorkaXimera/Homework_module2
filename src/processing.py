from src.widget import get_date


def filter_by_state(unfiltred_list: list, state='EXECUTED') -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению
    """
    if len(unfiltred_list) != 0:
        filtred_list = []
        for dictionary in unfiltred_list:
            if dictionary["state"] == state:
                filtred_list.append(dictionary)
        if len(filtred_list) != 0:
            return filtred_list
        else:
            return ('Список не содержит указанных данных')
    else:
        return ('Пустой список')


def sort_by_date(unsorted_list: list, reverse=True) -> list:
    """
    Функция возвращает новый список, отсортированный по дате
    """
    for dictionary in unsorted_list:
        new_value = get_date(dictionary["date"])
        if new_value == 'Ошибка ввода даты' or new_value == 'Данные отсутствуют':
            return ('Ошибка ввода даты')
        else:
            dictionary["date_changed"] = new_value
    sorted_by_date_list = sorted(unsorted_list, key=lambda x: x["date"], reverse=reverse)
    for dictionary in sorted_by_date_list:
        del dictionary["date_changed"]
    return sorted_by_date_list
