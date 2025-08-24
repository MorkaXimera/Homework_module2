from src.decorators import log
from typing import Any


@log()
def test_log_err_console() -> None:
    assert ValueError("Что-то пошло не так!")


@log("log.log")
def test_log_err_file() -> None:
    assert ValueError("Что-то пошло не так!")


@log()
def test_log_console() -> None:
    print("Всё идёт по плану!")


@log("log.log")
def test_log_file() -> None:
    print("Всё идёт по плану!")


@log()
def example_func() -> None:
    print("Всё идёт по плану!")


def test_log_console_capsys(capsys: Any) -> None:
    example_func()
    captured = capsys.readouterr()
    assert "начала работу", "закончила работу" "статус: ок" in captured.out


@log()
def example_err_func() -> int:
    return 10 // 0


def test_log_console_err_capsys(capsys: Any) -> None:
    example_err_func()
    captured = capsys.readouterr()
    assert "начала работу" "закончила работу" "завершила программу с ошибкой", "входные параметры" in captured.out
