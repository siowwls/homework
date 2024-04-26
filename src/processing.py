def new_list_dict(data: list[dict], keyword: str = "EXECUTED") -> list[dict]:
    """
    функция принимает на вход список словарей и значение для ключа state и возвращает новый спсиок, содержащий
    только те словари, у которых ключ state содержит переданное в функцию значение
    """
    return list(filter(lambda x: x["state"] == keyword, data))


def new_sorted_list(data: list[dict], reversed_order: bool = True) -> list[dict]:
    """
    функция принимает на вход писок словарей и возвращает новый список, в котором исходные словари
    отсортированы по убыванию даты"
    """
    if reversed_order:
        return sorted(data, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(data, key=lambda x: x["date"], reverse=False)
