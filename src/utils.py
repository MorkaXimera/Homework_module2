import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/morka/PycharmProjects/Homework_2/logs/utils.log", mode="w", encoding="UTF-8"
)
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)


def json_read(path: Any = "no.json") -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    """
    correct_path = str(path)

    logger.debug(f"Загрузка данных из файла {correct_path}")

    try:
        logger.debug("Открытие файла")
        with open(correct_path, encoding="UTF-8") as f:
            logger.info("Файл открыт. Загрузка данных")
            json_information = json.load(f)
            logger.info("Данные файла успешно загружены")
            return json_information
    except FileNotFoundError:
        logger.error(f"Файл не найден по пути {correct_path}")
        return []


print(json_read("C:/Users/morka/PycharmProjects/Homework_2/data/operations.json"))
