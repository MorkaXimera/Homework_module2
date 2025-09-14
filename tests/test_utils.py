import unittest
from unittest.mock import mock_open, patch

from src.utils import json_read


class TestReadJsonFile(unittest.TestCase):
    def test_json_read_file(self) -> None:
        mock_data = '{"key": "value"}'
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = json_read("dummy_path.json")
            self.assertEqual(result, {"key": "value"})


def test_json_read_incorrect_file() -> None:
    assert json_read("C:/Users/morka/PycharmProjects/Homework_2/tests/nofile.json") == []


def test_json_read_no_path() -> None:
    assert json_read() == []


def test_json_read_not_str() -> None:
    assert json_read(123) == []
