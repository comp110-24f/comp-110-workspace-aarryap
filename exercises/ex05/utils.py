"""EX05 - 'list' Utility Functions - implementing list utility functions"""

__author__ = "730672220"


def only_evens(list_1: list[int]) -> list[int]:
    index = 0
    evens_list: list[int] = []
    while index < len(list_1):
        if list_1[index] % 2 == 0:
            evens_list.append(list_1[index])
        index += 1
    return evens_list


def sub(list_2: list[int], start_index: int, end_index: int) -> list[int]:
    new_list: list[int] = []
    if len(list_2) == 0 or start_index >= len(list_2) or end_index <= 0:
        return []
    if start_index < 0:
        start_index = 0
    if end_index > len(list_2):
        end_index = len(list_2)
    while start_index >= 0 and start_index <= end_index - 1:
        new_list.append(list_2[start_index])
        start_index += 1
    return new_list


def add_at_index(list_2: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(list_2):
        raise IndexError("Index is out of bounds for the input list")
    list_2.append(0)
    for i in range(len(list_2) - 2, index - 1, -1):
        list_2[i + 1] = list_2[i]
    list_2[index] = element
