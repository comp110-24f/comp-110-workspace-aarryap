"""My first CQ exercise."""

__author__ = "730672220"


# Function Definition
def mimic(message: str) -> str:
    """Repeat the input back to me."""
    return message


# Function Definition
def main() -> None:
    """print result of mimic."""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
