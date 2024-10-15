"""testing list functions"""

from lessons.unit_tests.list_fns import get_first, get_and_remove_first, remove_first


def test_get_first_use_case() -> None:
    """testing get_first function returns the first element in a typical input."""
    a: list[str] = [4, 5, 6, 7]
    assert get_first(a) == 4


def test_get_first_edge_case() -> None:
    """Testing get_first on empty list."""
    assert get_first([]) == -1


def test_remove_first_use_case() -> None:
    """Testing remove_first reutrns nothing."""
    a: list[str] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]


def test_remove_first_edge_case() -> None:
    """Testing remove_first on empty list. Should not do anything."""
    a: list[str] = []
    remove_first(a)
    assert a == []


def test_get_and_remove_first_return_value_use_case() -> None:
    """Testing get_and_remove_first returns the first element in a typical input."""
    assert get_and_remove_first([4, 5, 6, 7]) == 4


def test_get_and_remove_first_mutation_use_case() -> None:
    """Testing that get_and_remove_first removes the first element in use case."""
    a: list[str] = [102, 45, 76]
    get_and_remove_first(a)
    assert a == [45, 76]
