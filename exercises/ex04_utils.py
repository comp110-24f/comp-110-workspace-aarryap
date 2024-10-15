"""EX04 - List Utility Functions."""

__author__ = "730672220"


def all(list_of_numbers: list[int], specific_number: int) -> bool:
    if (
        list_of_numbers == []
    ):  # start with empty list situation so it will return immediately
        return False
    index: int = 0
    while index < len(list_of_numbers):
        if list_of_numbers[index] != specific_number:
            # by using not equal to allows it to return false at any point
            # and only return true if all are true
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # i think this is how to create an error statement for a func
    index: int = 1  # make this 1 not 0
    biggest_number: int = input[0]  # can make input[index] to input[0]
    while index < len(input):  # like card example from slides
        if input[index] > biggest_number:
            biggest_number = input[index]
            # don't need else statement here
        index += 1
    return biggest_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    while index < len(list_1) and index < len(list_2):
        # need to include second "index <" in order to work
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True


def extend(first_list: list[int], second_list: list[int]) -> None:
    index: int = 0
    while index < len(second_list):
        first_list.append(second_list[index])
        index += 1  # must be inside while loop to prevent infinite loop
