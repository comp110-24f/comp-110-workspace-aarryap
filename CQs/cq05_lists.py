"""Mutating functions."""

__author__ = "730672220"


def manual_append(a_list: list[int], element: int) -> None:
    """Append the element to the a_list."""
    a_list.append(element)


def double(a_list: list[int]) -> None:
    """Double each element of the list."""
    index: int = 0
    while index < len(a_list):
        a_list[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
