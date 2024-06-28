from typing import Dict, List, Any

from src.collections_code import filter_by_keyword
from src.external_api import found_currency
from src.pandas_code import open_csv, open_excel
from src.processing import filtered_dict, sorted_list
from src.utils import open_transactions
from src.widget import format_data_time, mask_card_or_count


def count_transactions_by_category(transactions: List[Dict], categories: List[Dict]) -> Any:
    """
    Функция возвращает словарь с ключом категория, со значением кол-во операций
    """
    category_count = {category: 0 for category in categories}

    for transaction in transactions:
        for category, keywords in categories:
            for keyword in keywords:
                if keyword.lower() in transaction["description"].lower():
                    category_count[category] += 1
                    break

    return category_count


def filter_ruble_transactions(transactions: Any) -> list:
    """
    Фильтрует список транзакций, оставляя только рублевые операции
    """
    return [transaction for transaction in transactions if "руб." in transaction["description"]]


def main() -> None:
    """
    Основная функция программы для работы с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    file_type = int(input("Выберите тип файла для загрузки данных:JSON,CSV,Excel"))

    if file_type == 1:
        transactions = open_transactions("../data/operations.json")
    elif file_type == 2:
        transactions = open_csv("../data/transaction_csv")
    elif file_type == 3:
        transactions = open_excel("../data/transactions_excel.xlsx")

    status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ")
    filtered_transactions = filtered_dict(transactions, status.upper())
    if status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {status} недоступен.")

    sort_date = input("Отсортировать операции по дате? (да/нет): ")
    if sort_date.lower() == "да":
        order = input("Отсортировать по возрастанию или убыванию? (по возрастанию/по убыванию): ")
        ascending = True if order.lower() == "по возрастанию" else False
        filtered_transactions = sorted_list(filtered_transactions, ascending)

    ruble_only = input("Выводить только рублевые транзакции? (да/нет): ")
    if ruble_only.lower() == "да":
        filtered_transactions = filter_ruble_transactions(filtered_transactions)

    keyword_filter = input("Отфильтровать список транзакций по ключевому слову в описании? (да/нет): ")
    if keyword_filter.lower() == "да":
        keyword = input("Введите ключевое слово: ")
        filtered_transactions = filter_by_keyword(filtered_transactions, keyword)

    print("Распечатываю итоговый список транзакций..")
    for i in filtered_transactions:
        print(format_data_time(i["date"]), i["description"])
        if i["description"].startswith("Открытие вклада"):
            print(mask_card_or_count(i.get("to", "")))
        else:
            print(f"{mask_card_or_count(i.get('from', ''))} -> {mask_card_or_count(i.get('to', ''))}")
        print(f'{i["operationAmount"]["amount"]} руб.\n')


if __name__ == "__main__":
    main()
