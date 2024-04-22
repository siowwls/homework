def updated_list(roster: list[dict], key_up: str = "EXECUTED") -> list[dict]:
    """
    функция принимает на вход список словарей и значение для ключа state и возвращает новый спсиок, содержащий
    только те словари, у которых ключ state содержит переданное в функцию значение
    """
    new_list = []
    for item in roster:
        if item["state"] == key_up:
            new_list.append(item)
    return new_list


def list_sorting(roster: list[dict], change: bool = True) -> list[dict]:
    """
    функция принимает на вход писок словарей и возвращает новый список, в котором исходные словари
    отсортированы по убыванию даты
    """
    new_updated_list = sorted(roster, key=lambda x: x["data"], reverse=change)
    return new_updated_list
