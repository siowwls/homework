from src.masks import mask_count, mask_number_card


def mask_card_or_count(name_and_num: str) -> str:
    """
    Функция возвращает замаскированную карту или счет
    """
    if "Счет" in name_and_num:
        num = "".join([num for num in name_and_num if num.isdigit()])
        return f"Счет {mask_count(num)}"
    else:
        num = "".join([num for num in name_and_num if num.isdigit()])
        alpha = "".join([word for word in name_and_num if word.isalpha() or word == " "]).strip()
        return alpha + " " + mask_number_card(num)


def format_data_time(str_data: str) -> str:
    """
    Функция возвращает день, месяц, год
    """
    list_str_data = str_data.split("T")
    new_data = list_str_data[0].split("-")
    new_data = new_data[::-1]
    return ".".join(new_data)


print(format_data_time("2018-07-11T02:26:18.671407"))
