import random

class Die:
    """Models a die with a default of 6 sides."""

    def __init__(self, sides=6) -> None:
        """Initialize die with default of 6 sides."""
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))
