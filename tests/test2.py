from src.widget import get_date

def sort_by_date (unsorted_list, reverse=True):
    for dictionary in unsorted_list:
        new_value = get_date (dictionary['date'])
        dictionary['date_changed'] = new_value
    sorted_by_date_list = sorted(unsorted_list, key=lambda x: x['date'], reverse=True)
    for dictionary in sorted_by_date_list:
        del dictionary ['date_changed']
    return (sorted_by_date_list)

print (sort_by_date ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))