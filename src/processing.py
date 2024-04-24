def updated_list(data: list[dict], keyword: str = "EXECUTED") -> list[dict]:
    """
    функция принимает на вход список словарей и значение для ключа state и возвращает новый спсиок, содержащий
    только те словари, у которых ключ state содержит переданное в функцию значение
    """
    result = []
    for item in data:
        if item["state"] == keyword:
            result.append(item)
    return result


def list_sorting(data: list[dict], reversed_order: bool = True) -> list[dict]:
    """
    функция принимает на вход писок словарей и возвращает новый список, в котором исходные словари
    отсортированы по убыванию даты"
    """
    return sorted(data, key=lambda x: x["date"], reverse=reversed_order)
