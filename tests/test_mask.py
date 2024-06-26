import pytest

from src.masks import mask_count, mask_number_card


@pytest.fixture
def data() -> str:
    return "7000792289606361"


def test_mask_number_card(data: str) -> None:
    """
    Возвращает измененный номер карты
    """
    assert mask_number_card(data) == "7000 79** **** 6361"


@pytest.fixture
def data_2() -> str:
    return "73654108430135874305"


def test_mask_count(data_2: str) -> None:
    """
    Возвращает замаскированный номер счета
    """
    assert mask_count(data_2) == "**4305"
