import pytest

from src.widget import data_time, mask_card_or_count


@pytest.mark.parametrize("s, expected_result", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                ("Счет 64686473678894779589", "Счет **9589")])
def test_mask_card_or_count(s: str, expected_result: str) -> None:
    assert mask_card_or_count(s) == expected_result


@pytest.mark.parametrize("day, expected_result2", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_data_time(day: str, expected_result2: str) -> None:
    assert data_time(day) == expected_result2
