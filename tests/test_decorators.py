from src.decorators import log


@log()
def test_log_err_console() -> None:
    raise ValueError("Что-то пошло не так!")


@log("log.log")
def test_log_err_file() -> None:
    raise ValueError("Что-то пошло не так!")


@log()
def test_log_console() -> None:
    print("Всё идёт по плану!")


@log("log.log")
def test_log_ile() -> None:
    print("Всё идёт по плану!")
