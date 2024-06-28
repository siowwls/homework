from re import IGNORECASE, compile, escape, search
from typing import Any


def filter_by_keyword(transactions: Any, keyword: Any) -> list:
    """
    Фильтрует список транзакций по ключевому слову в описании с использованием регулярных выражений
    """
    pattern = compile(r"\b" + escape(keyword) + r"\b", IGNORECASE)
    return [transaction for transaction in transactions if search(pattern, transaction["description"])]


def search_transactions(data: Any, search_string: Any) -> list:
    """
    Функция возвращает список словарей, в которой есть определенная строка
    """
    results = []
    pattern = compile(search_string, IGNORECASE)

    for transaction in data:
        if pattern.search(transaction["description"]):
            results.append(transaction)

    return results
