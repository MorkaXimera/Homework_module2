import json
import requests


def json_read(path='no.json'):
    correct_path = str(path)
    try:
        with open(correct_path, encoding='UTF-8') as f:
            json_information = json.load(f)
            return (json_information)
    except FileNotFoundError:
        return ("Невозможно открыть файл")

print(json_read())


