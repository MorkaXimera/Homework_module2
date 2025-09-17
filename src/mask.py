import logging
from dbm import error

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/morka/PycharmProjects/Homework_2/logs/mask.log", mode="w", encoding="UTF-8"
)
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция возвращает маску номера карты
    """
    logger.info("Чтение номера карты")
    logger.debug("Проверка длины номера карты")
    if len(str(card_number)) == 16:
        logger.debug("Проверка, что все символы в номере карты - цифры")
        if str(card_number).isdigit():
            logger.debug("Создание маски номера карты")
            card_number_list = list(str(card_number))
            new_char = "*"
            for i in range(6, 12):
                card_number_list[i] = new_char
            mask_number_str = "".join(card_number_list)
            mask_number = ""
            for i in range(len(mask_number_str) - 1, -1, -1):
                mask_number = card_number_list[i] + mask_number
                if (len(mask_number_str) - i) % 4 == 0 and i != 0:
                    mask_number = " " + mask_number
                else:
                    error
            logger.info("Маска номера карты успешно создана")
            return mask_number
        else:
            logger.error("В номере карты содержатся не только цифры")
            return "Номер карты должен содержать только цифры"
    else:
        logger.error("Неверная длина номера карты")
        return "Неверная длина номера карты"


def get_mask_account(account: str) -> str:
    """
    Функция возвращает маску номера счёта
    """
    logger.info("Чтение номера счета")
    logger.debug("Проверка длины номера счета")
    if len(str(account)) == 20:
        logger.debug("Проверка, что все символы в номере счета - цифры")
        if str(account).isdigit():
            logger.debug("Создание маски номера счета")
            account_list = list(str(account))
            mask_list = account_list[-6:]
            mask_list[0] = "*"
            mask_list[1] = "*"
            mask_str = "".join(mask_list)
            logger.info("Маска номера счета успешно создана")
            return mask_str
        else:
            logger.error("В номере счета содержатся не только цифры")
            return "Номер счета должен содержать только цифры"
    else:
        logger.error("Неверная длина номера счета")
        return "Неверная длина номера счета"
