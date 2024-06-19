import unittest
from typing import Any
from unittest.mock import Mock, patch

from src.external_api import found_currency
from src.utils import sum_transactions, transactions


class TestTransactions(unittest.TestCase):

    @patch("builtins.open", return_value=Mock(read=Mock(return_value='{"data": "mock_data"}')))
    def test_transactions_file_found(self, mock_open: Any) -> None:
        result = transactions
        self.assertEqual(result, {"data": "mock_data"})

    @patch("requests.get")
    def test_found_currency(self, mock_get: Any) -> None:
        mock_response = Mock()
        mock_response.text = '{"rates": {"USD": 75.0}}'
        mock_get.return_value = mock_response
        result = found_currency("USD")
        self.assertEqual(result, 75.0)

    def test_sum_transactions(self) -> None:
        transactions = [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "RUB"}},
            }
        ]
        with patch("your_script.found_currency", return_value=75.0):
            result = sum_transactions(transactions)
        self.assertEqual(result, 8221.37)


if __name__ == "main":
    unittest.main()
