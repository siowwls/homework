def mask_number_card(number: str) -> str:
    '''
    Функция маскирует номер карты
    '''
    list_card = list(number)
    stars_card = list_card[0:5] + [" "] + list_card[5:7] + ["** ****"] + [" "] + list_card[-4:]
    return "".join(stars_card)


def mask_count(number: str) -> str:
    '''
    Функция маскирует счет пользователя
    '''
    list_card_2 = list(number)
    stars_card_2 = ["**"] + list_card_2[-4:]
    return "".join(stars_card_2)
