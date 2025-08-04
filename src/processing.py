from src.widget import get_date


def filter_by_state(unfiltred_by_state_list: list) -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует EXECUTED"""
    filtred_by_state_list = []
    for dictionary in unfiltred_by_state_list:
        for key, value in dictionary.items():
            if dictionary["state"] == "EXECUTED":
                filtred_by_state_list.append(dictionary)
    return filtred_by_state_list


def sort_by_date(unsorted_list: list) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    for dictionary in unsorted_list:
        new_value = get_date(dictionary["date"])
        dictionary["date_changed"] = new_value
    sorted_by_date_list = sorted(unsorted_list, key=lambda x: x["date"], reverse=True)
    for dictionary in sorted_by_date_list:
        del dictionary["date_changed"]
    return sorted_by_date_list
