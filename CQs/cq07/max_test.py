"""Max test file"""

__author__ = "730672220"

from CQs.cq07.find_max import find_and_remove_max


def test_find_max_use_case() -> None:
    """testing find_max part of find_and_remove_max function returns expected value."""
    test_1: list[int] = [4, 5, 6, 7, 4]
    assert find_and_remove_max(test_1) == 7


def test_remove_max_use_case() -> None:
    """testing remove_max part of find_and_remove_max function mutates the input in an expected way."""
    test_1: list[int] = [4, 5, 6, 7, 4]
    find_and_remove_max(test_1)
    assert test_1 == [4, 5, 6, 4]


def test_find_and_remove_max_edge_case() -> None:
    """testing find_and_remove_max function returns correct value in case of unconventional input."""
    test_1: list[int] = []
    assert find_and_remove_max(test_1) == -1
