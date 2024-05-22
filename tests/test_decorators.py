from src.decorators import my_function


def test_my_function() -> None:
    assert my_function(1, 2) == 3
    assert my_function(4, 8) == 12
