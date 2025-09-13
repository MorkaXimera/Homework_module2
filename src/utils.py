import json
from typing import Any


def json_read(path: Any = "no.json") -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    """
    correct_path = str(path)
    try:
        with open(correct_path, encoding="UTF-8") as f:
            json_information = json.load(f)
            return json_information
    except FileNotFoundError:
        return "Невозможно открыть файл"
