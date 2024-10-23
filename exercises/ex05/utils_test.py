"""EX05 - 'list' Utility Functions - defining unit tests for utils file"""

__author__ = "730672220"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_use_case_1() -> None:
    """testing only_evens function returns only evens in a typical input."""
    a: list[int] = [4, 5, 6, 7]
    assert only_evens(a) == [4, 6]


def test_only_evens_use_case_2() -> None:
    """Testing that only_evens function does not mutate list."""
    a: list[int] = [102, 45, 76]
    only_evens(a)
    assert a == [102, 45, 76]


def test_only_evens_use_case_3() -> None:
    """Testing that only_evens function returns only evens even if duplicates, in a typical input."""
    a: list[int] = [102, 102, 102]
    assert only_evens(a) == [102, 102, 102]


def test_only_evens_edge_case() -> None:
    """Testing only_evens on all odds list."""
    assert only_evens([3, 5, 7]) == []


def test_sub_use_case_1() -> None:
    """testing sub function returns should generate a list which is a subset of the input list, between the specified start index and the end index - 1 in a typical input."""
    a: list[int] = [4, 5, 6, 7]
    assert sub(a, 2, 3) == [6]


def test_sub_use_case_2() -> None:
    """Testing that sub function does not mutate list."""
    a: list[int] = [102, 45, 76]
    sub(a, 0, 1)
    assert a == [102, 45, 76]


def test_sub_edge_case_1() -> None:
    """Testing sub returns none when given empty list."""
    a: list[int] = []
    assert sub(a, 0, 1) == []


def test_sub_edge_case_2() -> None:
    """Testing sub returns none when given start index is greater than or equal to length of list."""
    a: list[int] = [100, 101, 102]
    assert sub(a, 4, 5) == []


def test_sub_edge_case_3() -> None:
    """Testing sub returns none when given end index is at most 0."""
    a: list[int] = [100, 101, 102]
    assert sub(a, 4, -5) == []


def test_add_at_index_use_case_1() -> None:
    """testing add_at_index function mutates list with added value at index in a typical input."""
    a: list[int] = [4, 5, 6, 7]
    add_at_index(a, 9, 2)
    assert a == [4, 5, 9, 6, 7]


def test_only_evens_use_case_2() -> None:
    """Testing that add_at_index function does not return anything."""
    a: list[int] = [102, 45, 76]
    assert add_at_index(a, 9, 2) is None


import pytest


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    a: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(a, 1, 3)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
