"""File to define Bear class."""

__author__ = "730672220"


class Bear:
    """Creating a Bear class."""

    age: int
    hunger_score: int
    # attributes for Bear class are given their types

    def __init__(self):
        """Initializing Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None
        # this intializes the values for age and hunger_score when class Bear is called

    def one_day(self):
        """Each day each bear gets older and lowers hunger score."""
        self.age += 1
        self.hunger_score -= 1
        return None
        # every time this function is called, one day will pass which will add 1 unit
        # to each bear's age, and remove 1 unit from self.hunger_score

    def eat(self, num_fish: int):
        """Eating fish increases hunger score."""
        self.hunger_score += num_fish
        # set self.hunger_score to add the amount of num_fish to the self.hunger_score
        # so that as num_fish increases, self.hunger_score increases
