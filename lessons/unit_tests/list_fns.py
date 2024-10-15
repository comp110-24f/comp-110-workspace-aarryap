"""List functions practice"""


def get_first(input: list[str]) -> str:
    """Return first element"""
    if len(input) == 0:
        return -1
    return input[0]


def remove_first(input: list[str]) -> None:
    """remove first element"""
    if len(input) > 0:
        input.pop(0)
    return None


def get_and_remove_first(input: list[str]) -> str:
    """remove first element AND return first element"""
    # first_element:str = input [0]
    first_elem: str = input[0]
    input.pop(0)
    return first_elem
    # return first_element


# edge case - unit test for when wrong input entered (empty, incorrect)
# use case - unit test for testing specific input
