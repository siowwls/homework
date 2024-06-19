import logging

from src.logger import loggers

logger = loggers()


def mask_number_card(number: str) -> str:
    """
    Функция маскирует номер карты
    """
    if len(number) == 16:
        list_card = list(number)
        stars_card = list_card[0:4] + [" "] + list_card[4:6] + [" ****"] + [" "] + list_card[-4:]
        logger.info("результат функции")
        return "".join(stars_card)
    else:
        logger.error("ошибка функции")
        return "Ошибка функции"


def mask_count(number: str) -> str:
    """
    Функция маскирует счет пользователя
    """
    if len(number) >= 4:
        list_card_2 = list(number)
        stars_card_2 = [""] + list_card_2[-4:]
        logger.info(f'результат функции - {"".join(stars_card_2)}')
        return "".join(stars_card_2)
    else:
        logger.error("Ошибка функции")
        return "Masks count"
