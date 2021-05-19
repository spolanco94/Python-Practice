# Create a 'Restaurant' class, including a 'restaurant_name' and 'cuisine_type'
# attribute as well as two methods, 'describe_restaurant' to print the name and 
# cuisine type, and 'open_restaurant' to print that the restaurant is open.
class Restaurant:
    """A simple restaurant class."""

    def __init__(self, name, cuisine) -> None:
        """Initialize name and cuisine attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Print out the name and cuisine of the restaurant."""
        print(f"Welcome to {self.name.title()}!")
        print(f"Here we serve authentic {self.cuisine.title()} cuisine.\n")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open!")