import unittest
from typing import Any
from unittest.mock import patch

from src.utils import open_transactions, sum_transactions


class TestTransactions(unittest.TestCase):

    @patch("builtins.open", create=True)
    def test_transactions(self, mock_open: Any) -> Any:
        """
        Функция тестирует открытие файла
        """
        file = mock_open.return_value.__enter__.return_value
        file.read.return_value = '{"id": 1}'
        result = open_transactions("test_file.json")
        self.assertEqual(result, {"id": 1})

    @patch("src.utils.found_currency")
    def test_sum_transactions(self, mock_found_currency: Any) -> Any:
        """
        Функция возвращает сумму операций
        """
        mock_found_currency.return_value = 75.0
        transactions = [
            {
                "id": 1,
                "state": "executed",
                "date": "2019-07-03t18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
            }
        ]
        result = sum_transactions(transactions)
        self.assertEqual(result, 8221.37)


if __name__ == "__main__":
    unittest.main()
