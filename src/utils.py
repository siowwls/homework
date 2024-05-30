import json
from typing import List, Any
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
headers = {
    'Authorization': API_KEY
}
filename = '../data/operations.json'


def transactions(filename: str) -> dict:
    try:
        with open(filename, 'r') as f:
            data = json.loads(filename)
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except PermissionError:
        print(f"You don't have permission to read file {filename}.")
    except json.JSONDecodeError:
        print("Invalid JSON data.")


print(transactions(filename))


def found_currency(currency: Any) -> Any:
    responce = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?symbols={currency}&base=RUB",
                            headers=headers, timeout=20)
    translate = json.loads(responce.text)["rates"]["RUB"]
    return translate


def sum_transactions(transactions: list) -> float:
    all = 0.0
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == 'RUB':
            all += float(transaction['operationAmount']['amount'])
        elif transaction['operationAmount']['currency']['code'] == 'USD':
            all += float(transaction['operationAmount']['amount'] * found_currency("USD"))
        elif transaction['operationAmount']['currency']['code'] == 'EUR':
            all += float(transaction['operationAmount']['amount'] * found_currency("EUR"))
    return all


transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "RUB"
        }}}

print(sum_transactions(transaction))
