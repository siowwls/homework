import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.logger import loggers

logger = loggers()

load_dotenv()

API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}
filename = "../data/operations.json"


def found_currency(currency: str) -> Any:
    """
    Функция, которая обращается к API и предоставляет данные о курсах валют
    """
    responce = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js", headers=headers, timeout=20)
    try:
        translate = json.loads(responce.text)
        result = translate["Valute"][currency]["Value"]
        logger.info(f"результат функции - {result}")
        if result:
            logger.info(f"результат функции - {result}")
            return result
        else:
            logger.error(f"Ошибка функции")
            return 1.0
    except requests.exceptions.RequestException:
        print(f"File {filename} not found.")
        logger.error("File not found.")
        return 1.0
