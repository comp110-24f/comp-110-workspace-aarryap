"""This is CQ02!"""

__author__ = "730672220"


def guess_a_number() -> None:
    secret: int = 7
    # how to add a local variable inside the function  -> local variable: type = value
    # Logic (if, else etc) should go inside function
    x = int(input("Guess a number:"))
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    # Means that you're running the file in question, not referencing other files
    guess_a_number()
