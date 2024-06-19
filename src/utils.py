import json
import logging
import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.external_api import found_currency
from src.logger import loggers

load_dotenv()

logger = loggers()
filename = "../data/operations.json"


def open_transactions(filename: str) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("результат функции ")
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        logger.error("File not found.")
        return []


def sum_transactions(transactions: Any) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях, возвращает тип float
    """
    all = 0.0
    if transactions.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
        all += float(transactions["operationAmount"]["amount"])
    elif transactions.get("operationAmount", {}).get("currency", {}).get("code") == "USD":
        all += float(transactions["operationAmount"]["amount"]) * found_currency("USD")
    elif transactions.get("operationAmount", {}).get("currency", {}).get("code") == "EUR":
        all += float(transactions["operationAmount"]["amount"]) * found_currency("EUR")
    else:
        logger.warning("результат функции")
    logger.info(f"результат функции - {all}")
    return all


transactions: Dict[str, Any] = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
}

# print(sum_transactions(transactions))
