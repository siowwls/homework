from unittest.mock import patch

import pandas as pd

from src.pandas_code import open_csv, open_excel


def test_open_csv() -> None:
    """
    Функция читает данные из файла csv
    """
    with patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame({"date": ["2023-09-05"], "amount": ["16210"]})

        result = open_csv("transaction_csv")

        mock_read_csv.assert_called_once_with("transaction_csv")
        pd.testing.assert_frame_equal(result, pd.DataFrame({"date": ["2023-09-05"], "amount": ["16210"]}))


def test_read_transactions_from_xlsx() -> None:
    """
    Функция читает финансовые транзакции с xlsx файла
    """
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame({"date": ["2023-09-05"], "amount": ["16210"]})

        result = open_excel("transaction_excel")

        mock_read_excel.assert_called_once_with("transaction_excel")
        pd.testing.assert_frame_equal(result, pd.DataFrame({"date": ["2023-09-05"], "amount": ["16210"]}))
