"""File to define River class."""

__author__ = "730672220"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

# you need to import the files with the classes used in this class


class River:
    """Creating a River class."""

    day: int  # what day of river cycle
    fish: list[Fish]  # fish population
    bears: list[Bear]  # bear population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes all fish older than 3 and bears older than 5 from the river."""
        Surviving_bears: list = []
        # create a new empty list that you will add to
        for bear in self.bears:
            if bear.age <= 5:
                Surviving_bears.append(bear)
        # we want to remove all bears older than 5
        # so we want to add all bears <= 5 in the new list
        Surviving_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                Surviving_fish.append(fish)
        # we want to remove all fish older than 3
        # so we want to add all fish <= 3 in the new list
        self.bears = Surviving_bears
        self.fish = Surviving_fish
        # set self.bears and self.fish to equal the new corresponding lists
        return None

    def bears_eating(self):
        """Counts how many fish bears are eating and removing from the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        # we iterate through self.bears in a for-in loop,
        # if the length of the list fish is >= 5
        # then we call the remove_fish function to remove 3 fish,
        # and call the bear.eat function for the bear to eat 3 fish
        return None

    def check_hunger(self):
        """Checks hunger score in bears to get rid of bears that die of starvation."""
        Healthy_bears: list = []
        # make a new list to have correct values that you add
        for bear in self.bears:
            if bear.hunger_score >= 0:
                Healthy_bears.append(bear)
        # we iterate through self.bears in a for-in loop,
        # if the bear.hunger_score is >= 0, then we add it to the new list
        # call the remove_fish function to remove 3 fish,
        self.bears = Healthy_bears
        # set self.bears to equal the new list
        return None

    def repopulate_fish(self):
        """How to count the baby fish additions to the Fish populations."""
        baby_fish = (len(self.fish) // 2) * 4
        for _ in range(0, baby_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """How to count the baby bear additions to the Bear populations."""
        baby_bears = len(self.bears) // 2
        for _ in range(0, baby_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """View river stats."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Remove fish from river."""
        for _ in range(0, amount):
            self.fish.pop(0)
