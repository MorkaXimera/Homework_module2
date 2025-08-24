import datetime
from typing import Any


def log(filename: Any = None) -> Any:
    """
    Декоратор, который логирует начало и конец выполнения функции,
    ее результаты или возникшие ошибки
    """

    def log_decorator(func: Any) -> Any:
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            start_time = 0
            try:
                start_time = f"{func.__name__} начала работу {datetime.datetime.now()}"
                result = func(*args, **kwargs)
                end_time = f"{func.__name__} закончила работу {datetime.datetime.now()}"
                result_message = f"{func.__name__} статус: ок"
                if filename is None:
                    print(f"{start_time} \n{end_time}\n{result_message}\n")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{start_time} \n{end_time}\n{result_message}\n")
            except Exception as e:
                end_time = f"{func.__name__} закончила работу {datetime.datetime.now()}"
                result_message = (
                    f"{func.__name__} завершила программу с ошибкой: {type(e).__name__}, "
                    f"входные параметры {args}, {kwargs}"
                )
                if filename is None:
                    print(f"{start_time} \n{end_time}\n{result_message}\n")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{start_time} \n{end_time}\n{result_message}\n")
                return e

        return wrapper

    return log_decorator
