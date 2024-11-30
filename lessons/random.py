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


x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(y)
