from src.app.example import random_computation


def test_random_computation() -> None:
    assert random_computation(2, 3) == 20.0
