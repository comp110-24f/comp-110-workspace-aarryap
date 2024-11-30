"""File to define Fish class."""

__author__ = "730672220"


class Fish:
    """Creating a Fish class."""

    age: int

    def __init__(self):
        """Initializong Fish class."""
        self.age = 0
        return None
        # this intializes the values for age when class Fish is called

    def one_day(self):
        """Each day each fish gets older."""
        self.age += 1
        return None
        # every time this function is called, one day will pass which will add 1 unit
        # to each fish's age, and remove 1 unit from self.hunger_score aka its hungry
