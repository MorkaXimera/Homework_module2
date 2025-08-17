def filter_by_currency(transactions, type):
    for transaction in transactions:
        if transaction['operationAmount']['currency']['name'] == type:
          yield transaction


def transaction_descriptions(transactions):
    while True:
      for transaction in transactions:
          yield transaction['description']


def card_number_generator(start, stop):
    zero_number = '0000 0000 0000 0000'
    new_card_list = list(zero_number)
    for i in range(start, stop):
      new_chars = list(str(i))
      new_card_list = new_card_list[:-len(new_chars)]
      new_card_list = new_card_list + new_chars
      new_card_number = ''.join(new_card_list)
      yield new_card_number

