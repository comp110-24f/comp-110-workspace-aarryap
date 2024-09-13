def fun(number: int, number2: int) -> int:
    """This function does simple addition, while demonstrating scope"""

    total: int = number + number2

    return total


def fun2(number: str, number2: str) -> str:

    concat: str = number + number2

    return concat


print(fun(1, 2))
print(fun2(str(1), str(2)))
print(fun2("3", "4"))
