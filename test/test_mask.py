import pytest
from src.masks import mask_number_card, mask_count


@pytest.fixture
def data() -> str:
    return "7000792289606361"


def test_mask_number_card(data: str) -> None:
    assert mask_number_card(data) == "7000 79** **** 6361"


@pytest.fixture
def data_2() -> str:
    return "73654108430135874305"


def test_mask_count(data_2: str) -> None:
    assert mask_count(data_2) == "**4305"
