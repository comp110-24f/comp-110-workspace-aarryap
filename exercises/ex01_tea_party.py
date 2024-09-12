"""This is my Exercise 1 assignment called Tea Party."""

__author__: str = "730672220"


def main_planner(guests: int) -> None:
    """This is the main planner function which is the entrypoint of the program."""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    # Got stuck here trying different things inside of the cost function like (tea_count=tea_bags, treat_count=treats) until I relaized since tea_count is never defined, I cannot call that function, I just need to put the values I want for (tea_count, treat_count) in the parentheses
    return None


def tea_bags(people: int) -> int:
    """This is a function to tell you how many tea bags will be used based on how many guests are attending the party."""
    return people * 2


def treats(people: int) -> int:
    """This is a function which attributes 1.5 treats for each cup of tea a guest drinks."""
    treats = tea_bags = people * 2
    return int(tea_bags * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This is a function which returns the total cost, while assuming each teabag is 50 cents and each treat costs 75 cents."""
    return (tea_count * 0.50) + (treat_count * 0.75)
    # Got stuck here because I thought I could use ((tea_count)(0.5)) + ((treat_count(0.75)) to multiply the values together, but actually it was applying that value to those variables.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
