def filter_by_state (unfiltred_by_state_list):
    ''' Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует EXECUTED '''
    filtred_by_state_list = []
    for dictionary in unfiltred_by_state_list:
        for key, value in dictionary.items():
            if dictionary['state'] == 'EXECUTED':
                filtred_by_state_list.append (dictionary)
    return (filtred_by_state_list)