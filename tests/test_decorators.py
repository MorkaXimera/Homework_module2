import pytest
from src.decorators import log


@log()
def test_log_err_console():
    raise ValueError('Что-то пошло не так!')


@log("log.log")
def test_log_err_file():
    raise ValueError('Что-то пошло не так!')

@log()
def test_log_console():
    print ('Всё идёт по плану!')

@log('log.log')
def test_log_ile():
    print ('Всё идёт по плану!')

