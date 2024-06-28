from src.utils import open_transactions


def filtered_dict(data: list, keyword: str = "EXECUTED") -> list:
    """
    функция принимает на вход список словарей и значение для ключа state и возвращает новый спсиок, содержащий
    только те словари, у которых ключ state содержит переданное в функцию значение
    """
    new_list = [d for d in data if d.get("state") == keyword]
    return new_list


def sorted_list(data: list[dict], reversed_order: bool = True) -> list[dict]:
    """
    функция принимает на вход писок словарей и возвращает новый список, в котором исходные словари
    отсортированы по убыванию даты"
    """
    if reversed_order:
        return sorted(data, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(data, key=lambda x: x["date"], reverse=False)
