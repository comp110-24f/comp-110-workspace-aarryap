"""EX06 - Dictionary Utils """

__author__ = "730672220"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}

    for key in input_dict:
        value: str = input_dict[key]

        if value in inverted_dict:
            raise KeyError("Duplicate value found")

    inverted_dict[value] = key

    return inverted_dict


print(invert({"a": "z", "b": "y", "c": "x"}))
