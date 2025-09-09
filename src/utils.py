import json
import requests


def json_read(path):
    with open(path, encoding='UTF-8') as f:
        json_information = json.load(f)
    return(json_information)



