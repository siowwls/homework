import pandas as pd


def open_csv(file: str) -> pd.DataFrame:
    """
    Фунция читает файл-csv
    """
    transactions = pd.read_csv(file)
    return transactions


def open_excel(file: str) -> pd.DataFrame:
    """
    Функция читает табличный файл
    """
    data = pd.read_excel(file)
    return data
