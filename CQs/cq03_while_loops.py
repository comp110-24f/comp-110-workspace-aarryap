"""This is CQ 3 !"""

__author__ = "730672220"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0  # this is a something that keeps track of where we are
    count: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count
