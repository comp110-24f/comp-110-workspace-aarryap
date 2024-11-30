"""Find Max file"""

__author__ = "730672220"


def find_and_remove_max(list_1: list[int]) -> int:
    if list_1 == []:
        return -1
    index = 1
    max_value: int = list_1[0]
    while index < len(list_1):
        if list_1[index] > max_value:
            max_value = list_1[index]
        index += 1
    index = 0
    while index < len(list_1):
        if list_1[index] == max_value:
            list_1.pop(index)
        else:
            index += 1
    return max_value
